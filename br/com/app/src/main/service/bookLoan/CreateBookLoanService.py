from repository.book.BookRepository import BookRepository
from repository.bookLoan.BookLoanRepository import BookLoanRepository
from utils.ApiResponse import ApiResponse
from domain.dto.bookLoan.BookLoanResponseDto import BookLoanResponseDto

from domain.exceptions.NotFoundException import NotFoundException
from domain.exceptions.InsufficientQuantityException import InsufficientQuantityException

class CreateBookLoanService:
  def __init__(self):
    self.book_repository = BookRepository()
    self.book_loan_repository = BookLoanRepository()

  def create_book_loan(self, bookLoanDto):
    book = self.book_repository.find_book_by_id(bookLoanDto.book_id)

    if book is None:
      raise NotFoundException()

    if book.quantity < bookLoanDto.loan_quantity or book.quantity == 0:
      raise InsufficientQuantityException()

    result = self.book_loan_repository.create_loan(bookLoanDto)

    newBookQuantity = book.quantity - bookLoanDto.loan_quantity

    updateResult = self.book_repository.update_book_quantity(book.id, newBookQuantity)

    if updateResult == 0:
      raise Exception()

    return BookLoanResponseDto(
      result, 
      bookLoanDto.book_id, 
      bookLoanDto.client_id, 
      bookLoanDto.loan_date, 
      bookLoanDto.loan_quantity, 
      bookLoanDto.expeted_return_date
    )


    