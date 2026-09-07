from sqlalchemy.orm import Session

from app.repositories.chamado_repository import ChamadoRepository
from app.repositories.usuario_repository import UsuarioRepository


class ChamadoService:

    def __init__(self):

        self.chamado_repository = ChamadoRepository()
        self.usuario_repository = UsuarioRepository()


    def abrir_chamado(
        self,
        session: Session,
        usuario_id: int,
        solicitacao: str
    ):

        # 1. Verifica se o usuário existe
        usuario = self.usuario_repository.buscar_por_id(
            session,
            usuario_id
        )

        if not usuario:
            raise ValueError(
                "Usuário não encontrado."
            )


        # 2. Verifica se a solicitação foi preenchida
        if not solicitacao.strip():
            raise ValueError(
                "A solicitação não pode estar vazia."
            )


        # 3. Cria o chamado
        chamado = self.chamado_repository.criar(
            session=session,
            solicitacao=solicitacao,
            usuario_id=usuario.id,
            setor=usuario.setor
        )

        return chamado

    def listar_chamados(
        self,
        session: Session
    ):

        return self.chamado_repository.listar(
            session
        )