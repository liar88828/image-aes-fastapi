from fastapi import APIRouter

from controller.user import UserController
from database.connect import SessionDep
from database.table.user import UserTable
from schema.response import Response

router = APIRouter(prefix="/users", tags=["users"])
user_controller=UserController()

@router.get('/')
def user_find_all(db: SessionDep):
    result = user_controller.find_all(db)
    return Response(message="success get all data user", data=result, code=200)


@router.get('/{id_user}')
def user_find_one(id_user: int, db: SessionDep):
    result = user_controller.find_by_id(db, id_user)
    return Response(code=201, message=f'success get data by id {id_user}', data=result, )


@router.post('/')
def user_create(user: UserTable, db: SessionDep):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put('/{id_user}')
def user_update(user: UserTable, id_user: int, db: SessionDep):
    result = user_controller.update(db, id_user, user)
    return Response(code=200, message=f'success update user {id_user}', data=result)


@router.delete('/{id_user}')
def user_delete(id_user: int, db: SessionDep):
    result = user_controller.delete(db, id_user)
    return Response(code=200, message=f'success delete user {id_user}', data=result)
