from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Python World!"


@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    print ('Getting RAW Data')
    print request.get_data()
    print ('Validate JSON Format')
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'


@app.route("/fibonacci/<num>")
def fibonacciHandler(num):
    num = int(request.view_args['num'])
    response = FibonacciDto(num, fibonacci(num))
    return toJsonResponse(response)


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


class FibonacciDto:
    def __init__(self, n, value):
        self.n = n
        self.value = value


def toJsonResponse(obj):
    return Response(json.dumps(obj.__dict__), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=3001)
