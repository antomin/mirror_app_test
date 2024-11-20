from datetime import datetime

from fastapi import HTTPException, status
from pydantic import BaseModel, field_validator, Field

from app.config import settings


class OrderCreateSchema(BaseModel):
    dt_start: datetime = Field(
        ...,
        title="Start date and time",
        description=f"The earliest time is {settings.START_TIME_HOUR}:00, the latest time is "
        f"{settings.END_TIME_HOUR}:00, and the minutes can only be 00 or 30, e.g., 8:30, 9:00, 9:30, etc.",
    )
    apartment_number: int = Field(..., title="Apartment number", gt=0)
    pet_name: str = Field(..., title="Pet name")
    pet_breed: str = Field(..., title="Pet breed")

    @field_validator("dt_start")
    def validate_dt_start(cls, value: datetime):
        if value.minute not in (0, 30):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The minute must be 0 or 30")
        if not (settings.START_TIME_HOUR <= value.hour < settings.END_TIME_HOUR):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="The time is out of working hours"
            )

        return value


class OrderResponseSchema(OrderCreateSchema):
    id: int
    dt_end: datetime
