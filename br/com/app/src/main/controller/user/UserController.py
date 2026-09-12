from flask import request
from domain.dto.user.UserDto import UserDto
from service.user.CreateUserService import CreateUserService
from service.user.UserLoginService import UserLoginService
from flasgger import swag_from
import os
from domain.exceptions.ConflictException import ConflictException
from utils.ApiResponse import ApiResponse
from domain.exceptions.NotFoundException import NotFoundException
from domain.exceptions.UnauthorizedException import UnauthorizedException

class UserController:
  def __init__(self, app):
    self.app = app
    self.create_user_service = CreateUserService()
    self.user_login_service = UserLoginService()
    self.default_route = "/user"
    self.register_routes()

  def register_routes(self):

    @self.app.route(self.default_route, methods=['POST'])
    @swag_from(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/user/create_user.yaml')))
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
      
    @self.app.route(self.default_route + "/login", methods=['POST'])
    @swag_from(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/user/login.yaml')))
    def login():
      json = request.get_json()
      user_dto = UserDto(json.get("id"), json.get("email"), json.get("password"))
      try:
        result = self.user_login_service.login(user_dto)

        return ApiResponse.ok(
          "",
          result
        )
      except NotFoundException:
        return ApiResponse.not_found(
          "User not found."
        )
      except UnauthorizedException:
        return ApiResponse.conflict(
          "Wrong email or password."
        )