from flask import Blueprint, render_template, request, session, redirect, make_response, jsonify
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from datetime import timedelta
from main.application import REVOKED_TOKENS
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
  return render_template('home_v2.html', locals=locals) 

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
@jwt_required()
def sign_out():
  jti = get_jwt()['jti']
  REVOKED_TOKENS.append(jti)
  session.clear()
  return redirect('/')

@view.route('/error/403', methods=['GET'])
def error_403():
  return render_template('403.html', locals=locals), 403

@view.route('/error/404', methods=['GET'])
def error_404():
  return render_template('404.html', locals=locals), 404

@view.route('/sign-in', methods=['POST'])
def sing_in_login():
  # data
  data = request.get_json()
  username = data['username']
  password = data['password']
  # blogic
  db_session = Session()
  user = db_session.query(User).filter(
    User.user_name == username,
    User.password == password
  ).first()
  print(user.to_dict())
  if user:
    # Crear el token JWT
    expires = timedelta(minutes=30)  # Configura la duración del token a 1 hora
    access_token = create_access_token(identity=username, expires_delta=expires)
    # Crear respuesta y establecer cookie con JWT
    response = make_response(redirect('/admin'))
    response.set_cookie('access_token', access_token, max_age=30, httponly=True)
    # Guardar datos del usuario y miembro en la sesión
    session['status'] = 'True'
    session['user'] = user.to_dict()
    member = db_session.query(Member).filter_by(id=user.member_id).first()
    session['member'] = member.to_dict()
    return access_token, 200
  else:
    return 'Usuario y/o contraseña no válido', 500