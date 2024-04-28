#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify

# Route definition
@app_views.route('/status', methods=['GET'])
def status():
    object_count = {

            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
    }
    return jsonify({"status": "OK"})

