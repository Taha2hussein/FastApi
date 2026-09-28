from src.DataBase import Base, engine
from src.models.db import User

def create_tables():
    Base.metadata.create_all(bind=engine)
    
