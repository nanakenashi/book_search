# -*- coding: utf-8 -*-
import csv
import os
from src import db
from src.models import Author

if __name__ == '__main__':
    db.create_all()

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(parent_dir, 'resource', 'authors.csv')

    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row.get('name', None)
            url = row.get('url', None)

            if name is not None:
                author = Author(name=name, url=url)
                db.session.add(author)

        db.session.commit()
