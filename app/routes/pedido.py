from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um pedido
@router.post("/", response_model=schemas.PedidoOut)
async def create_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    try:
        # Verifica se o cliente existe
        db_cliente = db.query(models.Cliente).filter(models.Cliente.id == pedido.cliente_id).first()
        if not db_cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")

        # Verifica se o produto existe
        db_produto = db.query(models.Produto).filter(models.Produto.id == pedido.produto_id).first()
        if not db_produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")

        db_pedido = models.Pedido(
            cliente_id=pedido.cliente_id,
            produto_id=pedido.produto_id,
            data_pedido=pedido.data_pedido,
            status=pedido.status,
            total=pedido.total
        )
        db.add(db_pedido)
        db.commit()
        db.refresh(db_pedido)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar pedido: {str(e)}")
    return db_pedido


@router.get("/", response_model=list[schemas.PedidoOut])
def get_pedidos(db: Session = Depends(get_db)):
    pedidos = db.query(models.Pedido).all()
    return pedidos

# Rota para obter um pedido por ID
@router.get("/{pedido_id}", response_model=schemas.PedidoOut)
def get_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

# Rota para atualizar um pedido
@router.put("/{pedido_id}", response_model=schemas.PedidoOut)
def update_pedido(pedido_id: int, pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    db_pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()
    if not db_pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    try:
        db_pedido.cliente_id = pedido.cliente_id
        db_pedido.produto_id = pedido.produto_id
        db_pedido.data_pedido = pedido.data_pedido
        db_pedido.status = pedido.status
        db_pedido.total = pedido.total
        db.commit()
        db.refresh(db_pedido)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar pedido: {str(e)}")
    
    return db_pedido

# Rota para deletar um pedido
@router.delete("/{pedido_id}", response_model=schemas.PedidoOut)
def delete_pedido(pedido_id: int, db: Session = Depends(get_db)):
    db_pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()
    if not db_pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    try:
        db.delete(db_pedido)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao deletar pedido: {str(e)}")

    return db_pedido
