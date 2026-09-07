from repository.client.ClientRepository import ClientRepository
from domain.exceptions.NotFoundException import NotFoundException
from domain.model.Client import Client

class UpdateClientService:
  def __init__(self):
    self.client_repository = ClientRepository()

  def update_client(self, id, clientDto):
    client = self.client_repository.find_client_by_id(id)

    if client is None:
      raise NotFoundException()

    result = self.client_repository.update_client(id, clientDto)

    if result == 0: 
      raise Exception()

    return Client(
      client.id, 
      client.user_id,
      clientDto.name,
      clientDto.phone,
      clientDto.address,
      clientDto.zip_code,
      clientDto.city,
      clientDto.neighborhood,
      clientDto.country,
      1
    )
    