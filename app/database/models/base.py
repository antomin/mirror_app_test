from datetime import datetime

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.functions import now


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now(), server_default=now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=now(), server_default=now(), onupdate=now()
    )
