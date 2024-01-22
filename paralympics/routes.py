from flask import current_app as app
def register_routes(app):
    @app.route('/')
    def hello():
        return f"Hello!"
