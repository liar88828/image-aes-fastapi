from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from key import settings

engine = create_async_engine(url=settings.DATABASE_URL_SQLITE,
                             echo=True
                             # connect_args={"check_same_thread": False}
                             )
# noinspection PyTypeChecker
def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


SessionDep = Annotated[Session, Depends(get_session)]
