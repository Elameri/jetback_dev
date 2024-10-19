import flask
from flask_cors import CORS
from jetback_dev import jetback_deploy_flask

# Initialize Flask
app = flask.Flask(__name__)
CORS(app)


# Example endpoint
@app.route('/hello')
def handler_hello():
    return flask.jsonify({"message": "Hello from Flask on JetBack.Dev :D !"})


# Deploy the Flask app
jetback_deploy_flask(app)