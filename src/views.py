from flask import request, render_template
from src import app
from src.models import Author
from .lib.rakuten_books.searcher import Searcher


@app.route('/')
def index():
    lines = __line_dict()
    filter = Author.id.in_(__popular_author_ids())
    popular_authors = Author.query.filter(filter).all()

    return render_template(
            'index.html',
            lines=lines, popular_authors=popular_authors)


@app.route('/l-<int:line_id>/')
def authors(line_id):
    line = __line(line_id)
    authors = Author.query.filter_by(line=line).all()

    filter = Author.id.in_(__popular_author_ids())
    popular_authors = Author.query.filter(filter).all()

    initials = __get_initials(authors)

    return render_template(
            'authors.html',
            line=line,
            initials=initials,
            authors=authors,
            popular_authors=popular_authors)


@app.route('/a-<int:author_id>/')
def author(author_id):
    author = Author.query.filter_by(id=author_id).first()

    filter = Author.id.in_(__popular_author_ids())
    popular_authors = Author.query.filter(filter).all()

    application_id = app.config['RAKUTEN_APPLICATION_ID']
    books = Searcher(application_id).find_by({'author': author.name})

    return render_template(
            'author.html',
            author=author, popular_authors=popular_authors, books=books)


@app.route('/_books/')
def _books():
    page = request.args.get('page')
    author_id = request.args.get('author_id')
    author = Author.query.filter_by(id=author_id).first()

    searcher = Searcher(app.config['RAKUTEN_APPLICATION_ID'])
    params = {'author': author.name, 'page': page}
    books = searcher.find_by(params)

    return render_template('_parts/_books.html', books=books, page=page)


def __get_initials(authors):
    return set([author.initial for author in authors])


def __popular_author_ids():
    return [
        94,
        123,
        330,
        339,
        343,
        429,
        471,
        595,
        662,
        651,
        1032,
        1095,
        1115,
        1212,
        1253,
        1277,
        1294,
        1309,
        1345,
        1424,
    ]


def __line(line_id):
    return __line_dict()[line_id]


def __line_dict():
    return {
        1: 'あ',
        2: 'か',
        3: 'さ',
        4: 'た',
        5: 'な',
        6: 'は',
        7: 'ま',
        8: 'や',
        9: 'ら',
        10: 'わ'
    }
