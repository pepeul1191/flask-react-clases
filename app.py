# !/usr/bin/env python
# -*- coding: utf-8 -*-
from main.application import APP
from main.blueprints import register

if __name__ == '__main__':
  register(APP)
  # run app
  APP.run(
    debug=True,
    host='0.0.0.0',
    port=5000
  )