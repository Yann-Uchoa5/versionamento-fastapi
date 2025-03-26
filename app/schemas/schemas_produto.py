from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    descricao: Optional[str] = Field(None, max_length=500)
    preco: float = Field(..., gt=0)
    estoque: int

    class Config:
        from_orm = True

class ProdutoOut(ProdutoCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_orm = True

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    descricao: Optional[str] = Field(None, max_length=500)
    preco: Optional[float] = Field(None, gt=0)

    class Config:
        from_orm = True
