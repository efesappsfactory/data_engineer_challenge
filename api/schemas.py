from marshmallow import Schema, fields


class FlatEmployeeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    datetime = fields.Str(required=True)


class FlatDepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    department = fields.Str(required=True)


class FlatJobSchema(Schema):
    id = fields.Int(dump_only=True)
    job = fields.Str(required=True)


class EmployeeSchema(FlatEmployeeSchema):
    department_id = fields.Int(required=True, load_only=True)
    department = fields.Nested(FlatDepartmentSchema(), dump_only=True)
    job_id = fields.Int(required=True, load_only=True)
    job = fields.Nested(FlatJobSchema(), dump_only=True)


class DepartmentSchema(FlatDepartmentSchema):
    employees = fields.List(fields.Nested(FlatEmployeeSchema(),
                                          dump_only=True))


class JobSchema(FlatJobSchema):
    employees = fields.List(fields.Nested(FlatEmployeeSchema(),
                                          dump_only=True))
