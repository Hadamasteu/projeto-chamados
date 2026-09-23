from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select

from app.models.processo import Processo


class ProcessoRepository:

    def criar(
        self,
        session: Session,
        descricao: str,
        chamado_id: int,
        usuario_id: int
    ):
        processo = Processo(
            descricao=descricao,
            chamado_id=chamado_id,
            usuario_id=usuario_id
        )

        session.add(processo)
        session.flush()

        return processo

    def listar_por_chamado(
        self,
        session: Session,
        chamado_id: int
    ):
        comando = (
            select(Processo)
            .options(joinedload(Processo.usuario))
            .where(Processo.chamado_id == chamado_id)
            .order_by(Processo.data)
        )

        resultado = session.execute(comando)

        return resultado.scalars().all()