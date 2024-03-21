from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (project_invested_delete,
                                project_closed_check,
                                get_project_exists,
                                project_invested_sum_min_early,
                                project_name_duplicate)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.models import Donation
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.services.invest import investing_process


router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
    summary='Создание проекта'
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.
    Создание нового благотворительного проекта.
    """
    await project_name_duplicate(charity_project.name, session)
    await charity_project_crud.get_project_id_by_name(
        charity_project.name, session
    )
    charity_project = await charity_project_crud.create(charity_project, session)
    await investing_process(charity_project, Donation, session)
    return charity_project


@router.get(
    '/',
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True,
    summary='Получение списка всех проектов'
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session),
):
    """Доступно для всех пользователей.
    Получает список всех проектов."""
    return await charity_project_crud.get_multi(session)


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    summary='Редактирование проектов'
)
async def update_charity_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.
    Запрещено меньшать сумму сбора.
    Закрытый проект нельзя отредактировать.
    """
    project = await get_project_exists(
        project_id, session
    )
    project_closed_check(project)
    if obj_in.name:
        await project_name_duplicate(obj_in.name, session)
    if obj_in.full_amount is not None:
        project_invested_sum_min_early(project, obj_in.full_amount)
    return await charity_project_crud.update(
        project, obj_in, session)


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    summary='Удаление проектов'
)
async def delete_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.
    Удалить можно только открытый проект на котором нет средств.
    Проект в котором есть донаты можно только закрыть, удалить нельзя.
    """
    project = await get_project_exists(
        project_id, session
    )
    project_invested_delete(project)
    return await charity_project_crud.remove(
        project, session)
