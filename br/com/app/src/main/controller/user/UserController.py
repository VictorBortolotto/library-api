from flask import request
from domain.dto.user import UserDto
from service.user.CreateUserService import CreateUserService

class UserController:
  def __init__(self, app):
    self.app = app
    self.create_user_service = CreateUserService()
    self.default_route = "/user"
    self.register_routes()

  def register_routes(self):

    @self.app.route(self.default_route, methods=['POST'])
    def create_note():
      json = request.get_json()
      user_dto = UserDto(json.get("email"), json.get("password"))
      return self.create_user_service.create_user(user_dto)