#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

view = Blueprint('admin-view', __name__, template_folder='../templates')

@view.route('/admin', methods=['GET'])
def index():
  locals = {
    'title': 'Home',
    'nav_active': 'home',
  }
  return render_template('home/index.html', locals=locals)