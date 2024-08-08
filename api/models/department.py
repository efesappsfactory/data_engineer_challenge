from database import db


class DepartmentModel(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(30), unique=True, nullable=False)
    employees = db.relationship(
        "EmployeeModel", back_populates="department", lazy="dynamic"
    )
