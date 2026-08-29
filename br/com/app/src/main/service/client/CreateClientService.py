from repository.client.ClientRepository import ClientRepository
from utils.ApiResponse import ApiResponse

class CreateClientService:
  def __init__(self):
    self.client_repository = ClientRepository()

  def create_client(self, clientDto):
    result = self.client_repository.create_client(clientDto)

    if result == 0: 
      return ApiResponse.bad_request("Error to create client.")

    return ApiResponse.created("Created with success.", clientDto)
    