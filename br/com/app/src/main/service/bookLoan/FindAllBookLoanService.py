from repository.bookLoan.BookLoanRepository import BookLoanRepository
from utils.ApiResponse import ApiResponse

class FindAllBookLoanService:
  def __init__(self):
    self.book_loan_repository = BookLoanRepository()

  def find_all_book_loan_service(self, idClient):
    booksLoan = self.book_loan_repository.find_all_book_loan_by_id_client(idClient)

    if booksLoan is None:
      return ApiResponse.not_found("Loan not found.")

    return ApiResponse.ok("", booksLoan)