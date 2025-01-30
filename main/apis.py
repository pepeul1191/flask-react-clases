from flask import Blueprint, render_template

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
  