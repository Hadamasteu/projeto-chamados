from flask import Flask

from config import Config

from app.database.connection import Base, engine

from app.models.usuario import Usuario
from app.models.chamado import Chamado

from app.routes.chamado_routes import chamado_bp
from app.routes.auth_routes import auth_bp
from app.routes.dashboard_routes import dashboard_bp




def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    Base.metadata.create_all(engine)

    app.register_blueprint(chamado_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app

