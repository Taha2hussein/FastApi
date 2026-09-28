from pydantic import BaseModel, EmailStr
from typing import Optional


class UserInCreate(BaseModel):
    email: EmailStr
    password: str
    last_name: str
    first_name: str 
    
class UserInUpdate(BaseModel):
    id: int
    email: EmailStr
    password: str
    last_name: str
    first_name: str 

class UserOutput(BaseModel):
     id: Optional[int]
     email: Optional[EmailStr]
     password: Optional[str]
     last_name: Optional[str]
     first_name: Optional[str] 
     
     
class LoginwithToken(BaseModel):
    user_token: str
    
    
class UserInLogin(BaseModel):
    email: EmailStr
    password: str