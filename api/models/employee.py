from database import db


class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    datetime = db.Column(db.String(20), unique=False, nullable=False)
    department_id = db.Column(
        db.Integer, db.ForeignKey("departments.id"), unique=False, nullable=False
    )
    department = db.relationship("DepartmentModel", back_populates="employees")
    job_id = db.Column(
        db.Integer, db.ForeignKey("jobs.id"), unique=False, nullable=False
    )
    job = db.relationship("JobModel", back_populates="employees")
