FROM python:3.5.2-alpine

RUN apk update
RUN apk add vim git mariadb-client

WORKDIR /web
RUN git clone https://github.com/nanakenashi/book_search.git book_search
RUN pip install -r ./book_search/requirements.txt

ENV FLASK_APP /web/book_search/run.py
CMD flask run -h 0.0.0.0 -p 5000
