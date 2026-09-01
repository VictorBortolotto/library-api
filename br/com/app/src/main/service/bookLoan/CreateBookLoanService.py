from repository.book.BookRepository import BookRepository
from repository.bookLoan.BookLoanRepository import BookLoanRepository
from utils.ApiResponse import ApiResponse
from domain.dto.bookLoan.BookLoanResponseDto import BookLoanResponseDto

class CreateBookLoanService:
  def __init__(self):
    self.book_repository = BookRepository()
    self.book_loan_repository = BookLoanRepository()

  def create_book_loan(self, bookLoanDto):
    book = self.book_repository.find_book_by_id(bookLoanDto.book_id)

    if book is None:
      return ApiResponse.not_found("Book not found.")

    if book.quantity < bookLoanDto.loan_quantity or book.quantity == 0:
      return ApiResponse.conflict("Insufficient copies available for loan.")

    result = self.book_loan_repository.create_loan(bookLoanDto)

    newBookQuantity = book.quantity - bookLoanDto.loan_quantity

    updateResult = self.book_repository.update_book_quantity(book.id, newBookQuantity)

    if updateResult == 0:
      return ApiResponse.bad_request("Error to update book quantity.")

    bookLoanResposneDto = BookLoanResponseDto(
      result, 
      bookLoanDto.book_id, 
      bookLoanDto.client_id, 
      bookLoanDto.loan_date, 
      bookLoanDto.loan_quantity, 
      bookLoanDto.expeted_return_date
    )

    return ApiResponse.created("Book loan confirmed.", bookLoanResposneDto)

    