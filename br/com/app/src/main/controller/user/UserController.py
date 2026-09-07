from flask import request
from domain.dto.user.UserDto import UserDto
from service.user.CreateUserService import CreateUserService
from domain.exceptions.ConflictException import ConflictException
from utils.ApiResponse import ApiResponse

class UserController:
  def __init__(self, app):
    self.app = app
    self.create_user_service = CreateUserService()
    self.default_route = "/user"
    self.register_routes()

  def register_routes(self):

    @self.app.route(self.default_route, methods=['POST'])
    def create_user():
      json = request.get_json()
      user_dto = UserDto(json.get("email"), json.get("password"))
      try:
        result = self.create_user_service.create_user(user_dto)

        return ApiResponse.created(
          "User created with success.",
          result.user_id
        )
      except ConflictException:
        return ApiResponse.conflict(
          "User already exists."
        )