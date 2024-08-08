from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from database import db
from models import EmployeeModel
from schemas import EmployeeSchema


blp = Blueprint("employees", __name__, description="Operations on employees")


@blp.route("/employee")
class Employee(MethodView):
    @blp.arguments(EmployeeSchema)
    @blp.response(201, EmployeeSchema)
    def post(self, employee_data):
        employee = EmployeeModel(**employee_data)

        try:
            db.session.add(employee)
            db.session.commit()
        except SQLAlchemyError:
            abort(
                500,
                message="An error ocurred while trying to insert an employee record.",
            )

        return employee
