from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from app.database.connection import SessionLocal
from app.services.auth_service import AuthService

from app.utils.decorators import get_usuario_logado


auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    user_log = get_usuario_logado()
    if user_log:
        return redirect(url_for("dashboard.index"))
    
    if request.method == "GET":

        return render_template(
            "login.html"
        )


    nome_usuario = request.form.get(
        "nome_usuario"
    )

    senha = request.form.get(
        "senha"
    )


    service = AuthService()


    with SessionLocal() as session_db:

        usuario = service.autenticar(
            session=session_db,
            nome_usuario=nome_usuario,
            senha=senha
        )


    if not usuario:

        return "Usuário ou senha inválidos."

    session["usuario_id"] = usuario.id

    return redirect(url_for("dashboard.index"))


@auth_bp.route("/teste-login")
def teste_login():

    usuario_id = session.get("usuario_id")

    return f"Usuário logado: {usuario_id}"


@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("auth.login")
    )

@auth_bp.route("/usuario-logado")
def usuario_logado():

    usuario = get_usuario_logado()

    if not usuario:

        return "Nenhum usuário está logado."

    return f"""
        ID: {usuario.id}<br>
        Nome: {usuario.nome}<br>
        Usuário: {usuario.nome_usuario}<br>
        Setor: {usuario.setor}
    """

@auth_bp.route("/acesso-negado")
def acesso_negado():
    return "O usuário não tem permissão para acessar essa página!"
