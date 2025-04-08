from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class ClienteCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    telefone: Optional[str] = Field(None, max_length=20)
    endereco: Optional[str] = Field(None, max_length=200)

    class Config:
        from_orm = True

class ClienteOut(ClienteCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_orm = True

class ClienteUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[EmailStr]
    telefone: Optional[str] = Field(None, max_length=20)
    endereco: Optional[str] = Field(None, max_length=200)

    class Config:
        from_orm = True
