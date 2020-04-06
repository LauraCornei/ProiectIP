import flask
from controllers.RecommendationController import RecommendationController
from controllers.SearchController import SearchController

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.after_request
def func(response):
    response.headers["Content-type"] = "text/json"
    return response


RecommendationController.register(app, route_base='/recommendations')
SearchController.register(app, route_base='/search')


@app.route('/', methods=['GET'])
def func():
    return 'welcome'


app.run()
