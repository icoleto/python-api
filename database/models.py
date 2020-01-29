from .db import db


class User (db.Document):
    name = db.StringField()
    lastname = db.StringField()
    gender = db.StringField()
    country = db.StringField()
    programming_languages = db.ListField(db.StringField())
