from datetime import datetime
from app import db


class Device(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    device_type = db.Column(db.String(33))
    operator = db.Column(db.String(33))
    time = db.Column(db.DateTime)
    success = db.Column(db.Integer)
