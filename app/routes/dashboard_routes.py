from flask import Blueprint, render_template

from app.utils.decorators import login_required
from app.utils.auth import get_usuario_logado

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard"
)


@dashboard_bp.route("/")
@login_required
def index():
    usuario = get_usuario_logado()

    if usuario.permissao_gerente:
        return render_template("dashboard/gerente.html")

    if usuario.permissao_ti:
        return render_template("dashboard/ti.html")


    return render_template("dashboard/usuario.html")