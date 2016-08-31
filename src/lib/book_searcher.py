# -*- coding: utf-8 -*-
import requests


class BookSearcher:

    URL = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20130522'

    def __init__(self, application_id):
        self.application_id = application_id

    def find(self, opts):
        query = self.__build_query(opts)
        r = requests.get(self.URL, params=query)

        return r.json()['Items']

    def __build_query(self, opts):
        query = self.__base_query()
        query.update(opts)

        return query

    def __base_query(self):
        return {
            'format': 'json',
            'applicationId': self.application_id
        }
