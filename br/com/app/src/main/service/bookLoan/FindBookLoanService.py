from repository.bookLoan.BookLoanRepository import BookLoanRepository
from utils.ApiResponse import ApiResponse

class FindBookLoanService:
  def __init__(self):
    self.book_loan_repository = BookLoanRepository()

  def find_book_loan_by_id(self, id):
    bookLoan = self.book_loan_repository.find_book_loan_by_id(id)

    if bookLoan is None:
      return ApiResponse.not_found("Loan not found.")

    return ApiResponse.ok("", bookLoan)