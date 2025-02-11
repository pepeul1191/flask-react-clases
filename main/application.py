# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_session import Session
from main.constants import INFO
from main.helpers import copyright

APP = Flask(
  __name__,
  static_folder='../static',
  static_url_path='/'
)
APP.config['SECRET_KEY'] = 'your_secret_key'
APP.config['SESSION_TYPE'] = 'filesystem'
APP.config['SESSION_PERMANENT'] = False
APP.config['SESSION_USE_SIGNER'] = True
APP.config['SESSION_KEY_PREFIX'] = 'session:'
Session(APP)

# filters/helpers in templates
@APP.context_processor
def utility_processor():
  return dict(
    copyright=copyright,
    info=INFO,
  )
