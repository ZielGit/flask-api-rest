def init_routes(app):
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/users")
