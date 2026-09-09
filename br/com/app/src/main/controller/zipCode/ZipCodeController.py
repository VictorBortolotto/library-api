from service.external.ExternalApiService import ExternalApiService
from utils.ApiResponse import ApiResponse

class ZipCodeController:
  def __init__(self, app):
    self.app = app
    self.external_api_service = ExternalApiService()
    self.default_route = "/zip_code"
    self.register_routes()

  def register_routes(self):

    @self.app.route(self.default_route + "/<cep>", methods=['GET'])
    def get_zip_code_data_service(cep):
      zipCodeData = self.external_api_service.find_by_cep(cep)

      return ApiResponse.ok(
        "",
        zipCodeData
      )

