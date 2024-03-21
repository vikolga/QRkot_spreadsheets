from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import CharityProject, User
from app.schemas.donation import DonationBase, DonationCreate, DonationDB
from app.services.invest import investing_process


router = APIRouter()


@router.post(
    '/',
    response_model=DonationCreate,
    response_model_exclude_none=True,
    summary='Сделать пожертвование'
)
async def create_donation(
    donation: DonationBase,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Только для зарегистрированных пользователей.
    Сделать пожертвование без выбора проекта."""
    new_donation = await donation_crud.create(donation, session, user)
    await investing_process(new_donation, CharityProject, session)
    return new_donation


@router.get(
    '/',
    response_model=List[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
    summary='Список всех пожертвований'
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.
    Получить список всех сделанных пожертвований от всех пользвателей.
    """
    return await donation_crud.get_multi(session)


@router.get(
    '/my',
    response_model=List[DonationCreate],
    response_model_exclude={'user_id'},
    summary='Список моих пожертвований'
)
async def get_my_reservations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Только для авторизованных пользователей.
    Получить список моих пожертвований(авторизованного пользователя)."""
    return await donation_crud.get_by_user(
        session=session, user=user
    )
