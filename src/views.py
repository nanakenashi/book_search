from flask import render_template
from src import app
from src.models import Author


@app.route('/')
def authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)


@app.route('/a-<author_id>/')
def author(author_id):
    author = Author.query.filter_by(id=author_id).first()
    return render_template('author.html', author=author)
