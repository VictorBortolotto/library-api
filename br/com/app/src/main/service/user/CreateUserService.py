from repository.user.UserRepository import UserRepository
from domain.dto.user.UserResponseDto import UserResponseDto
from domain.exceptions.ConflictException import ConflictException

class CreateUserService:
  def __init__(self):
    self.user_repository = UserRepository()

  def create_user(self, userDto):
    result = self.user_repository.find_user_by_email(userDto.email)

    if result > 0:
      raise ConflictException()

    result = self.user_repository.create_user(userDto)

    if result == 0:
      raise Exception()

    return UserResponseDto(result)

