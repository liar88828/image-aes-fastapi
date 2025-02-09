from sqlmodel import SQLModel, Field


class UserDB(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    email: str = Field(nullable=False)
    phone: str = Field(nullable=False)
    address: str = Field(nullable=True)
    password: str = Field(nullable=False)
