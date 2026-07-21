from app.core.logger import setup_logger
from app.database.database import Base, engine

# Import models so SQLAlchemy registers them
from app.models.job import Job

logger = setup_logger(__name__)


def init_db():
    logger.info("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    logger.info("Database initialized successfully.")