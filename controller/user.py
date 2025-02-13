from fastapi import HTTPException
from sqlmodel import select
from database.connect import SessionDep
from database.table.user import UserTable


# noinspection PyMethodMayBeStatic
class UserController:
    def find_all(self, db: SessionDep):
        result = db.execute(select(UserTable)).all()
        return result.scalars().all()

    def find_by_id(self, db: SessionDep, id_user: int):
        result = db.execute(select(UserTable).where(UserTable.id == id_user))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def find_by_email(self, db: SessionDep, email: str):
        result = db.get(select(UserTable).where(UserTable.email == email))
        user: UserTable | None = result.scalar_one_or_none()
        return user

    def create(self, db: SessionDep, user: UserTable) -> UserTable:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update(self, db: SessionDep, id_user: int, user: UserTable):
        exist_user = self.find_by_id(db, id_user)
        if exist_user:
            for key, value in user.model_dump().items():
                setattr(exist_user, key, value)
            db.add(exist_user)
            db.commit()
            db.refresh(exist_user)
        return exist_user

    def delete(self, db: SessionDep, id_user: int):
        exist_user = self.find_by_id(db, id_user)
        if exist_user:
            db.delete(exist_user)
            db.commit()
        return exist_user
