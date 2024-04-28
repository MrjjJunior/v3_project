#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify

# Route definition
@app_views.route('/status', methods=['GET'])
def get_api_status():
    return jsonify({"status": "OK"})

    
