from flask import render_template
from src import app
from src.models import Author
from .lib.rakuten_books.searcher import Searcher


@app.route('/')
def authors():
    authors = Author.query.all()

    return render_template('authors.html', authors=authors)


@app.route('/a-<author_id>/')
def author(author_id):
    author = Author.query.filter_by(id=author_id).first()

    application_id = app.config['RAKUTEN_APPLICATION_ID']
    books = Searcher(application_id).find({'author': author.name})

    return render_template('author.html', author=author, books=books)
