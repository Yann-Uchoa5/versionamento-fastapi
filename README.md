# FastAPI CRUD Operations

This is a simple FastAPI application that provides CRUD operations for business management with Customer, Product, Orders and Appointments. The backend is powered by FastAPI, with SQLite as the database, and SQLAlchemy for ORM.

## Tecnologias Utilizadas

- **Python 3.9+**
- **FastAPI**: Framework para criação de APIs rápidas e eficientes.
- **SQLAlchemy**: ORM para gerenciar interações com o banco de dados.
- **SQLite**: Banco de dados leve para persistência de dados.

---

## Pré-requisitos

1. **Python 3.9+** instalado.
2. Gerenciador de pacotes `pip`.

---

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-diretorio>
   ```

2. **Crie e ative um ambiente virtual:**

   No Linux/macOS:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   No Windows:

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Crie o banco de dados SQLite:**
   O banco de dados será criado automaticamente ao executar o código, com base nos modelos definidos.

---

## Executando a API

1. Crie o arquivo .env com as seguintes variaveis e introduza as informações:

   ```bash
   DATABASE_PORT=
   POSTGRES_PASSWORD=
   POSTGRES_USER=
   POSTGRES_DB=fastapi
   POSTGRES_HOST=
   POSTGRES_HOSTNAME=
   ```

2. Inicie o servidor:

   ```bash
   uvicorn main:app --reload
   ```

3. Acesse a documentação interativa no navegador:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoints

### Produtos

- **GET /produtos/**: Lista todos os produtos.
- **POST /produtos/**: Cria um novo produto.
- **PUT /produtos/{produto_id}**: Atualiza um produto existente.
- **DELETE /produtos/{produto_id}**: Deleta um produto do estoque.

### Clientes

- **GET /clientes/**: Lista todos os clientes.
- **POST /medicos**: Cadastra um novo cliente.
- **PUT /clientes/{cliente_id}**: Atualiza um cliente existente.
- **DELETE /clientes/{cliente_id}**: Deleta um cliente.

### Pedidos

- **GET /pedidos/**: Lista todos os pedidos.
- **POST /pedidos/**: Cria um novo pedido.
- **PUT /pedidos/{pedido_id}**: Atualiza um pedido existente.
- **DELETE /pedidos/{pedido_id}**: Deleta um cliente.

---

## Modelos de Dados

### Produto

- **nome**: String
- **descricao**: Inteiro
- **preco**: float
- **estoque**: int
- **dosponivel**: String

### Cliente

- **nome**: String
- **email**: String
- **telefone**: String
- **endereco**: String

### Pedido

- **id**: int
- **cliente_id**: Inteiro (referência a `Cliente`)
- **cliente_id**: Inteiro (referência a `Produto`)
- **data_pedido**: dateTime
- **status**: String

---

### Requisições

- para testar as requisições do projeto utilize o **Postman** e abra o arquivo **(APi Gestão de Negócios.postman_collection.json)**.
