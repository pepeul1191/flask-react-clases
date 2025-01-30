from flask import Blueprint, render_template

view = Blueprint('main_views', __name__, template_folder='./templates')

@view.route('/', methods=['GET'])
def index():
  return 'home'

@view.route('/hola', methods=['GET'])
def hola():
  return 'hola'

@view.route('/demo', methods=['GET'])
def demo():
  return 'demo'
  