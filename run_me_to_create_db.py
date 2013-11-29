#!flask/bin/python
from app import db, models

db.create_all()


db.session.commit()
