from repository.client.ClientRepository import ClientRepository
from domain.model.Client import Client
from domain.exceptions.ConflictException import ConflictException

class CreateClientService:
  def __init__(self):
    self.client_repository = ClientRepository()

  def create_client(self, clientDto):
    is_client_exists = self.client_repository.find_client_by_user_id(clientDto.user_id)

    if is_client_exists > 0:
      raise ConflictException()

    result = self.client_repository.create_client(clientDto)

    if result == 0:
      raise Exception()

    return Client(
      result, 
      clientDto.user_id,
      clientDto.name,
      clientDto.phone,
      clientDto.address,
      clientDto.zip_code,
      clientDto.city,
      clientDto.neighborhood,
      clientDto.country,
      1
    )
    