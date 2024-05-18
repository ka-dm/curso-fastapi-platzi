
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from jwt_manager import create_token
from schemas.user import User

movie_router = APIRouter()


@movie_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin" and user.password == "admin":
        token: str = create_token(user.model_dump())
    return JSONResponse(status_code=200, content=token)
