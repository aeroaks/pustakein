from flask import render_template
from datetime import datetime
from source import app, db
from .models import Books, Authors, Books_Authors_Link

#~ @app.errorhandler(404)
#~ def not_found_error(error):
    #~ return render_template('404.html'), 404


#~ @app.errorhandler(500)
#~ def internal_error(error):
    #~ db.session.rollback()
    #~ return render_template('500.html'), 500

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')
