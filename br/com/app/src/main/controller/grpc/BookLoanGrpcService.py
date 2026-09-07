import grpc

from generated import book_loan_pb2
from generated import book_loan_pb2_grpc

from domain.dto.bookLoan.CreateBookLoanDto import CreateBookLoanDto
from domain.dto.bookLoan.UpdateBookLoanRequest import UpdateBookLoanRequest

from service.bookLoan.CreateBookLoanService import CreateBookLoanService
from service.bookLoan.UpdateBookLoanService import UpdateBookLoanService
from service.bookLoan.FindAllBookLoanService import FindAllBookLoanService
from service.bookLoan.FindBookLoanService import FindBookLoanService

from domain.exceptions.ConflictException import ConflictException
from domain.exceptions.NotFoundException import NotFoundException
from domain.exceptions.InsufficientQuantityException import InsufficientQuantityException

class BookLoanGrpcService(book_loan_pb2_grpc.BookLoanServiceServicer):

  def __init__(self):
    self.create_book_loan_service = CreateBookLoanService()
    self.update_book_loan_service = UpdateBookLoanService()
    self.find_all_book_loan_service = FindAllBookLoanService()
    self.find_book_loan_by_id_service = FindBookLoanService()

  def CreateBookLoan(self, request, context):

    bookLoanDto = CreateBookLoanDto(
      request.book_id,
      request.client_id,
      request.loan_date,
      request.loan_quantity,
      request.expeted_return_date
    )

    try:

      bookLoanResponseDto = self.create_book_loan_service.create_book_loan(bookLoanDto)

      return book_loan_pb2.BookLoanCreateResponse(
        data=book_loan_pb2.BookLoanCreateData(
          id=bookLoanResponseDto.id,
          book_id=bookLoanResponseDto.book_id,
          client_id=bookLoanResponseDto.client_id,
          loan_date=bookLoanResponseDto.loan_date,
          loan_quantity=bookLoanResponseDto.loan_quantity,
          expeted_return_date=bookLoanResponseDto.expeted_return_date
        ),
        message="Book loan confirmed."
      )
    
    except NotFoundException:

      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details("Book not found.")

      return book_loan_pb2.BookLoanCreateResponse()
    
    except InsufficientQuantityException:

      context.set_code(grpc.StatusCode.OUT_OF_RANGE)
      context.set_details("Insufficient copies available for loan.")

      return book_loan_pb2.BookLoanCreateResponse()
    
    except Exception:

      context.set_code(grpc.StatusCode.INTERNAL)
      context.set_details("Error to update book quantity.")

      return book_loan_pb2.BookLoanCreateResponse()

  def UpdateBookLoan(self, request, context):

    bookLoanUpdateRequest = UpdateBookLoanRequest(
      book_id=request.data.book_id,
      return_date=request.data.return_date,
      is_book_already_returned=request.data.is_book_already_returned,
      returned_quantity=request.data.returned_quantity
    )

    try:

      self.update_book_loan_service.update_book_loan_service(request.id, bookLoanUpdateRequest)

      return book_loan_pb2.GenericResponse(
        message="Book returned successfully."
      )

    except NotFoundException:

      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details("Book or loan not found.")

      return book_loan_pb2.GenericResponse()

    except ConflictException:

      context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
      context.set_details("The quantity of returned books is greater than the quantity of rented books.")

      return book_loan_pb2.GenericResponse()

    except Exception:

      context.set_code(grpc.StatusCode.INTERNAL)
      context.set_details("Error to update book loan data.")

      return book_loan_pb2.GenericResponse()

  def FindAllBookLoan(self, request, context):
    try:

      book_loan_list = self.find_all_book_loan_service.find_all_book_loan_service(request.id)

      books_loan_list_proto = [
        book_loan_pb2.BookLoan(
          id = book_loan.id,
          book_id = book_loan.book_id,
          client_id = book_loan.client_id,
          loan_date = book_loan.loan_date,
          expeted_return_date = book_loan.expeted_return_date,
          return_date = book_loan.return_date,
          returned_quantity = book_loan.returned_quantity,
          loan_quantity = book_loan.loan_quantity,
          is_book_already_returned = book_loan.is_book_already_returned,
        )
        for book_loan in book_loan_list
      ]

      return book_loan_pb2.BookLoanListResponse(
        data=books_loan_list_proto,
        message=""
      )
    
    except NotFoundException:

      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details("Loans not found.")

      return book_loan_pb2.BookResponseDto()

  def FindBookLoanById(self, request, context):
    try:

      book_loan = self.find_book_loan_by_id_service.find_book_loan_by_id(request.id)

      book_loan_response = book_loan_pb2.BookLoan(
          id = book_loan.id,
          book_id = book_loan.book_id,
          client_id = book_loan.client_id,
          loan_date = book_loan.loan_date,
          expeted_return_date = book_loan.expeted_return_date,
          return_date = book_loan.return_date,
          returned_quantity = book_loan.returned_quantity,
          loan_quantity = book_loan.loan_quantity,
          is_book_already_returned = book_loan.is_book_already_returned,
        )

      return book_loan_pb2.BookLoanResponse(
        data=book_loan_response,
        message=""
      )
    
    except NotFoundException:

      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details("Loan not found.")

      return book_loan_pb2.BookResponseDto()

    