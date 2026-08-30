from repository.client.ClientRepository import ClientRepository
from utils.ApiResponse import ApiResponse

class UpdateClientService:
  def __init__(self):
    self.client_repository = ClientRepository()

  def update_client(self, id, clientDto):
    result = self.client_repository.update_client(id, clientDto)

    if result == 0: 
      return ApiResponse.bad_request("Error to update client.")

    return ApiResponse.ok("Updated with success.", clientDto)
    