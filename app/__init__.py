from flask import Flask, session

from app.blueprints.citizen.routes import citizen_bp
from app.blueprints.core.routes import core_bp
from app.blueprints.government.routes import government_bp
from app.blueprints.politician.routes import politician_bp
from app.config import DevelopmentConfig
from app.extensions import babel, db


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    babel.init_app(app)

    app.register_blueprint(core_bp)
    app.register_blueprint(citizen_bp, url_prefix="/citizen")
    app.register_blueprint(government_bp, url_prefix="/government")
    app.register_blueprint(politician_bp, url_prefix="/politician")

    @babel.localeselector
    def get_locale():
        return session.get("preferred_language", app.config["BABEL_DEFAULT_LOCALE"])

    return app
