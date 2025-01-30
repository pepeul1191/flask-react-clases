from flask import Blueprint, render_template

api = Blueprint('admin-apis', __name__)

@api.route('/api/v1/admin/home', methods=['GET'])
def index():
  return 'api admin home'

@api.route('/api/v1/admin/hola', methods=['GET'])
def hola():
  return 'api admin hola'

@api.route('/api/v1/admin/demo', methods=['GET'])
def demo():
  return 'api admin demo'
  