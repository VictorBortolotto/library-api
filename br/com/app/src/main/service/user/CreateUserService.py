from repository.user.UserRepository import UserRepository
from utils.ApiResponse import ApiResponse

class CreateUserService:
  def __init__(self):
    self.user_repository = UserRepository()

  def create_user(self, userDto):
    result = self.user_repository.find_user_by_id(userDto.email)

    if result > 0:
      return ApiResponse.conflict("User already exists.")

    result = self.user_repository.create_user(userDto)

    if result == 0:
      return ApiResponse.bad_request("Error to create user.")

    return ApiResponse.ok("User created with success.")

