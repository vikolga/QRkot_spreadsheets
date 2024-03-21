from datetime import datetime
from typing import Optional
from pydantic import BaseModel, PositiveInt, Field


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]


class DonationCreate(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(DonationCreate):
    id: int
    user_id: int
    create_date: datetime
    invested_amount: int = Field(0)
    fully_invested: bool
    close_date: Optional[datetime]
