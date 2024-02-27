from flask import Flask

app = Flask(__name__)


@app.route("/admin-admin")
def hello_world():
    return "<p>Hello, Mykhailo!dsadsadas</p>"


@app.route("/generate-password")
def generate_password():
    ...


@app.route("/calculate-average")
def calculate_average():
    ...


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
