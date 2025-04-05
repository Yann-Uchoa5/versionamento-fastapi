from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    descricao: Optional[str] = Field(None, max_length=500)
    preco: float = Field(..., gt=0)
    estoque: int
    imagem: Optional[str] = None  # Campo opcional para a imagem em base64

    class Config:
        from_attributes = True  # Atualizado para FastAPI mais recente (substitui from_orm)

class ProdutoOut(ProdutoCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    descricao: Optional[str] = Field(None, max_length=500)
    preco: Optional[float] = Field(None, gt=0)
    estoque: Optional[int] = None
    imagem: Optional[str] = None  # Campo opcional para atualização da imagem

    class Config:
        from_attributes = True