from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import produto, cliente, pedido, register, auth

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicializa a aplicação FastAPI
app = FastAPI()

# Configuração de CORS
origins = [
    "http://localhost:8000", 
    # Substitua pelo endereço do seu frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Diretório dos templates HTML
templates = Jinja2Templates(directory="app/templates")

# Inclui as rotas das diferentes entidades
app.include_router(produto.router, tags=["Produtos"], prefix="/produtos")
app.include_router(cliente.router, tags=["Clientes"], prefix="/clientes")
app.include_router(pedido.router, tags=["Pedidos"], prefix="/pedidos")
app.include_router(register.router, tags=["Cadastrar"], prefix="/cadastrar")
app.include_router(auth.router, tags=["Autenticar"], prefix="/login")

# Rota de verificação de saúde
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/listaProdutos", response_class=HTMLResponse)
async def lista_produtos(request: Request):
    return templates.TemplateResponse("produtos.html", {"request": request})

@app.get("/listaClientes", response_class=HTMLResponse)
async def lista_clientes(request: Request):
    return templates.TemplateResponse("clientes.html", {"request": request})

@app.get("/listaPedidos", response_class=HTMLResponse)
async def lista_pedidos(request: Request):
    return templates.TemplateResponse("pedidos.html", {"request": request})
