#!/usr/bin/python3
"""	
	creating flask app blueprint
"""
from flask import Blueprint

app_views = Blueprint('appviews', __name__, url_prefix='/api/v1')

from api.v1.views.index import *