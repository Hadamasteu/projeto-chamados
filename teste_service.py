from app.database.connection import SessionLocal

from app.repositories.usuario_repository import UsuarioRepository


repository = UsuarioRepository()


with SessionLocal() as session:

    usuario = repository.criar(
        session,
        nome= "Edu Costa",
        email= "edu@email.com",
        nome_usuario= "edu.costa",
        senha= "senha123",
        setor= "TI",
        permissao_gerente= False,
        permissao_ti= True
    )
