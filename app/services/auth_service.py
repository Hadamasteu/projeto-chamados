from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash

from app.repositories.usuario_repository import UsuarioRepository


class AuthService:

    def __init__(self):

        self.usuario_repository = UsuarioRepository()


    def autenticar(
        self,
        session: Session,
        nome_usuario: str,
        senha: str
    ):

        usuario = self.usuario_repository.buscar_por_nome_usuario(
            session,
            nome_usuario
        )

        if not usuario:
            return None

        if not check_password_hash(
            usuario.senha,
            senha
        ):
            return None

        return usuario