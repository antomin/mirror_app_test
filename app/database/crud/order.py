from datetime import date, timedelta, datetime
from typing import Sequence

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database.models import Order
from app.schemas.order import OrderCreateSchema


async def get_orders_by_date(date: date, session: AsyncSession) -> Sequence[Order]:
    stmt = select(Order).where(func.date(Order.created_at) == date)
    result = await session.scalars(stmt)
    return result.all()


async def create_order(order: OrderCreateSchema, session: AsyncSession) -> Order:
    order_obj = Order(**order.model_dump(), dt_end=order.dt_start + timedelta(minutes=30))
    session.add(order_obj)
    await session.commit()
    return order_obj


async def is_slot_available(dt_start: datetime, session: AsyncSession) -> bool:
    stmt = select(func.count()).where(Order.dt_start == dt_start)
    result = await session.scalar(stmt)
    return result < settings.WORKERS
