
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def new_users():
    name = request.form["name"]
    return "id: 1, name: {}".format(name), 201

@app.route('/users/1', methods=['GET', 'DELETE'])
def users():
    if request.method == 'GET':
        return "id = 1, name= foo", 200
    if request.method == 'DELETE':
        return "", 204 

