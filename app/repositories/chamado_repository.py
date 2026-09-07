from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.chamado import Chamado


class ChamadoRepository:

    def criar(
        self,
        session: Session,
        solicitacao: str,
        usuario_id: int,
        setor: str
    ):

        chamado = Chamado(
            solicitacao=solicitacao,
            usuario_id=usuario_id,
            setor=setor
        )

        session.add(chamado)
        session.commit()

        session.refresh(chamado)

        return chamado


    def listar(self, session: Session):

        comando = (select(Chamado).options(selectinload(Chamado.usuario)))

        resultado = session.execute(comando)

        return resultado.scalars().all()


    def buscar_por_id(
        self,
        session: Session,
        chamado_id: int
    ):

        comando = select(Chamado).where(
            Chamado.id == chamado_id
        )

        resultado = session.execute(comando)

        return resultado.scalar_one_or_none()