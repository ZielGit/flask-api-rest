from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    migrate.init_app(app, db)  # Inicializar Flask-Migrate

    # Registrar rutas
    from app.routes import init_routes
    init_routes(app)

    return app
