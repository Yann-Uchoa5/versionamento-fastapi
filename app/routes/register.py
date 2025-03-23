from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.core.security import get_password_hash

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    username: str = Form(..., min_length=3, max_length=20),
    email: str = Form(...),
    full_name: str = Form(None, max_length=50),
    password: str = Form(..., min_length=6),
    db: Session = Depends(get_db)
):
    # Verificar se o usuário já existe
    if db.query(models.User).filter(models.User.username == username).first():
        raise HTTPException(status_code=400, detail="Nome de usuário já está em uso.")
    
    if db.query(models.User).filter(models.User.email == email).first():
        raise HTTPException(status_code=400, detail="Email já está registrado.")

    # Criptografar a senha
    hashed_password = get_password_hash(password)

    # Criar novo usuário
    new_user = models.User(
        username=username,
        email=email,
        full_name=full_name,
        hashed_password=hashed_password
    )

    # Salvar no banco de dados
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Usuário criado com sucesso!", "user_id": new_user.id}


@router.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")