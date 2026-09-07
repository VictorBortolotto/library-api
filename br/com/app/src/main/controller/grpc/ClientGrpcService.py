import grpc

from generated import client_pb2
from generated import client_pb2_grpc

from service.client.CreateClientService import CreateClientService
from service.client.UpdateClientService import UpdateClientService
from service.client.DeactivateClientService import DeactivateClientService

from domain.dto.client.CreateClientDto import CreateClientDto
from domain.dto.client.UpdateClientDto import UpdateClientDto

from domain.exceptions.NotFoundException import NotFoundException
from domain.exceptions.ConflictException import ConflictException


class ClientGrpcService(client_pb2_grpc.ClientServiceServicer):

  def __init__(self):
    self.create_client_service = CreateClientService()
    self.update_client_service = UpdateClientService()
    self.deactivate_client_service = DeactivateClientService()

  def CreateClient(self, request, context):
    clientDto = CreateClientDto(
      request.user_id,
      request.name,
      request.phone,
      request.address,
      request.zip_code,
      request.city,
      request.neighborhood,
      request.country,
    )

    try:

      client = self.create_client_service.create_client(clientDto)

      return client_pb2.ClientResponse(
        data=client_pb2.Client(
          id=client.id,
          user_id=client.user_id,
          name=client.name,
          phone=client.phone,
          address=client.address,
          zip_code=client.zip_code,
          city=client.city,
          neighborhood=client.neighborhood,
          country=client.country,
          is_active=client.is_active
        ),
        message="Client created with success."
      )

    except ConflictException:

      context.set_code(grpc.StatusCode.ALREADY_EXISTS)
      context.set_details("Client already exists with this user.")

      return client_pb2.ClientResponse()

    except Exception:

      context.set_code(grpc.StatusCode.INTERNAL)
      context.set_details("Error to create client.")

      return client_pb2.ClientResponse()
    
  def UpdateClient(self, request, context):
    
    clientDto = UpdateClientDto(
      request.client.name,
      request.client.phone,
      request.client.address,
      request.client.zip_code,
      request.client.city,
      request.client.neighborhood,
      request.client.country,
    )

    try:

      client = self.update_client_service.update_client(request.id, clientDto)

      return client_pb2.ClientResponse(
        data=client_pb2.Client(
          id=client.id,
          user_id=client.user_id,
          name=client.name,
          phone=client.phone,
          address=client.address,
          zip_code=client.zip_code,
          city=client.city,
          neighborhood=client.neighborhood,
          country=client.country
        ),
        message="Client updated with success."
      )

    except NotFoundException:

      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details("Client not found.")

      return client_pb2.ClientResponse()
    
    except Exception:

      context.set_code(grpc.StatusCode.INTERNAL)
      context.set_details("Error to update client.")

      return client_pb2.ClientResponse()

  def DeactivateClient(self, request, context):
    try:

      self.deactivate_client_service.deactivate_client(request.id)

      return client_pb2.GenericResponse(
        message="Client deactivated with success."
      )

    except NotFoundException:

      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details("Client not found.")

      return client_pb2.GenericResponse()
    
    except Exception:

      context.set_code(grpc.StatusCode.INTERNAL)
      context.set_details("Error to deactivate client.")

      return client_pb2.GenericResponse()