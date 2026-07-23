from app.core.logger import setup_logger
from app.database.database import Base, engine

# Import ALL models
from app.database import base

logger = setup_logger(__name__)


def init_db():
    logger.info("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    logger.info("Database initialized successfully.")