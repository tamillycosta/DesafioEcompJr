
from pydantic import BaseModel, EmailStr


class UserCreateRequest(BaseModel):
    username: str
    password: str
    email: EmailStr
    is_admin: bool = False

class UserCreateResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_admin: bool
