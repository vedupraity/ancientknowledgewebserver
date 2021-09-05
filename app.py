from flask import Flask, render_template, url_for
from helpers.filters import register_filters

from blueprints.site.home import blueprint as home_blueprint
from blueprints.site.about import blueprint as about_blueprint

from blueprints.content.bhagavad_gita_hindi import blueprint as bhagavad_gita_hindi_blueprint
from blueprints.content.bhagavad_gita_english import blueprint as bhagavad_gita_english_blueprint
from blueprints.content.ramcharitmanas_hindi import blueprint as ramcharitmanas_hindi_blueprint
from blueprints.content.ramcharitmanas_english import blueprint as ramcharitmanas_english_blueprint


# Initialise flask app
app = Flask(__name__)

# Register custom filters
register_filters(app)

# Register site blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)

# Register content blueprints
app.register_blueprint(bhagavad_gita_hindi_blueprint)
app.register_blueprint(bhagavad_gita_english_blueprint)
app.register_blueprint(ramcharitmanas_hindi_blueprint)
app.register_blueprint(ramcharitmanas_english_blueprint)


if __name__ == '__main__':
    app.run(debug=True, port=5000)