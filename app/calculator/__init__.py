from flask import Blueprint

calculator = Blueprint('calculator', __name__, url_prefix='/calculator')

from . import  views