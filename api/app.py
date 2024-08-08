import os

from flask import Flask
from flask_smorest import Api

from database import db
import models

from resources.employee import blp as EmployeeBlueprint
from resources.department import blp as DepartmentBlueprint
from resources.job import blp as JobBlueprint
from resources.challenge_tasks import blp as ChalllengeTasksBlueprint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Globant DE Challenge - REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app)

    api.register_blueprint(EmployeeBlueprint)
    api.register_blueprint(DepartmentBlueprint)
    api.register_blueprint(JobBlueprint)
    api.register_blueprint(ChalllengeTasksBlueprint)

    return app
