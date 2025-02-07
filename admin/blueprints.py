from admin.apis import api as _api
from admin.views.body_part import view as _body_part_view
from admin.views.home import view as _admin_home_view

blueprints = [
  _api,
  _body_part_view,
  _admin_home_view,
]