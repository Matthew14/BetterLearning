#!flask/bin/python
from app import db
import models
db.create_all()


db.session.commit()
