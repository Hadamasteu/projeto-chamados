from datetime import datetime

from sqlalchemy import String, ForeignKey, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.connection import Base


class Chamado(Base):

    __tablename__ = "chamados"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    data: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    solicitacao: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False
    )

    setor: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="pendente",
        nullable=False
    )

    processos: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    usuario: Mapped["Usuario"] = relationship(
        back_populates="chamados"
    )