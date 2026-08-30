from flask import request
from domain.dto.client.CreateClientDto import CreateClientDto
from domain.dto.client.UpdateClientDto import UpdateClientDto
from service.client.CreateClientService import CreateClientService
from service.client.UpdateClientService import UpdateClientService
from service.client.DeactivateClientService import DeactivateClientService

class ClientController:
  def __init__(self, app):
    self.app = app
    self.create_client_service = CreateClientService()
    self.update_client_service = UpdateClientService()
    self.deactivate_client_service = DeactivateClientService()
    self.default_route = "/client"
    self.register_routes()

  def register_routes(self):

    @self.app.route(self.default_route, methods=['POST'])
    def create_client():
      json = request.get_json()
      client_dto = CreateClientDto(
        json.get("user_id"), 
        json.get("name"),
        json.get("phone"),
        json.get("address"),
        json.get("zip_code"),
        json.get("city"),
        json.get("neighborhood"),
        json.get("country")
      )
      
      return self.create_client_service.create_client(client_dto)

    @self.app.route(self.default_route + "/<id>", methods=['PUT'])
    def update_client(id):
      json = request.get_json()
      client_dto = UpdateClientDto(
        json.get("name"),
        json.get("phone"),
        json.get("address"),
        json.get("zip_code"),
        json.get("city"),
        json.get("neighborhood"),
        json.get("country")
      )
      
      return self.update_client_service.update_client(id, client_dto)

    @self.app.route(self.default_route + "/deactivate/<id>", methods=['PATCH'])
    def deactivate_client(id):
      return self.deactivate_client_service.deactivate_client(id)