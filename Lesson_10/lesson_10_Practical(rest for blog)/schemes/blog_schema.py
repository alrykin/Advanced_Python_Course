from marshmallow import Schema, fields, validates, ValidationError
#Это валидаторный фафл
class LocationSchema(Schema):
    city = fields.String()
    street = fields.String()

class PersonSchema(Schema):
    id = fields.String()
    first_name = fields.String(required=True)
    surname = fields.String()
    age = fields.Integer()
    experience = fields.Integer()
    location = fields.Nested(LocationSchema)

    @validates('age')
    def validate_age(self, value):#название может быть любым
        if value > 65:
            raise ValidationError("The age must be less than 65")
