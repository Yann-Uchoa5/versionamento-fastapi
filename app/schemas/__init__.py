# app/schemas/__init__.py
from .schemas_produto import ProdutoCreate, ProdutoOut, ProdutoUpdate
from .schemas_cliente import ClienteCreate, ClienteOut, ClienteUpdate
from .schemas_pedido import PedidoCreate, PedidoOut, PedidoUpdate
from .schemas_usuario import UserOut  # Importando UserOut de schemas_user.py
from .schemas_auth import Token