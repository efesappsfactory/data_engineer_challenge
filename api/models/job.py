from database import db


class JobModel(db.Model):
    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(20), unique=True, nullable=False)
    employees = db.relationship(
        "EmployeeModel", back_populates="department", lazy="dynamic"
    )
