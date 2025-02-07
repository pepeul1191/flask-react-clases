#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback
from flask import Blueprint, render_template, request, redirect
from main.database import Session
from main.models import BodyPart

view = Blueprint('admin-body-part-view', __name__, template_folder='../templates')

@view.route('/admin/body-parts', methods=['GET'])
def index():
  session = Session()
  try:
    status = request.args.get('status')
    body = request.args.get('body')
    if status != None and body != None:
      message = {
        'status': status,
        'body': body
      } 
    else:
      message = None
    body_parts = session.query(BodyPart).all()
    locals = {
      'title': 'Home',
      'nav_active': 'home',
      'body_parts': body_parts,
      'message': message
    }
    return render_template('body_part/index.html', locals=locals)
  except Exception as e:
    session.rollback()  # Revertir en caso de otros errores también
    error_msg = f"Ha ocurrido un error inesperado: {str(e)}"
    print(error_msg)
    body_parts = []
    locals = {
      'title': 'Home',
      'nav_active': 'home',
      'body_parts': body_parts,
      'message': {
        'status': 'error',
        'body': 'Error al listar las partes del cuerpo'
      }
    }
    return render_template('body_part/index.html', locals=locals)
  finally:
      session.close()  # Cerrar la sesión para liberar recursos

@view.route('/admin/body-parts/add', methods=['GET'])
def add_body_part():
  locals = {
    'title': 'Home',
    'nav_active': 'home',
    'body_part': BodyPart(id=None, name='')
  }
  return render_template('body_part/detail.html', locals=locals)

@view.route('/admin/body-parts/create', methods=['POST'])
def create_body_part():
  # data
  name = request.form.get('name')
  # blogic
  session = Session()
  try:
    session = Session()
    body_part = BodyPart(
      name=name
    )
    # Agregar y confirmar la inserción en la base de datos
    session.add(body_part)
    session.commit()
    return redirect('/admin/body-parts?status=success&body=Se ha creado una nueva parte del cuerpo')
  except Exception as e:
    session.rollback()  # Revertir en caso de otros errores también
    error_msg = f"Ha ocurrido un error inesperado: {str(e)}"
    traceback.print_exc()
    return redirect('/admin/body-parts?status=danger&body=ocurrio un error al crear la nueva parte de cuerpo')
  finally:
      session.close()  # Cerrar la sesión para liberar recursos


@view.route('/admin/body-parts/update', methods=['POST'])
def update_body_part():
  # data
  id = request.form.get('id')
  name = request.form.get('name')
  # blogic
  session = Session()
  body_part = session.query(BodyPart).filter_by(id=id).first()
  if body_part:
    # Actualizar campos específicos
    body_part.name = name
    # Guardar los cambios
    session.commit()
    # Mostrar el registro actualizado
    return redirect('/admin/body-parts')
  else:
    return redirect('/admin/body-parts')

@view.route('/admin/body-parts/delete/<int:body_part_id>', methods=['GET'])
def delete_body_part(body_part_id):
  # blogic
  session = Session()
  body_part = session.query(BodyPart).filter_by(id=body_part_id).first()
  if body_part:
    session.delete(body_part)
    session.commit()
    # Mostrar el registro actualizado
    return redirect('/admin/body-parts')
  else:
    return redirect('/admin/body-parts')
  
@view.route('/admin/body-parts/edit/<int:body_part_id>', methods=['GET'])
def edit_body_part(body_part_id):
  # blogic
  session = Session()
  body_part = session.query(BodyPart).filter_by(id=body_part_id).first()
  if body_part:
    locals = {
      'title': 'Home',
      'nav_active': 'home',
      'body_part': body_part
    }
    return render_template('body_part/detail.html', locals=locals)
  else:
    return redirect('/admin/body-parts')

@view.route('/admin/demo', methods=['GET'])
def demo():
  return 'admin demo'

@view.route('/admin/home', methods=['GET'])
def home():
  return 'admin home'
  