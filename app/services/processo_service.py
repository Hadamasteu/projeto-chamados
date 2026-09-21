from app.repositories.processo_repository import ProcessoRepository
from app.repositories.chamado_repository import ChamadoRepository


class ProcessoService:

    def __init__(self):
        self.repository = ProcessoRepository()
        self.chamado_repository = ChamadoRepository()

    def criar_processo(
        self,
        session,
        descricao,
        chamado_id,
        usuario_id
    ):
        descricao = descricao.strip()
        if not descricao:
            return None, "descricao_invalida"

        chamado = self.chamado_repository.buscar_por_id(
            session,
            chamado_id
        )
        if not chamado:
            return None, "chamado_nao_encontrado"

        processo = self.repository.criar(
            session,
            descricao,
            chamado_id,
            usuario_id
        )

        
        return processo, None

    def listar_processos_por_chamado(
        self,
        session,
        chamado_id
    ):
        return self.repository.listar_por_chamado(
            session,
            chamado_id
        )