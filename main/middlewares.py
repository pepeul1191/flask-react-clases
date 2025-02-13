from functools import wraps
from flask import session, redirect, request

def not_found(e):
  # print(request.url)
  if request.method == 'GET':
    extensions_to_check = ['.css', '.js', '.woff', 'png', ]
    if any(ext in request.url for ext in extensions_to_check):
      return 'Recurso no encontrado', 404
    else:
      return redirect('/error/404')
  else:
    return 'Recurso no encontrado', 404

def only_logged(fn):
  @wraps(fn)
  def _only_logged(*args, **kwargs):
    print('1 +++++++++++++++++++++++++++++++++')
    # si la session es activaa, vamos a '/accesos/'
    user_agent = request.headers.get('User-Agent', '').lower()
    browser_agents = ['mozilla', 'chrome', 'safari', 'firefox', 'edge', 'opera']
    if any(browser in user_agent for browser in browser_agents):
      if session.get('status'):
        if session.get('status') == False:
          return redirect('/error/403')
      else:
        return redirect('/error/403')
    return fn(*args, **kwargs)
  return _only_logged

def logged_go_admin(fn):
  @wraps(fn)
  def _logged_go_admin(*args, **kwargs):
    # si la session es activaa, vamos a '/accesos/'
    if session.get('status'):
      if session.get('status'):
        return redirect('/admin')
      else:
        fn(*args, **kwargs)
    else:
      fn(*args, **kwargs)
    return fn(*args, **kwargs)
  return _logged_go_admin