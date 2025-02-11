from flask import Blueprint, render_template, request, session, redirect
from main.database import Session
from main.models import User, Member
from main.middlewares import logged_go_admin

view = Blueprint('main_views', __name__, template_folder='./templates')

@view.route('/', methods=['GET'])
@logged_go_admin
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
  
@view.route('/sign-in', methods=['GET'])
@logged_go_admin
def sing_in():
  locals = {
    'title': 'Ingresar',
    'message': ''
  }
  return render_template('sign-in.html', locals=locals) 

@view.route('/sign-out', methods=['GET'])
def sign_out():
  session.clear()
  return redirect('/')

@view.route('/error/403', methods=['GET'])
def error_403():
  return render_template('403.html', locals=locals) 

@view.route('/error/404', methods=['GET'])
def error_404():
  return render_template('404.html', locals=locals) 

@view.route('/sign-in', methods=['POST'])
def sing_in_login():
  # data
  username = request.form.get('username')
  password = request.form.get('password')
  # blogic
  db_session = Session()
  user = db_session.query(User).filter(
    User.user_name == username,
    User.password == password
  ).first()
  if user:
    member = db_session.query(Member).filter_by(id=user.member_id).first()
    # session
    session['status'] = 'True'
    session['user'] = user.to_dict()
    session['member'] = member.to_dict()
    return redirect('/admin')
  else:
    locals = {
      'title': 'Ingresar',
      'message': 'Usuario y contraseña no existen'
    }
    return render_template('sign-in.html', locals=locals)   