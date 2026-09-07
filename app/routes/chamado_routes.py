from flask import Blueprint, render_template, request, redirect, url_for

from app.database.connection import SessionLocal
from app.repositories.chamado_repository import ChamadoRepository
from app.services.chamado_service import ChamadoService

from app.database.connection import SessionLocal
from app.utils.decorators import login_required, permissao_required
from app.utils.auth import get_usuario_logado


chamado_bp = Blueprint(
    "chamados",
    __name__,
    url_prefix="/chamados"
)


@chamado_bp.route("/")
@login_required
@permissao_required("permissao_ti", "permissao_gerente")
def listar_chamados():

    repository = ChamadoRepository()

    with SessionLocal() as session_db:

        chamados = repository.listar(
            session_db
        )

    return render_template(
        "chamados/lista.html",
        chamados=chamados
    )

@chamado_bp.route("/novo", methods=["GET", "POST"])
@login_required
def novo_chamado():

    usuario = get_usuario_logado()

    if request.method == "POST":

        solicitacao = request.form["solicitacao"]

        # Aqui vamos chamar o service

        service = ChamadoService()

        with SessionLocal() as session_db:
            service.abrir_chamado(
                session_db,
                usuario.id,
                solicitacao
            )

        return redirect(url_for("dashboard.index"))

    return render_template(
        "chamados/novo.html"
    )