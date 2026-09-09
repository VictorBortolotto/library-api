import grpc

from generated import zip_code_pb2
from generated import zip_code_pb2_grpc

from service.external.ExternalApiService import ExternalApiService
from domain.exceptions.ConflictException import ConflictException
from domain.exceptions.NotFoundException import NotFoundException


class ZipCodeGrpcService(zip_code_pb2_grpc.ZipCodeServiceServicer):

  def __init__(self):
    self.external_api_service = ExternalApiService()

  def FindDataByZipCode(self, request, context):
    try:
      zip_code_data = self.external_api_service.find_by_cep(request.zip_code)


      book_loan_response = zip_code_pb2.ZipCodeData(
        address=zip_code_data.logradouro,
        zip_code=zip_code_data.cep,
        city=zip_code_data.localidade,
        neighborhood=zip_code_data.bairro
      )

      return zip_code_pb2.ZipCodeResponse(
        data=book_loan_response,
        message=""
      )
    
    except NotFoundException:

      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details("Data not found.")

      return zip_code_pb2.ZipCodeResponse()