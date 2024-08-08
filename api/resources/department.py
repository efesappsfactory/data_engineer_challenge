from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from database import db
from models import DepartmentModel
from schemas import DepartmentSchema


blp = Blueprint("departments", __name__, description="Operations on departments")


@blp.route("/department")
class Department(MethodView):
    @blp.arguments(DepartmentSchema)
    @blp.response(201, DepartmentSchema)
    def post(self, department_data):
        department = DepartmentModel(**department_data)

        try:
            db.session.add(department)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="There is an existing record with the same name.",
            )
        except SQLAlchemyError:
            abort(
                500,
                message="An error ocurred while trying to insert a department record.",
            )

        return department
