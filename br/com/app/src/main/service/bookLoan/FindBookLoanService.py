from repository.bookLoan.BookLoanRepository import BookLoanRepository
from utils.ApiResponse import ApiResponse
from domain.exceptions.NotFoundException import NotFoundException

class FindBookLoanService:
  def __init__(self):
    self.book_loan_repository = BookLoanRepository()

  def find_book_loan_by_id(self, id):
    bookLoan = self.book_loan_repository.find_book_loan_by_id(id)

    if bookLoan is None:
      raise NotFoundException()

    return bookLoan