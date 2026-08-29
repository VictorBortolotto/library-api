from flask import request
from domain.dto.client import CreateClientDto
from service.client.CreateClientService import CreateClientService

class ClientController:
  def __init__(self, app):
    self.app = app
    self.create_client_service = CreateClientService()
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