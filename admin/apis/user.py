#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback
from flask import Blueprint, jsonify, request
from main.database import Session
from main.models import User

api = Blueprint('admin-api-user', __name__)

@api.route('/api/admin/users', methods=['GET'])
def fetch_all():
  # data
  response = None
  status = 200
  # blogic
  session = Session()
  try:
    users = session.query(User).all()
    user_list = [user.to_dict() for user in users]
    response = jsonify(user_list)
  except Exception as e:
    traceback.print_exc()
    response = jsonify({
      'message': 'Ocurrió un erro en listar los usuarios',
      'error': str(e)
    })
    status = 500
  finally:
    session.close()
  # response
  return response, status

@api.route('/api/admin/users', methods=['POST'])
def save_one():
  # data
  response = None
  status = 200
  # blogic
  session = Session()
  try:
    data = request.get_json()
    user = User(
      user_name = data['user_name'],
      password = data['password'],
      member_id = data['member_id'],
    )
    # Agregar y confirmar la inserción en la base de datos
    session.add(user)
    session.commit()
    response = str(user.id)
  except Exception as e:
    traceback.print_exc()
    response = jsonify({
      'message': 'Ocurrió un error en crear al usuario',
      'error': str(e)
    })
    status = 500
  finally:
    session.close()
  # response
  return response, status

@api.route('/api/admin/users', methods=['PUT'])
def update_one():
  # data
  response = None
  status = 200
  # blogic
  session = Session()
  try:
    data = request.get_json()
    user = session.query(User).filter_by(id=data['id']).first()
    if user:
      user.user_name = data['user_name']
      user.password = data['password']
      user.member_id = data['member_id']
      session.commit()
      response = 'ok'
    else:
      response = {
        'message': 'Ususario a editar no encontrado',
        'error': f'No hay usuario con el id {data['id']}'
      }
      status = 404
  except Exception as e:
    traceback.print_exc()
    response = jsonify({
      'message': 'Ocurrió un error en actualizar al usuario',
      'error': str(e)
    })
    status = 500
  finally:
    session.close()
  # response
  return response, status

@api.route('/api/admin/users/<int:id>', methods=['GET'])
def fetch_one(id):
  # data
  response = None
  status = 200
  # blogic
  session = Session()
  try:
    user = session.query(User).filter_by(id=id).first()
    if user:
      response = jsonify(user.to_dict())
    else:
      response = {
        'message': 'Ususario no encontrado',
        'error': f'No hay usuario con el id {id}'
      }
      status = 404
  except Exception as e:
    traceback.print_exc()
    response = jsonify({
      'message': 'Ocurrió un error en buscar al usuario',
      'error': str(e)
    })
    status = 500
  finally:
    session.close()
  # response
  return response, status

@api.route('/api/admin/users/<int:id>', methods=['DELETE'])
def delete_one(id):
  # data
  response = None
  status = 200
  # blogic
  session = Session()
  try:
    user = session.query(User).filter_by(id=id).first()
    if user:
      session.delete(user)
      session.commit()
      response = 'ok'
    else:
      response = {
        'message': 'Ususario a eliminar no encontrado',
        'error': f'No hay usuario con el id {id}'
      }
      status = 404
  except Exception as e:
    traceback.print_exc()
    response = jsonify({
      'message': 'Ocurrió un error en buscar al usuario',
      'error': str(e)
    })
    status = 500
  finally:
    session.close()
  # response
  return response, status
  
