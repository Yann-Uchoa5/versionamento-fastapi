from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    full_name: Optional[str] = Field(None, max_length=50)
    password: str = Field(..., min_length=6)

    class Config:
        from_orm = True

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str] = None

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str
