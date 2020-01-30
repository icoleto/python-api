from .db import db
from dto.user_dto import UserDto

class User (db.Document):
    id = db.StringField(primary_key=True)
    name = db.StringField()
    lastname = db.StringField()
    gender = db.StringField()
    country = db.StringField()
    programming_languages = db.ListField(db.StringField())

    def to_dto(user):
        return UserDto(str(user.id), user.name, user.lastname, user.gender, user.country, user.programming_languages)

