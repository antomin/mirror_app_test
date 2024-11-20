from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from app.config import settings


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        max_overflow: int = 10,
        pool_size: int = 5,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url, echo=echo, echo_pool=echo_pool, max_overflow=max_overflow, pool_size=pool_size
        )

        self.session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_maker() as session:
            yield session


db = DatabaseHelper(
    url=settings.DB.url,
    echo=settings.DB.ECHO,
    echo_pool=settings.DB.ECHO_POOL,
    pool_size=settings.DB.POOL_SIZE,
    max_overflow=settings.DB.MAX_OVERFLOW,
)
