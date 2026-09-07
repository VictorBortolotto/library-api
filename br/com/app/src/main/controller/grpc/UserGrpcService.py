import grpc

from generated import user_pb2
from generated import user_pb2_grpc

from domain.dto.user.UserDto import UserDto
from service.user.CreateUserService import CreateUserService
from domain.exceptions.ConflictException import ConflictException

class UserGrpcService(user_pb2_grpc.UserServiceServicer):

  def __init__(self):
    self.create_user_service = CreateUserService()

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

  def ValidadeUser(self, request, context):
    return super().ValidadeUser(request, context)