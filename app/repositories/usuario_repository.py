from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.usuario import Usuario

from werkzeug.security import generate_password_hash


class UsuarioRepository:

    def criar(
        self,
        session: Session,
        nome: str,
        email: str,
        nome_usuario: str,
        senha: str,
        setor: str,
        permissao_gerente: bool = False,
        permissao_ti: bool = False
    ):

        usuario = Usuario(
            nome=nome,
            email=email,
            nome_usuario=nome_usuario,
            senha=generate_password_hash(senha),
            setor=setor,
            permissao_gerente=permissao_gerente,
            permissao_ti=permissao_ti
        )

        session.add(usuario)
        session.commit()

        session.refresh(usuario)

        return usuario


    def listar(self, session: Session):

        comando = select(Usuario)

        resultado = session.execute(comando)

        return resultado.scalars().all()


    def buscar_por_id(
        self,
        session: Session,
        usuario_id: int
    ):

        comando = select(Usuario).where(
            Usuario.id == usuario_id
        )

        resultado = session.execute(comando)

        return resultado.scalar_one_or_none()

    def buscar_por_nome_usuario(
        self,
        session,
        nome_usuario
    ):

        comando = select(Usuario).where(
            Usuario.nome_usuario == nome_usuario
        )

        resultado = session.execute(comando)

        return resultado.scalar_one_or_none()
