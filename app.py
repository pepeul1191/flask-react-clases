# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

if __name__ == '__main__':
  APP = Flask(
    __name__,
    static_folder='./static',
    static_url_path='/'
  )
  # run app
  APP.run(
    debug=True,
    host='0.0.0.0',
    port=5000
  )