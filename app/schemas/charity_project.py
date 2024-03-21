from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, PositiveInt, validator, Extra


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None)
    full_amount: Optional[PositiveInt] = Field(None)

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., max_length=100)
    description: str = Field(...)
    full_amount: PositiveInt = Field(...)

    class Config:
        min_anystr_length = 1


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int = Field()
    fully_invested: bool = Field(False)
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class CharityProjectUpdate(CharityProjectBase):

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Название проекта не может отсутствовать!')
        return value

    @validator('description')
    def description_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Проект должен иметь описание!')
        return value

    @validator('full_amount')
    def full_amount_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Целевая сумма проекта не может быть 0!')
        return value
