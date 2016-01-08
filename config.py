# -*- coding: utf-8 -*-

import os
# basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'metadata.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

BOOKS_PER_PAGE = 15

WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS = 50

CSRF_ENABLED = True
SECRET_KEY = 'read-books'

LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi'
}
