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

    def listar_chamados_usuario(self, session, usuario_id):
        return self.chamado_repository.listar_chamado_por_usuario(
            session,
            usuario_id
        )

    def buscar_chamado(self, session, chamado_id, usuario):
        chamado = self.chamado_repository.buscar_por_id(session, chamado_id)
        if not chamado:
            return None, "nao_encontrado"
        if usuario.permissao_ti or usuario.permissao_gerente:
            return chamado, None
        if chamado.usuario_id == usuario.id:
            return chamado, None
        return None, "sem_permissao"

    def atualizar_status(self, session, chamado_id, novo_status):
        status_permitidos = [
            "pendente",
            "em_andamento",
            "resolvido"
        ]

        if novo_status not in status_permitidos:
            return None, "status_invalido"

        chamado = self.chamado_repository.atualizar_status(
            session,
            chamado_id,
            novo_status
        )

        if not chamado:
            return None, "nao_encontrado"

        return chamado, None