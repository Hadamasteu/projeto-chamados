from functools import wraps

from flask import session, redirect, url_for

from app.utils.auth import get_usuario_logado



def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "usuario_id" not in session:

            return redirect(
                url_for("auth.login")
            )

        return func(*args, **kwargs)

    return wrapper

def permissao_required(*permissoes):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            usuario = get_usuario_logado()

            if not usuario:
                return "Acesso negado", 403

            if not any(getattr(usuario, permissao) for permissao in permissoes):
                return "Acesso negado", 403

            return func(*args, **kwargs)

        return wrapper

    return decorator


