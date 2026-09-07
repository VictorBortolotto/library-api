from repository.client.ClientRepository import ClientRepository
from utils.ApiResponse import ApiResponse
from service.user.DeactivateUserService import DeactivateUserService
from domain.exceptions.NotFoundException import NotFoundException

class DeactivateClientService:
  def __init__(self):
    self.client_repository = ClientRepository()
    self.deactivate_user_service = DeactivateUserService()

  def deactivate_client(self, id):
    client = self.client_repository.find_client_by_id(id)

    if client is None: 
      return NotFoundException()
    
    result = self.client_repository.update_client_is_activate(id)

    if result == 0:
      return Exception() 
    
    return self.deactivate_user_service.deactivate_user(client.user_id)

    