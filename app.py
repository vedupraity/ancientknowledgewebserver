import json
import os

from flask import Flask, render_template, url_for
from helpers.api import fetch_gitub_database_tree
from helpers.filters import register_filters

from blueprints.site import blueprint as website_blueprint
from blueprints.content import blueprint as content_blueprint

# from blueprints.site.home import blueprint as home_blueprint
# from blueprints.site.about import blueprint as about_blueprint

# from blueprints.content.bhagavad_gita_hindi import blueprint as bhagavad_gita_hindi_blueprint
# from blueprints.content.bhagavad_gita_english import blueprint as bhagavad_gita_english_blueprint
# from blueprints.content.ramcharitmanas_hindi import blueprint as ramcharitmanas_hindi_blueprint
# from blueprints.content.ramcharitmanas_english import blueprint as ramcharitmanas_english_blueprint


# Initialise flask app
app = Flask(__name__)
project_root_dir = os.path.dirname(os.path.abspath(__file__))

# Register custom filters
register_filters(app)

# Register blueprints
app.register_blueprint(website_blueprint)
app.register_blueprint(content_blueprint)

# # Register site blueprints
# app.register_blueprint(home_blueprint)
# app.register_blueprint(about_blueprint)

# # Register content blueprints
# app.register_blueprint(bhagavad_gita_hindi_blueprint)
# app.register_blueprint(bhagavad_gita_english_blueprint)
# app.register_blueprint(ramcharitmanas_hindi_blueprint)
# app.register_blueprint(ramcharitmanas_english_blueprint)


# github_database_tree = fetch_gitub_database_tree()
# github_database_json_path = os.path.join(project_root_dir, 'github_database_tree.json')
# json.dump(github_database_tree, open(github_database_json_path, 'w'), indent=4)
# print(f'saved github_database_tree.json to {github_database_json_path}')

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
