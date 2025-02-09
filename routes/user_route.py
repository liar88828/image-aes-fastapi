from fastapi import APIRouter
from controller.userDB import userDB_controller
from database.connect import SessionDep
from database.table.userDB import UserDB
from schema.response import Response

router = APIRouter(prefix="/user-new", tags=["users"])


@router.get("/")
def user_find_all(db: SessionDep) -> Response:
    data = userDB_controller.find_all(db=db)
    return Response(code=200, message=f'success get data by ', data=data)


@router.get('/{id_user}')
def user_find_one(id_user: int, db: SessionDep):
    result = userDB_controller.find_by_id(db, id_user)
    return Response(code=201, message=f'success get data by id {id_user}', data=result, )



@router.post("/")
def user_create(user: UserDB, db: SessionDep) -> Response:
    data = userDB_controller.create(db=db, user=user)
    return Response(code=201, message=f'success get data by ', data=data)


@router.put('/{id_user}')
def user_update(user: UserDB, id_user: int, db: SessionDep):
    result = userDB_controller.update(db, id_user, user)
    return Response(code=200, message=f'success update user {id_user}', data=result)


@router.delete('/{id_user}')
def user_delete(id_user: int, db: SessionDep):
    result = userDB_controller.delete(db, id_user)
    return Response(code=200, message=f'success delete user {id_user}', data=result)
