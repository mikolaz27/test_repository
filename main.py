import pprint
import random
import string
from http import HTTPStatus

import httpx
from flask import Flask, request, Response
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

from database_handler import execute_query
from formatter import format_records

app = Flask(__name__)


# post/2024/12/12/
# post/2024/11/12/

# @app.route("/<int:counter>/")
# def hello_world(counter):
#     return ' '.join(["Mykhailo" for i in range(int(counter))])

@app.route("/")
def hello_world():
    # print(request.args.get('a'))
    # counter =
    # return ' '.join(["Mykhailo" for i in range(int(counter))])
    return 'Hello'


# GET
# ?counter=1876287&counter1=123
# in url

# POST
# body


@app.route("/generate-password")
@use_kwargs(
    {
        'password_length': fields.Int(
            missing=15,
            validate=[validate.Range(min_inclusive=True, min=8, max=100, max_inclusive=True)]
        ),
    },
    location='query'
)
def generate_password(password_length: int):
    # password_length = request.args.get('length', '10')

    # snake_case
    # CamelCase
    # kebab-case

    # full_salary
    # salary_after_something

    # for word in sentance:
    #     ...

    # coefficient = 125

    # max_password_limit = int(request.args.get('max_limit', '100'))

    # if not password_length.isdigit():
    #     return 'ERROR: should be a number'
    # password_length = int(password_length)

    # if not 8 <= password_length <= max_password_limit:
    #     return 'ERROR: should be in range [8, 100]'

    return ''.join(random.choices(
        string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation, k=password_length
    ))


@app.route("/get-astronauts")
def get_astronauts():
    url = 'http://api.open-notify.org/astros.json'
    result = httpx.get(url)

    if result.status_code not in (HTTPStatus.TOO_MANY_REQUESTS, HTTPStatus.OK,):
        return Response('ERROR:something went wrong', status=result.status_code)

    data: dict = result.json()
    statistics = {}

    for entry in data.get('people', {}):
        statistics[entry['craft']] = statistics.get(entry['craft'], 0) + 1

    return statistics


@app.route("/calculate-average")
def calculate_average():
    ...


@app.route("/get-customers")
def get_customers():
    query = 'SELECT FirstName, LastName FROM customers'
    result = execute_query(query=query)
    return format_records(result)


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )

# kebab-style
# snake_style
# CamelCase

# / % : ? @ + ~ &


# https://flask.palletsprojects.com/en/3.0.x/quickstart/#redirects-and-errors
# https | http
# SSL
# s1 -> s2 -> s3 -> c1

# flask.palletsprojects.com
# facebook.com -> 31.13.81.36
# DNS

# 5000
# 31.13.81.36:443 - https
# 31.13.81.36:80 - http
# 31.13.81.36:5432
# 31.13.81.36:587  - smtp

# en/3.0.x/quickstart

# #redirects-and-errors
