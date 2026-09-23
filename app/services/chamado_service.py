from sqlalchemy.orm import Session

from app.repositories.chamado_repository import ChamadoRepository
from app.repositories.usuario_repository import UsuarioRepository
from app.services.processo_service import ProcessoService


class ChamadoService:

    def __init__(self):

        self.chamado_repository = ChamadoRepository()
        self.usuario_repository = UsuarioRepository()
        self.processo_service = ProcessoService()


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

    def atualizar_status(self, session, chamado_id, novo_status, usuario_id):
        status_permitidos = [
            "pendente",
            "em_andamento",
            "resolvido"
        ]

        nomes_status = {
            "pendente" : "Pendente",
            "em_andamento": "Em andamento",
            "resolvido": "Resolvido"
        }

        if novo_status not in status_permitidos:
            return None, "status_invalido"

        chamado_anterior = self.chamado_repository.buscar_por_id(session, chamado_id)

        if not chamado_anterior:
            return None, "nao_encontrado"

        status_anterior = chamado_anterior.status

        if status_anterior == novo_status:
            return chamado_anterior, None

        chamado = self.chamado_repository.atualizar_status(
            session,
            chamado_id,
            novo_status
        )

        if not chamado:
            return None, "nao_encontrado"

        descricao = (
            f"Status alterado de '{nomes_status[status_anterior]}' "
            f"para '{nomes_status[novo_status]}'."
        )

        self.processo_service.criar_processo(
            session,
            descricao,
            chamado_id,
            usuario_id
        )

        return chamado, None

    def atualizar_processos(self, session, chamado_id, novos_processos):
        return self.chamado_repository.atualizar_processos(
            session,
            chamado_id,
            novos_processos
        )