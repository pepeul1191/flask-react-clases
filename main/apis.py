from flask import Blueprint, session
from main.application import REVOKED_TOKENS
from flask_jwt_extended import (get_jwt, jwt_required)


api = Blueprint('main-apis', __name__)

@api.route('/api/v1/home', methods=['GET'])
def index():
  return 'api home'

@api.route('/api/v1/hola', methods=['GET'])
def hola():
  return 'api hola'

@api.route('/api/v1/demo', methods=['GET'])
def demo():
  return 'api demo'
  
@api.route('/api/sign-out', methods=['GET'])
@jwt_required()
def signout():
  jti = get_jwt()["jti"]
  REVOKED_TOKENS.append(jti)
  session.clear()
  return 'api demo'
  