# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from main.constants import INFO
from main.helpers import copyright

APP = Flask(
  __name__,
  static_folder='../static',
  static_url_path='/'
)

# filters/helpers in templates
@APP.context_processor
def utility_processor():
  return dict(
    copyright=copyright,
    info=INFO,
  )
