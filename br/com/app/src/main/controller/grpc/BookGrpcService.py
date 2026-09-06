import grpc

from generated import book_pb2
from generated import book_pb2_grpc

from domain.dto.book.BookDto import BookDto
from service.book.CreateBookService import CreateBookService
from service.book.UpdateBookService import UpdateBookService
from service.book.FindAllBooksService import FindAllBooksService
from service.book.FindBookByIdService import FindBookByIdService
from service.book.DeleteBookService import DeleteBookService
from domain.exceptions.ConflictException import ConflictException
from domain.exceptions.NotFoundException import NotFoundException


class BookGrpcService(book_pb2_grpc.BookServiceServicer):

    def __init__(self):
        self.create_book_service = CreateBookService()
        self.update_book_service = UpdateBookService()
        self.find_all_book_service = FindAllBooksService()
        self.find_book_by_id_service = FindBookByIdService()
        self.delete_book_service = DeleteBookService()

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

        except ConflictException:

            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("Book already exists.")

            return book_pb2.BookResponseDto()

    def UpdateBook(self, request, context):

        bookDto = BookDto(
            request.book.title,
            request.book.description,
            request.book.quantity
        )
        
        try:

            book = self.update_book_service.update_book(request.id, bookDto)

            return book_pb2.BookResponseDto(
                data=book_pb2.Book(
                    id=book.id,
                    title=book.title,
                    description=book.description,
                    quantity=book.quantity
                ),
                message="Book updated with success."
            )

        except NotFoundException:

            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Book not found.")

            return book_pb2.BookResponseDto()

        except Exception:

            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Error to update book.")

            return book_pb2.BookResponseDto()

    def FindAllBook(self, request, context):
        try:

            books = self.find_all_book_service.find_all_books()

            books_proto = [
                book_pb2.Book(
                    id=book.id,
                    title=book.title,
                    description=book.description,
                    quantity=book.quantity
                )
                for book in books
            ]

            return book_pb2.BookListResponse(
                data=books_proto,
                message=""
            )

        except NotFoundException:

            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Books not found.")

            return book_pb2.BookListResponse()

    def FindBookById(self, request, context):
        try:

            book = self.find_book_by_id_service.find_book_by_id(request.id)

            return book_pb2.BookResponseDto(
                data=book_pb2.Book(
                    id=book.id,
                    title=book.title,
                    description=book.description,
                    quantity=book.quantity
                ),
                message=""
            )

        except NotFoundException:

            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Book not found.")

            return book_pb2.BookResponseDto()
        
    def DeleteBook(self, request, context):
        try:

            self.delete_book_service.delete_book(request.id)

            return book_pb2.BookDeleteResponse(
                message="Book deleted with success."
            )

        except NotFoundException:

            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Book not found.")

            return book_pb2.BookDeleteResponse()
        
        except Exception:

            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Error to delete book.")

            return book_pb2.BookDeleteResponse()