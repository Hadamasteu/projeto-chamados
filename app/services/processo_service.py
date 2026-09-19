from app.repositories.processo_repository import ProcessoRepository


class ProcessoService:

    def __init__(self):
        self.repository = ProcessoRepository()

    def criar_processo(
        self,
        session,
        descricao,
        chamado_id,
        usuario_id
    ):
        return self.repository.criar(
            session,
            descricao,
            chamado_id,
            usuario_id
        )

    def listar_processos_por_chamado(
        self,
        session,
        chamado_id
    ):
        return self.repository.listar_por_chamado(
            session,
            chamado_id
        )