from sqlmodel import SQLModel, Field


class UserTable(SQLModel, Table=True):
    name: str = Field(nullable=False)
    email: str = Field(nullable=False)
    phone: str = Field(nullable=False)
    address: str = Field(nullable=True)
    password: str = Field(nullable=False)
    # role: str = Field(nullable=False, default=RoleUser.User)
