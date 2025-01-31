from flask import Blueprint, render_template

view = Blueprint('main_views', __name__, template_folder='./templates')

@view.route('/', methods=['GET'])
def index():
  comments = [
    {
      'guest': 'Juan Pérez',
      'date': '10 de julio, 2023',
      'comment': 'Un lugar maravilloso para visitar con la familia. ¡Las vistas son impresionantes y el personal muy amable!'
    },
    {
      'guest': 'Ana Gómez',
      'date': '15 de julio, 2023',
      'comment': '¡Absolutamente recomendado! Un excelente lugar para desconectar y disfrutar de la naturaleza.'
    },
    {
      'guest': 'Carlos Ruiz',
      'date': '20 de julio, 2023',
      'comment': 'Muy organizado, limpio y lleno de actividades para todas las edades. Sin duda volveremos.'
    },
  ]
  locals = {
    'title': 'Home',
    'nav_active': 'home',
    'comments': comments,
  }
  return render_template('home.html', locals=locals) 

@view.route('/nosotros', methods=['GET'])
def about():
  locals = {
    'title': 'Nosotros',
    'nav_active': 'nosotros'
  }
  return render_template('nosotros.html', locals=locals) 

@view.route('/contacto', methods=['GET'])
def contact():
  locals = {
    #'title': 'Home',
    'nav_active': 'contacto'
  }
  return render_template('contacto.html', locals=locals) 
  