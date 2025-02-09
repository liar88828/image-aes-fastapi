from fastapi import APIRouter, Depends
from controller.auth import AuthController
from database.connect import SessionDep
from database.table.user import UserTable
from schema.response import Response
from schema.user import UserLogin
from service.jwt_token import create_jwt, verify_jwt

router = APIRouter(prefix="/auth", tags=['auth'])
authController = AuthController()


@router.post("/login")
async def login(user: UserLogin, db: SessionDep):
    user_db = await authController.login(db, user)
    token = create_jwt(data=user_db)
    return Response(code=200, data={'access': token}, message='Login Success', )


@router.post("/register")
async def register(user: UserTable, db: SessionDep):
    user_db = await authController.register(db, user)
    token = create_jwt(data=user_db)
    return Response(code=200, data={'access': token}, message='Register Success')


@router.post("/check")
async def check(user: UserTable = Depends(verify_jwt)):
    return Response(code=200, data={'user': user}, message='check Success', )
