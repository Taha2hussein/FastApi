from bcrypt import checkpw, hashpw, gensalt

class HashHelper(object):
    
    @staticmethod
    def verfiy_password(plain_password:str, hashed_passwored:str):
        if checkpw(plain_password.encode('utf-8'),hashed_passwored.encode('utf-8')):
            return True
        else:
            return False
    
    
    def get_password_hash(plain_password: str):
        return hashpw(plain_password.encode('utf-8'),
                      gensalt()).decode()
        
        