from concurrent import futures
import grpc

from generated import book_pb2_grpc
from generated import user_pb2_grpc
from generated import client_pb2_grpc
from generated import book_loan_pb2_grpc
from generated import zip_code_pb2_grpc
from controller.grpc.BookGrpcService import BookGrpcService
from controller.grpc.UserGrpcService import UserGrpcService
from controller.grpc.ClientGrpcService import ClientGrpcService
from controller.grpc.BookLoanGrpcService import BookLoanGrpcService
from controller.grpc.ZipCodeGrpcService import ZipCodeGrpcService

def serve():

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    book_pb2_grpc.add_BookServiceServicer_to_server(
        BookGrpcService(),
        server
    )

    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserGrpcService(),
        server
    )

    client_pb2_grpc.add_ClientServiceServicer_to_server(
        ClientGrpcService(),
        server
    )

    book_loan_pb2_grpc.add_BookLoanServiceServicer_to_server(
        BookLoanGrpcService(),
        server
    )

    zip_code_pb2_grpc.add_ZipCodeServiceServicer_to_server(
        ZipCodeGrpcService(),
        server
    )

    port = server.add_insecure_port("[::]:50051")

    print("Porta configurada:", port)

    server.start()

    print("Servidor gRPC iniciado em localhost:50051")

    return server


if __name__ == "__main__":
    server = serve()
    server.wait_for_termination()