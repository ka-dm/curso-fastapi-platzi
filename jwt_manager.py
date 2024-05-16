import os
from dotenv import load_dotenv
from jwt import encode

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


def creat_token(data: dict):
    token: str = encode(payload=data, key=SECRET_KEY, algorithm="HS256")
    return token
