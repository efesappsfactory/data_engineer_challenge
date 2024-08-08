from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from database import db
from models import JobModel
from schemas import JobSchema


blp = Blueprint("jobs", __name__, description="Operations on jobs")


@blp.route("/job")
class Job(MethodView):
    @blp.arguments(JobSchema)
    @blp.response(201, JobSchema)
    def post(self, job_data):
        job = JobModel(**job_data)

        try:
            db.session.add(job)
            db.session.commit()

        except IntegrityError:
            abort(
                400,
                message="There is an existing record with the same name.",
            )
        except SQLAlchemyError:
            abort(
                500,
                message="An error ocurred while trying to insert an job record.",
            )

        return job
