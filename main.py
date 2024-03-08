import random
import string

from flask import Flask
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

from blueprints.astronauts.views import astronauts_blueprint
from blueprints.customers.views import customers_blueprint

app = Flask(__name__)

app.register_blueprint(astronauts_blueprint, url_prefix='/astronauts')
app.register_blueprint(customers_blueprint, )


@app.route("/")
def hello_world():
    # print(request.args.get('a'))
    # counter =
    # return ' '.join(["Mykhailo" for i in range(int(counter))])
    return 'Hello'


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


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )
