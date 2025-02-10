from admin.apis.user import api as _api_user
from admin.views.user import view as _view_user
from admin.views.body_part import view as _body_part_view
from admin.views.home import view as _admin_home_view

blueprints = [
  _api_user,
  _view_user,
  _body_part_view,
  _admin_home_view,
]