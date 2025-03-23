from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# -------- Cliente --------
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


# -------- Produto --------
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


# -------- Pedido --------
class PedidoCreate(BaseModel):
    cliente_id: int
    produto_id: int
    data_pedido: datetime
    status: str = Field(..., min_length=3, max_length=20)
    total: float

    class Config:
        from_orm = True


class PedidoOut(PedidoCreate):
    id: int
    cliente: ClienteOut  # Incluindo os detalhes do Cliente
    produto: ProdutoOut  # Incluindo os detalhes do Produto
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_orm = True


class PedidoUpdate(BaseModel):
    status: Optional[str] = Field(None, min_length=3, max_length=20)
    total: Optional[float]

    class Config:
        from_orm = True


# -------- Usuário --------
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    full_name: Optional[str] = Field(None, max_length=50)
    password: str = Field(..., min_length=6)

    class Config:
        from_orm = True


class UserLogin(BaseModel):
    username: str
    password: str


# -------- Autenticação --------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# -------- Resposta de Erro --------
class ErrorResponse(BaseModel):
    detail: str
