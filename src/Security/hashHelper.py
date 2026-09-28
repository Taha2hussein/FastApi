from datetime import datetime, timedelta, timezone
import jwt
from decouple import config


JWT_SECRET = config("JWT-SECRET")
JWT_ALGORITHM = config("JWT-ALGORITHM")


class Auth_Handler:

    @staticmethod
    def sign_JWT(user_id: int):

        payload = {
            "user_id": user_id,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
        }

        token = jwt.encode(
            payload,
            JWT_SECRET,
            algorithm=JWT_ALGORITHM
        )

        return token

    @staticmethod
    def decode_JWT(token: str):

        try:
            decoded_token = jwt.decode(
                token,
                JWT_SECRET,
                algorithms=[JWT_ALGORITHM]
            )

            return decoded_token

        except jwt.ExpiredSignatureError:
            return None

        except jwt.InvalidTokenError:
            return None