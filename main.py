"""Simple Flask."""

# Third-party imports
from flask import Flask
from flask_cors import CORS

# Local source tree imports
from simple_flask.endpoints.users import API as users_api

API = Flask(__name__)
CORS(API)
# carrega os endpoints relacionado ao usuário...
API.register_blueprint(users_api)

if __name__ == '__main__':
    API.run(debug=True)
