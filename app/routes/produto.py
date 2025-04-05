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

# Rota para criar um produto
@router.post("/", response_model=schemas.ProdutoOut)
def create_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    db_produto = models.Produto(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
        estoque=produto.estoque,
        imagem=produto.imagem  # Adicionando a imagem
    )
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

# Rota para listar todos os produtos
@router.get("/", response_model=list[schemas.ProdutoOut])
def get_produtos(db: Session = Depends(get_db)):
    produtos = db.query(models.Produto).all()
    return produtos

# Rota para obter um produto por ID
@router.get("/{produto_id}", response_model=schemas.ProdutoOut)
def get_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

# Rota para atualizar um produto
@router.put("/{produto_id}", response_model=schemas.ProdutoOut)
def update_produto(produto_id: int, produto: schemas.ProdutoUpdate, db: Session = Depends(get_db)):
    db_produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    # Atualiza apenas os campos fornecidos
    if produto.nome is not None:
        db_produto.nome = produto.nome
    if produto.descricao is not None:
        db_produto.descricao = produto.descricao
    if produto.preco is not None:
        db_produto.preco = produto.preco
    if produto.estoque is not None:
        db_produto.estoque = produto.estoque
    if produto.imagem is not None:
        db_produto.imagem = produto.imagem
    
    db.commit()
    db.refresh(db_produto)
    return db_produto

# Rota para deletar um produto
@router.delete("/{produto_id}", response_model=schemas.ProdutoOut)
def delete_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    db.delete(db_produto)
    db.commit()
    return db_produto