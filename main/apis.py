from flask import Blueprint, render_template

view = Blueprint('main_apis', __name__)

@view.route('/api/v1/home', methods=['GET'])
def index():
  return 'api home'

@view.route('/api/v1/hola', methods=['GET'])
def hola():
  return 'api hola'

@view.route('/api/v1/demo', methods=['GET'])
def demo():
  return 'api demo'
  