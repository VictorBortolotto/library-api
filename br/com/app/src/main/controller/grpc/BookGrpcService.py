import grpc

from generated import book_pb2
from generated import book_pb2_grpc

from domain.dto.book.BookDto import BookDto
from service.book.CreateBookService import CreateBookService
from domain.exceptions.BookAlreadyExistsException import BookAlreadyExistsException


class BookGrpcService(book_pb2_grpc.BookServiceServicer):

    def __init__(self):
        self.create_book_service = CreateBookService()

    def CreateBook(self, request, context):

        bookDto = BookDto(
            request.title,
            request.description,
            request.quantity
        )

        try:

            book = self.create_book_service.create_book(bookDto)

            return book_pb2.BookResponseDto(
                data=book_pb2.Book(
                    id=book.id,
                    title=book.title,
                    description=book.description,
                    quantity=book.quantity
                ),
                message="Book created with success."
            )

        except BookAlreadyExistsException:

            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("Book already exists.")

            return book_pb2.BookResponseDto()