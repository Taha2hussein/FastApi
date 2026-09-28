from src.Repository.base import BaseRepository
from src.schema.UserSchema import UserInCreate
from src.models.db.model import User



class UserRepository(BaseRepository):
    def create_user(self,user_data: UserInCreate):
        newUser = User(**user_data.model_dump(exclude_none = True))
        self.session.add(instance = newUser)
        self.session.commit()
        self.session.refresh(instance=newUser)
        return newUser
    
    def user_exit_byEmail(self,email: str):
        user = self.session.query(User).filter_by(email=email).first()
        return bool(user)
    
    def get_user_byEmail(self,email:str):
        user = self.session.query(User).filter_by(email=email).first()
        return user
   
    def get_user_byId(self,user_id:str):
           user = self.session.query(User).filter_by(email=user_id).first()
           return user