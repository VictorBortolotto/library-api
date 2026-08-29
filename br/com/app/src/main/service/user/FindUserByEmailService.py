from repository.user.UserRepository import UserRepository
from utils.ApiResponse import ApiResponse

class FindUserByEmailService:
  def __init__(self):
    self.user_repository = UserRepository()

  def find_user_by_email(self, email):
    result = self.user_repository.find_user_by_id(email)

    if result == 0: 
      return ApiResponse.not_found("User not found.")

    return ApiResponse.ok("", result)