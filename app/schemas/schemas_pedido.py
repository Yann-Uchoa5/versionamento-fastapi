from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .schemas_cliente import ClienteOut
from .schemas_produto import ProdutoOut

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
    cliente: ClienteOut  # Relacionamento com Cliente
    produto: ProdutoOut  # Relacionamento com Produto
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_orm = True

class PedidoUpdate(BaseModel):
    status: Optional[str] = Field(None, min_length=3, max_length=20)
    total: Optional[float]

    class Config:
        from_orm = True
