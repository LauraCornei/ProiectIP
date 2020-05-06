from flask import Flask

from flask_cors import CORS
from controllers.RecommendationController import RecommendationController
from controllers.SearchController import SearchController


app = Flask(__name__, static_url_path='/static', static_folder='public',)
app.config["DEBUG"] = True
CORS(app)

RecommendationController.register(app, route_base='/recommendations')
SearchController.register(app, route_base='/search')
app.run()
