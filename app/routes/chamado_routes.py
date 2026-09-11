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


@chamado_bp.route("/area-ti")
@login_required
@permissao_required("permissao_ti", "permissao_gerente")
def listar_chamados():

    repository = ChamadoRepository()

    with SessionLocal() as session_db:

        chamados = repository.listar(
            session_db
        )

    return render_template(
        "chamados/area_ti.html",
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

@chamado_bp.route("/meus-chamados")
@login_required
def meus_chamados():

    usuario = get_usuario_logado()

    service = ChamadoService()

    with SessionLocal() as session_db:

        chamados = service.listar_chamados_usuario(
            session_db,
            usuario.id
        )

    return render_template(
        "chamados/meus_chamados.html",
        chamados=chamados
    )

@chamado_bp.route("/<int:chamado_id>")
@login_required
def visualizar_chamado(chamado_id):

    service = ChamadoService()
    usuario = get_usuario_logado()

    with SessionLocal() as session_db:

        chamado, erro = service.buscar_chamado(
            session_db,
            chamado_id,
            usuario
        )

    if erro == "nao_encontrado":
        return "Chamado não encontrado", 403

    if erro == "sem_permissao":
        return "Você não tem permissão para visualizar este chamado", 403

    return render_template(
        "chamados/detalhes.html",
        chamado=chamado,
        usuario=usuario
    )

@chamado_bp.route("/<int:chamado_id>/status", methods=["POST"])
@login_required
@permissao_required("permissao_ti", "permissao_gerente")
def atualizar_status(chamado_id):
    novo_status = request.form["status"]

    service = ChamadoService()

    with SessionLocal() as session_db:
        chamado, erro = service.atualizar_status(
            session_db,
            chamado_id,
            novo_status
        )
    if erro == "status_invalido":
        return "Status inválido", 400
    
    if not chamado:
        return "Chamado não encontrado", 404

    return redirect(
        url_for(
            "chamados.visualizar_chamado",
            chamado_id=chamado.id
        )
    )