from http import HTTPStatus

import httpx
from flask import Response, Blueprint, redirect, url_for

astronauts_blueprint = Blueprint(
    'astronauts', __name__
)


@astronauts_blueprint.route("/redirect-astronauts")
def redirect_astronauts():
    return redirect('http://api.open-notify.org/astros.json')


@astronauts_blueprint.route("/redirect-astronauts-local")
def redirect_astronauts_local():
    return redirect(url_for('astronauts.get_astronauts'))


@astronauts_blueprint.route("/get-astronauts")
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
