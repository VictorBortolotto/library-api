from repository.user.UserRepository import UserRepository
from domain.dto.user.UserResponseDto import UserResponseDto
from domain.dto.user.UserLoginRequest import UserLoginRequest
from domain.exceptions.NotFoundException import NotFoundException
from domain.exceptions.UnauthorizedException import UnauthorizedException
from utils.HashUtils import HashUtils

class UserLoginService:
  def __init__(self):
    self.user_repository = UserRepository()
    self.hash_utils = HashUtils()

  def create_user(self, userLoginRequest):
    result = self.user_repository.find_user_by_id(userLoginRequest.id)

    if result is None:
      raise NotFoundException()

    if not self.hash_utils.verify_hash(userLoginRequest.password, result.password) or userLoginRequest.email != result.email:
      raise UnauthorizedException()

    return UserLoginRequest(userLoginRequest.id,True)
