import os
# basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'metadata.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
