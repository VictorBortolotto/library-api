import grpc

from generated import user_pb2
from generated import user_pb2_grpc

from domain.dto.user.UserDto import UserDto
from service.user.CreateUserService import CreateUserService
from service.user.UserLoginService import UserLoginService
from domain.exceptions.ConflictException import ConflictException
from domain.exceptions.NotFoundException import NotFoundException
from domain.exceptions.UnauthorizedException import UnauthorizedException

class UserGrpcService(user_pb2_grpc.UserServiceServicer):

  def __init__(self):
    self.create_user_service = CreateUserService()
    self.user_login_service = UserLoginService()


  def CreateUser(self, request, context):
    userDto = UserDto(
      request.email,
      request.password
    )

    try:

      user = self.create_user_service.create_user(userDto)

      return user_pb2.UserResponse(
        user_id=user.user_id,
        message="User created with success."
      )

    except ConflictException:

      context.set_code(grpc.StatusCode.ALREADY_EXISTS)
      context.set_details("User already exists.")

      return user_pb2.UserResponse()

  def ValidateUser(self, request, context):

    user_login_request = UserDto(
      request.email,
      request.password
    )

    try:

      user = self.user_login_service.login(user_login_request)

      return user_pb2.UserLoginResponse(
        user_id=user.id,
        is_valid_login=user.is_valid_login
      )

    except NotFoundException:

      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details("User not found.")

      return user_pb2.UserLoginResponse()

    except UnauthorizedException:

      context.set_code(grpc.StatusCode.UNAUTHENTICATED)
      context.set_details("Wrong email or password.")

      return user_pb2.UserLoginResponse()
    