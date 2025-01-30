# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

APP = Flask(
  __name__,
  static_folder='../static',
  static_url_path='/'
)
