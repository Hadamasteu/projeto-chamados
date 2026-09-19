from sqlalchemy.orm import Session
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
        session.commit()
        session.refresh(processo)

        return processo

    def listar_por_chamado(
        self,
        session: Session,
        chamado_id: int
    ):
        comando = (
            select(Processo)
            .where(Processo.chamado_id == chamado_id)
            .order_by(Processo.data)
        )

        resultado = session.execute(comando)

        return resultado.scalars().all()