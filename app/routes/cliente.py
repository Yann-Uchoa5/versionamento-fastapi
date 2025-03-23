from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal

router = APIRouter()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um cliente
@router.post("/", response_model=schemas.ClienteOut)
async def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    try:
        db_cliente = models.Cliente(
            nome=cliente.nome,
            email=cliente.email,
            telefone=cliente.telefone,
            endereco=cliente.endereco
        )
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao criar cliente: {str(e)}")

# Rota para listar todos os clientes
@router.get("/", response_model=list[schemas.ClienteOut])
async def get_clientes(db: Session = Depends(get_db)):
    return db.query(models.Cliente).all()

# Rota para obter um cliente por ID
@router.get("/{cliente_id}", response_model=schemas.ClienteOut)
async def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

# Rota para atualizar um cliente
@router.put("/{cliente_id}", response_model=schemas.ClienteOut)
async def update_cliente(cliente_id: int, cliente: schemas.ClienteUpdate, db: Session = Depends(get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    try:
        # Apenas altera os campos passados na requisição
        if cliente.nome:
            db_cliente.nome = cliente.nome
        if cliente.email:
            db_cliente.email = cliente.email
        if cliente.telefone:
            db_cliente.telefone = cliente.telefone
        if cliente.endereco:
            db_cliente.endereco = cliente.endereco
        
        # Atualiza o campo 'updated_at' automaticamente
        db.commit()
        db.refresh(db_cliente)
        return db_cliente
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar cliente: {str(e)}")


# Rota para deletar um cliente
@router.delete("/{cliente_id}", response_model=schemas.ClienteOut)
async def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    try:
        db.delete(db_cliente)
        db.commit()
        return db_cliente
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao deletar cliente: {str(e)}")

