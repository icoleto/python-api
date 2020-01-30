from database.models import User
from service.user_service import get_user_by_name
from database.db import initialize_db
from flask import send_from_directory
from flask import Flask
from flask import request
from flask import jsonify
from dotenv import load_dotenv
from dto.fibonacci_dto import FibonacciDto
from utils import toJsonResponse, fibonacci
load_dotenv()


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




if __name__ == '__main__':
    app.run(debug=True, port=3001)
