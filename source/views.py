from flask import render_template, url_for, g, redirect
from datetime import datetime
from source import app, db
from .models import Books, Authors, Books_Authors_Link
from config import BOOKS_PER_PAGE, MAX_SEARCH_RESULTS, LANGUAGES
from .forms import SearchForm
from source import babel
from flask.ext.babel import gettext

#~ @app.errorhandler(404)
#~ def not_found_error(error):
    #~ return render_template('404.html'), 404

#~ @app.errorhandler(500)
#~ def internal_error(error):
    #~ db.session.rollback()
    #~ return render_template('500.html'), 500

#~ @babel.localeselector
#~ def get_locale():
    #~ return request.accept_languages.best_match(LANGUAGES.keys())

@app.before_request
def before_request():
    g.search_form = SearchForm()
    
    # a/c no 29520100013049
    # IFSC BARB0SOLAHM

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/book-list')
@app.route('/book-list/<int:page>')
def books(page=1):
    bookList = Books.query.paginate(page, BOOKS_PER_PAGE, False)
    
    return render_template('books.html',
                           title='List',
                           bookList=bookList)

@app.route('/search', methods=['POST'])
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('search_results', query=g.search_form.search.data))
    
@app.route('/search_results/<query>')
def search_results(query):
    query_str = '%' + str(query) + '%'
    search_title = Books.query.filter(Books.title.like(query_str)).all()
    search_author = Books.query.filter(Books.author_sort.like(query_str)).all()
    results = search_title + search_author
    #results = search_title
    return render_template('search_results.html',
                            query=query,
                            results=results)




