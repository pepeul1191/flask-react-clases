#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from main.middlewares import only_logged

view = Blueprint('admin-view', __name__, template_folder='../templates')

@view.route('/admin', methods=['GET'])
@only_logged
def index():
  locals = {
    'title': 'Home',
    'nav_active': 'home',
  }
  return render_template('home/index.html', locals=locals)