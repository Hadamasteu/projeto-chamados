from datetime import datetime

from sqlalchemy import String, ForeignKey, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.connection import Base


class Processo(Base):
    __tablename__ = "processos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    data: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    descricao: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    chamado_id: Mapped[int] = mapped_column(
        ForeignKey("chamados.id"),
        nullable=False
    )

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False
    )

    chamado: Mapped["Chamado"] = relationship(
        back_populates="processos"
    )

    usuario: Mapped["Usuario"] = relationship()