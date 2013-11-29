import os
CSRF_ENABLED = True
SECRET_KEY = 'this-should-be-harder-to-guess'
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'BetterLearningDB.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

