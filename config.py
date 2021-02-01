import pathlib
import os


BASE_DIR = pathlib.Path(__file__).parent


class Config:
    DEBUG = True
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///' + str(BASE_DIR / 'db.sqlite3')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '(8dvwf@-b62qg(q2xold%yr4%bz-gw9@anm5w39+id_rid2ntg'
