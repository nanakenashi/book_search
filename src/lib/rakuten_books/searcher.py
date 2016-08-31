# -*- coding: utf-8 -*-
import requests
from .book import Book


class Searcher:

    URL = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20130522'

    def __init__(self, application_id):
        self.application_id = application_id

    def find(self, opts):
        query = self.__build_query(opts)
        r = requests.get(self.URL, params=query)
        books = self.__wrap_array(r.json()['Items'])

        return books

    def __build_query(self, opts):
        query = self.__base_query()
        query.update(opts)

        return query

    def __base_query(self):
        return {
            'format': 'json',
            'applicationId': self.application_id
        }

    def __wrap_array(self, rows):
        return [Book(row['Item']) for row in rows]
