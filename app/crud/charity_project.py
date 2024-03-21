from typing import Optional
from sqlalchemy import select, Boolean
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_project_by_id(
            self,
            project_id: int,
            session: AsyncSession,
    ) -> Optional[CharityProject]:
        db_project = await session.execute(
            select(CharityProject).where(
                CharityProject.id == project_id
            )
        )
        db_project = db_project.scalars().first()
        return db_project
    
    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list[dict[str, int]]:
        charity_project = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested))
        charity_projects = charity_project.scalars().all()
        list_charuty_project = []
        for project in charity_projects:
            list_charuty_project.append({
                'name': project.name,
                'time_project': project.close_date - project.create_date,
                'description': project.description
            })
        return sorted(list_charuty_project, key=lambda i: (i['time_project']))


charity_project_crud = CRUDCharityProject(CharityProject)
