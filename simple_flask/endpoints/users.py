"""Pontos de acesso de consultas relacionadas a usuários"""

from flask import Blueprint, jsonify

from simple_flask.models.db import get_users_db

API = Blueprint('users_api', __name__)


@API.route('/', methods=['GET'])
def _index():
    return jsonify("Hello .. Acesse /users - retorna usuarios.."), 200


@API.route('/users', methods=['GET'])
def _get_users():
    user = get_users_db()
    return jsonify(user), 200
