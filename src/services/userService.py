from src.Repository.userRepo import UserRepository
from src.schema import UserInCreate, UserInLogin, UserOutput, LoginwithToken
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.schema.UserSchema import UserInLogin
from src.Security.authHandler import HashHelper
from src.Security.hashHelper import Auth_Handler

class UserService:
    def __init__(self,session:Session):
        self._userRepo = UserRepository(session=session)
        
    def signup(self,userData: UserInCreate)->UserOutput:
        if self._userRepo.user_exit_byEmail(email=userData.email):
            raise HTTPException(status_code=400,detail="Login First")
        
        hased_password = HashHelper.get_password_hash(plain_password=userData.password)
        userData.password = hased_password
        return self._userRepo.create_user(user_data=userData)
    
    def login(self,userData:UserInLogin)->LoginwithToken:
        if not self._userRepo.user_exit_byEmail(email=userData.email):
            raise HTTPException(status_code=400,detail="sign up first")
        
        user = self._userRepo.get_user_byEmail(email=userData.email)
        if HashHelper.verfiy_password(plain_password=userData.password, hashed_passwored=user.password):
            token =  Auth_Handler.sign_JWT(user_id=user.id)
            if token:
                return LoginwithToken(user_token=token)
            raise HTTPException(status_code=500,detail="unable to procced login")
        raise HTTPException(status_code=400,detail="please check your credential")
        
        
    def get_user_ById(self,user_id:int):
        user = self._userRepo.get_user_byId(user_id=user_id)
        if user:
            return user
        raise HTTPException(status_code=400,detail="User not found")