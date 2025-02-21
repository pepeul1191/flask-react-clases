from flask import Blueprint, render_template, request, session, redirect
from main.database import Session
from main.models import User
from main.middlewares import logged_go_admin

view = Blueprint('main_views', __name__, template_folder='./templates')

@view.route('/')
@view.route('/nosotros')
@view.route('/contacto')
@logged_go_admin
def home():
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
    'title': 'Bienvenido',
    'nav': 'home',
    'comments': comments
  }
  return render_template('home.html', locals=locals)

"""
@view.route('/nosotros')
def nosotros():
  locals = {
    'title': 'Nosotros',
    'nav': 'nosotros',
  }
  return render_template('nosotros.html', locals=locals)

@view.route('/contacto')
def contacto():
  locals = {
    'title': 'Contáctenos',
    'nav': 'contacto',
  }
  return render_template('contacto.html', locals=locals)
"""
@view.route('/error/403')
def error_403():
  return render_template('403.html')

@view.route('/error/404')
def error_404():
  return render_template('404.html'), 404

@view.route('/demo')
def demo():
  return '<h1>Bienvenido a la página de demo</h1>'

@view.route('/sign-in', methods=["GET"])
@logged_go_admin
def sign_in():
  locals = {
    'message': '',
    'title': 'Ingresar al Sitema'
  }
  return render_template('sign-in.html', locals=locals)

@view.route('/sign-out', methods=["GET"])
def sign_out():
  session.clear()
  return redirect('/')

@view.route('/react', methods=["GET"])
def react():
  return render_template('demo.html')

@view.route('/sign-in', methods=["POST"])
def sign_in_login():
  # data
  username = request.form.get('username')
  password = request.form.get('password')
  # logic
  db_session = Session()
  user = db_session.query(User).filter(
    User.user_name == username,
    User.password == password
  ).first() # SELECT * FROM un = 'asdfasd' and passowrd = ''''
  if user:
    session['status'] = True
    session['user'] = user.to_dict()
    return redirect('/admin')
  else:
    locals = {
      'message': 'Usuario y contraseña no existen',
      'title': 'Ingresar al Sitema'
    }
    return render_template('sign-in.html', locals=locals)
