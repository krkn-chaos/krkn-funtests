import requests
from flask import Flask

from utils import make_http_request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return make_http_request("https://www.google.com")


if __name__ == "__main__":
    app.run()
