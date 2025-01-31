#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .constants import CONSTANTS

def copyright(year):
  resp = f'''
    <!-- Línea divisoria y derechos reservados -->
    <div class="text-center bg-secondary py-3 mt-4">
      <p class="mb-0">© {year} Végueta. Todos los derechos reservados.</p>
    </div>
  '''
  return resp
