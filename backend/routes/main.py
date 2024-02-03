from flask import Blueprint, jsonify
from ..models.person import Person

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Just an example route
    return "Hello, Flask App!"
