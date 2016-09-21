from src import db


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    line = db.Column(db.String(2))
    initial = db.Column(db.String(2))
    url = db.Column(db.Text)

    def __repr(self):
        return '<Author %r>' % self.name
