from repository.user.UserRepository import UserRepository
from datetime import date, timedelta

class DeactivateUserService:
  def __init__(self):
    self.user_repository = UserRepository()

  def deactivate_user(self, user_id):
    delete_date = date.today() + timedelta(days=30)
    
    result = self.user_repository.update_user_is_activate(user_id, delete_date)

    if result == 0:
      raise Exception()

    return result