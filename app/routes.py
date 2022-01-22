from flask import Blueprint


main = Blueprint('main', __name__)

#routes
@main.route("/", methods=['GET'])
def home():
    return 'Hello World!'
