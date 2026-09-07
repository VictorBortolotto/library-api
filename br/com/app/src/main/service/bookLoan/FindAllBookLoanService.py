from repository.bookLoan.BookLoanRepository import BookLoanRepository
from domain.exceptions.NotFoundException import NotFoundException

class FindAllBookLoanService:
  def __init__(self):
    self.book_loan_repository = BookLoanRepository()

  def find_all_book_loan_service(self, idClient):
    booksLoan = self.book_loan_repository.find_all_book_loan_by_id_client(idClient)

    if booksLoan is None:
      raise NotFoundException()

    return booksLoan