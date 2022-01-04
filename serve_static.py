from flask_frozen import Freezer

from app import app

freezer = Freezer(app)

freezer.serve()
