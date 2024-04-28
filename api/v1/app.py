#!/usr/bin/python3
''' '''
from flask import Flask
from api.v1.views import app_views
from models import storage

# Create Flask app
app = Flask(__name__)

# Register blueprint
app.register_blueprint(app_views, url_prefix='/api/v1')

# Teardown app context
@app.teardown_appcontext
def teardown(exception):
    storage.close()

# Run Flask server
if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)

