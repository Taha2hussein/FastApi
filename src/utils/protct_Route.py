from fastapi import Header, Depends, status, HTTPException
from typing import Annotated, Union
from sqlalchemy.orm import Session
from src.Security.authHandler import HashHelper
from src.services.userService import UserService
from src.DataBase import get_db
from src.schema.UserSchema import UserOutput
from src.Security.hashHelper import Auth_Handler

AUTH_PREFIX = 'Bearer '

def get_current_user(session:Session=Depends(get_db),authorization:Annotated[Union[str,None],Header()]=None)->UserOutput:
    auth_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Authentication Credential "
    )
    if not authorization:
        raise auth_exception
    
    payload = Auth_Handler.decode_JWT(token=authorization[len(AUTH_PREFIX):])
    if payload and payload["user_id"]:
        try:
          user = UserService(session=session).get_user_byId(payload["user_id"])
          return UserOutput(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email
            )
        except Exception as error:
            raise error
    raise auth_exception