from flask_mongoengine import MongoEngine
import os

db = MongoEngine()


def initialize_db(app):

    dbuser = os.getenv("DB_USER")
    dbpass = os.getenv("DB_PASS")
    dbhostname = os.getenv("DB_HOSTNAME")
    app.config['MONGODB_SETTINGS'] = {
        'host': f"mongodb://{dbuser}:{dbpass}@{dbhostname}"
    }
    db.init_app(app)
