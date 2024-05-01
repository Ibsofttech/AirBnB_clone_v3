#!/usr/bin/python3
"""
    creating flask app blueprint
"""
from api.v1.views.index import *
from flask import Blueprint

app_views = Blueprint('appviews', __name__, url_prefix='/api/v1')
