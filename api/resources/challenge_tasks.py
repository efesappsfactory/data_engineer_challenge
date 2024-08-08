from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort


blp = Blueprint(
    "challenge_tasks",
    __name__,
    description="Definition of the routes that \
                    implement the challenge requirements",
)


@blp.route("/batch-load")
class BatchLoad(MethodView):
    def post(self):
        batch_load_data = request.get_json()
        if "csv-file" not in batch_load_data:
            abort(
                400,
                message="Bad request. CSV batch file is not \
                    present in your request.",
            )
        # code to insert a job into the database
        return batch_load_data


@blp.route("/number-employees-hired-by-job-and-department")
class FirstQuery(MethodView):
    def get(self):
        # code to retrieve table view from the database for the firt query.
        return {"consulta 1": "en construccion... seguimos"}


@blp.route("/employees-hired-by-department-mean")
class SecondQuery(MethodView):
    def get(self):
        # code to retrieve table view from the database for the firt query.
        return {"consulta 2": "en construccion..."}
