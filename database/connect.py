from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from key import settings

engine = create_async_engine(settings.DATABASE_URL,
                             echo=True
                             # connect_args={"check_same_thread": False}
                             )
# noinspection PyTypeChecker
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    # autocommit=False,
    # autoflush=False
)


def get_db():
    # async with async_session() as session:
    #     yield session
    db = async_session()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[AsyncSession, Depends(get_db)]
