from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Order(Base):
    __tablename__ = "orders"

    dt_start: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    dt_end: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    apartment_number: Mapped[int]
    pet_name: Mapped[str]
    pet_breed: Mapped[str]

    def __str__(self):
        return f"{self.apartment_number}({self.dt_start})"

    def __repr__(self):
        return f"<Order: {self.id}>"
