from flask import Blueprint, render_template


main = Blueprint('main', __name__)

#routes
@main.route("/", methods=['GET'])
def index():
    template_context = {}
    
    return render_template('index.html', **template_context)
