from flask import Flask


def create_app():
    # Création de l'application Flask
    app = Flask(__name__)

    # Configuration de l'application (chargement à partir de config.py)
    app.config.from_pyfile("config.py")

    # Importation et enregistrement des routes
    from app.routes import main_routes

    app.register_blueprint(main_routes)

    # Autres initialisations, par exemple, connexion à la base de données, etc.

    return app
