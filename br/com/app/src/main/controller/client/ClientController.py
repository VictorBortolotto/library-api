from flask import request
from domain.dto.client.CreateClientDto import CreateClientDto
from domain.dto.client.UpdateClientDto import UpdateClientDto
from service.client.CreateClientService import CreateClientService
from service.client.UpdateClientService import UpdateClientService
from service.client.DeactivateClientService import DeactivateClientService
from flasgger import swag_from
import os
from domain.exceptions.ConflictException import ConflictException
from domain.exceptions.NotFoundException import NotFoundException
from utils.ApiResponse import ApiResponse

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
    @swag_from(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/client/create_client.yaml')))
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

      try:
        client = self.create_client_service.create_client(client_dto)

        return ApiResponse.created(
          "Client created with success.",
          client
        )

      except ConflictException:
        return ApiResponse.conflict(
          "Client already exists with this user."
        )
      
      except Exception:
        return ApiResponse.internal_server_error(
          "Error to create client."
        )

    @self.app.route(self.default_route + "/<id>", methods=['PUT'])
    @swag_from(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/client/update_client.yaml')))
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

      try:
        client = self.update_client_service.update_client(id, client_dto)

        return ApiResponse.ok(
          "Client updated with success.",
          client
        )

      except NotFoundException:
        return ApiResponse.not_found(
          "Client not found."
        )
      
      except Exception:
        return ApiResponse.internal_server_error(
          "Error to update client."
        )

    @self.app.route(self.default_route + "/deactivate/<id>", methods=['PATCH'])
    @swag_from(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/client/deactivate_client.yaml')))
    def deactivate_client(id):
      try:
        self.deactivate_client_service.deactivate_client(id)

        return ApiResponse.ok(
          "Client updated with success."
        )

      except NotFoundException:
        return ApiResponse.not_found(
          "Client not found."
        )
      
      except Exception:
        return ApiResponse.internal_server_error(
          "Error to update client."
        )