# -*- coding: utf-8 -*-


class Book:

    def __init__(self, raw):
        self.raw = raw

    @property
    def title(self):
        return self.raw['title']

    @property
    def author(self):
        return self.raw['author']

    @property
    def publisher_name(self):
        return self.raw['publisherName']

    @property
    def caption(self):
        return self.raw['itemCaption']

    @property
    def review_average(self):
        return self.raw['reviewAverage']

    @property
    def review_count(self):
        return self.raw['reviewCount']

    @property
    def url(self):
        return self.raw['itemUrl']

    @property
    def small_image_url(self):
        return self.raw['smallImageUrl']

    @property
    def medium_image_url(self):
        return self.raw['mediumImageUrl']

    @property
    def large_image_url(self):
        return self.raw['largeImageUrl']
