#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

view = Blueprint('admin-view', __name__, template_folder='./templates')

@view.route('/admin/hola', methods=['GET'])
def index():
  return 'admin hola'

@view.route('/admin/demo', methods=['GET'])
def demo():
  return 'admin demo'

@view.route('/admin/home', methods=['GET'])
def home():
  return 'admin home'
  