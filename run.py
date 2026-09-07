from app import create_app

from app.database.connection import SessionLocal

from app.repositories.usuario_repository import UsuarioRepository


app = create_app()

repository = UsuarioRepository()


if __name__ == "__main__":

    with SessionLocal() as session:

        usuarios = repository.listar(session)

        print("\n=== USUÁRIOS ===")

        for usuario in usuarios:

            print(
                f"{usuario.id} | "
                f"{usuario.nome} | "
                f"{usuario.email} | "
                f"{usuario.setor}"
            )

    app.run(debug=True)