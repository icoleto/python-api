from flask import Flask
from flask import request
from flask import jsonify

import json
    
print ('you are here')
app = Flask(__name__)
 
@app.route("/")
def hello():
        return "Hello Python World!"
 
@app.route('/postjson', methods = ['POST'])
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
    print(num)
    response = FibonacciDto(num, fibonacci(num))
    print(response)
    return toJson(response)

    

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci (n-2)
    

class FibonacciDto:
    def __init__(self, n, value):
        self.n = n
        self.value = value


def toJson(obj):
    return json.dumps(obj.__dict__)