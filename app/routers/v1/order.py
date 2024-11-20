from fastapi import APIRouter, Path, Depends, HTTPException
from typing import Annotated
from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.crud.order import get_orders_by_date, create_order, is_slot_available
from app.database.models import db
from app.schemas.order import OrderResponseSchema, OrderCreateSchema

router = APIRouter(prefix="/order")


@router.get("/{date}", response_model=list[OrderResponseSchema])
async def orders_by_date_router(
    date: Annotated[date, Path(title="Date of orders in ISO format")],
    session: Annotated[AsyncSession, Depends(db.get_session)],
):
    orders = await get_orders_by_date(date=date, session=session)

    return orders


@router.post("/", response_model=OrderResponseSchema)
async def create_order_router(
    order: OrderCreateSchema,
    session: Annotated[AsyncSession, Depends(db.get_session)],
):
    if await is_slot_available(dt_start=order.dt_start, session=session):
        order = await create_order(order=order, session=session)
        return order

    raise HTTPException(status_code=400, detail="This time is busy")