#!/usr/bin/python3
""""
    creating flask app; app_view
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """"
       give a Json response for RESFUL API
    """
    response = {'status': "OK"}
    return jsonify(response)
