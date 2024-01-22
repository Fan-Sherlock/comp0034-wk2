import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # configure the Flask app (see later notes on how to generate your own secret key)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # Set the location of the database file called paralympics.sqlite in the instance folder that you created earlier.
        SQLALCHEMY_DATABASE_URI= "sqlite:///" + os.path.join(app.instance_path, "paralympics.sqlite"),
    )

    if test_config is None:
       # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        # Register the routes with the app in the context
        from .routes import register_routes
        register_routes(app)

    return app