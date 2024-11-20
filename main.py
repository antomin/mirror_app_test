import logging

import uvicorn
from fastapi import FastAPI
from loguru import logger

from app.config import settings
from app.routers import router


def _set_loggers() -> None:
    logger.add("logs/bot.log", rotation="00:00", level="ERROR", enqueue=True)
    logging.basicConfig(level=settings.LOG_LEVEL)


def start_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    return app


if __name__ == "__main__":
    _set_loggers()
    logger.info("Start application...")
    try:
        uvicorn.run(
            "main:start_app",
            factory=True,
            host="0.0.0.0",
            port=8000,
            workers=1,
            log_level=settings.LOG_LEVEL.lower(),
        )
    except KeyboardInterrupt:
        logger.info("Application stopped")
