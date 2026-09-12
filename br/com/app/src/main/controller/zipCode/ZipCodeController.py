from service.external.ExternalApiService import ExternalApiService
from flasgger import swag_from
import os
from utils.ApiResponse import ApiResponse
from domain.exceptions.NotFoundException import NotFoundException

class ZipCodeController:
  def __init__(self, app):
    self.app = app
    self.external_api_service = ExternalApiService()
    self.default_route = "/zip_code"
    self.register_routes()

  def register_routes(self):

    @self.app.route(self.default_route + "/<cep>", methods=['GET'])
    @swag_from(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/zipCode/zip_code.yaml')))
    def get_zip_code_data_service(cep):
      try:
        zipCodeData = self.external_api_service.find_by_cep(cep)

        return ApiResponse.ok(
          "",
          zipCodeData
        )
      except NotFoundException:
        return ApiResponse.not_found(
          "Zip code data not found."
        )

