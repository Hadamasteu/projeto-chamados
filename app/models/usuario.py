from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.connection import Base


class Usuario(Base):

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    nome_usuario: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    senha: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    setor: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    permissao_gerente: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    permissao_ti: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    chamados: Mapped[list["Chamado"]] = relationship(
        back_populates="usuario"
    )