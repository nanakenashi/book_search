from flask import render_template
from src import app
from src.models import Author


@app.route('/')
def index():
    authors = Author.query.all()
    return render_template('index.html', authors=authors)
