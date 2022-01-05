import os

from flask import Flask

from blueprints.site import blueprint as website_blueprint
from blueprints.content import blueprint as content_blueprint


# Initialise flask app
app = Flask(__name__)
project_root_dir = os.path.dirname(os.path.abspath(__file__))

# Register blueprints
app.register_blueprint(website_blueprint)
app.register_blueprint(content_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
