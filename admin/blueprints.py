from .views.home import view as view_home
from .views.user import view as view_user
from .views.body_part import view as view_body_part
from .apis.user import api as api_user

blueprints = [
  view_home,
  view_body_part,
  view_user,
  api_user,
]