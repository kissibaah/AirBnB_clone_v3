#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import jasonify
from api.v1.views import app_views

@app_views.route('status')
def api_status():
    """

    """
    response = {'status': "0k"}
    return jsonify(response)