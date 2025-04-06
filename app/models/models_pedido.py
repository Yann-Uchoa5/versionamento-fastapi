from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, TIMESTAMP, func
from sqlalchemy.orm import relationship
from ..database import Base

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)  
    data_pedido = Column(DateTime, nullable=False, server_default=func.now())
    status = Column(String, nullable=False)
    total = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())

    # Relacionamentos
    cliente = relationship("Cliente", back_populates="pedidos")  
    produto = relationship("Produto")
