from database.models import User
from service.user_service import get_user_by_name
from database.db import initialize_db
from flask import send_from_directory
from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
from dotenv import load_dotenv
load_dotenv()

from database.db import initialize_db
from database.models import User
import json

app = Flask(__name__)


initialize_db(app)


@app.route("/")
def hello():
    return "Hello Python World!"


@app.route("/fibonacci/<num>")
def fibonacciHandler(num):
    num = int(request.view_args['num'])
    response = FibonacciDto(num, fibonacci(num))
    return toJsonResponse(response)


@app.route('/user')
def findUserByName():
    name = request.args.get('name')
    users = get_user_by_name(name)
    return toJsonResponse(users)


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


class FibonacciDto:
    def __init__(self, n, value):
        self.n = n
        self.value = value


def toJsonResponse(obj):
    if hasattr(type(obj), '__iter__'):
        return Response(obj.to_json(), mimetype='application/json')
    else:
        return Response(json.dumps(obj.__dict__), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=3001)
