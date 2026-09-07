from flask import session

from app.database.connection import SessionLocal
from app.repositories.usuario_repository import UsuarioRepository

def get_usuario_logado():

    usuario_id = session.get("usuario_id")

    if not usuario_id:
        return None

    repository = UsuarioRepository()

    with SessionLocal() as session_db:

        usuario = repository.buscar_por_id(
            session_db,
            usuario_id
        )

    return usuario