from datetime import datetime

from sqlalchemy.orm import Mapped

from .base import Base


class Order(Base):
    __tablename__ = "orders"

    dt_start: Mapped[datetime]
    dt_end: Mapped[datetime]
    apartment_number: Mapped[int]
    pet_name: Mapped[str]
    pet_breed: Mapped[str]

    def __str__(self):
        return f"{self.apartment_number}({self.dt_start})"

    def __repr__(self):
        return f"<Order: {self.id}>"
