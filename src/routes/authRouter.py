from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from src.models import UserInCreate, UserInLogin, UserOutput, LoginwithToken
from src.DataBase import get_db
from src.services.userService import UserService
authRouter = APIRouter()

@authRouter.post("/login",status_code=200,response_model=LoginwithToken)
async def login(request: UserInLogin,session:Session=Depends(get_db)):
    try:
        return UserService(session=session).login(userData=request)
    except Exception as error:
        raise error

@authRouter.post("/signup",status_code=201,response_model=UserOutput)
async def signup(request: UserInCreate,session:Session=Depends(get_db)):
    try:
        return UserService(session=session).signup(userData=request)
    except Exception as error:
        raise error

