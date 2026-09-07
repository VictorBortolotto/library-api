from repository.book.BookRepository import BookRepository
from repository.bookLoan.BookLoanRepository import BookLoanRepository
from domain.exceptions.NotFoundException import NotFoundException
from domain.exceptions.ConflictException import ConflictException

class UpdateBookLoanService:
  def __init__(self):
    self.book_repository = BookRepository()
    self.book_loan_repository = BookLoanRepository()

  def update_book_loan_service(self,id,updateBookLoanRequest):
    book = self.book_repository.find_book_by_id(updateBookLoanRequest.book_id)
    bookLoan = self.book_loan_repository.find_book_loan_by_id(id)

    if book is None or bookLoan is None:
      raise NotFoundException()

    returned_quantity = bookLoan.loan_quantity - updateBookLoanRequest.returned_quantity
    if returned_quantity > 0 and updateBookLoanRequest.is_book_already_returned:
      updateBookLoanRequest.is_book_already_returned = False

    if bookLoan.loan_quantity > bookLoan.returned_quantity and updateBookLoanRequest.returned_quantity < bookLoan.loan_quantity and updateBookLoanRequest.returned_quantity > 0:
      updateBookLoanRequest.returned_quantity = bookLoan.returned_quantity + updateBookLoanRequest.returned_quantity

    if bookLoan.loan_quantity < updateBookLoanRequest.returned_quantity:
      raise ConflictException()

    if bookLoan.loan_quantity != bookLoan.returned_quantity:
      newQuantity = book.quantity + updateBookLoanRequest.returned_quantity

    self.book_repository.update_book_quantity(id, newQuantity)
    result = self.book_loan_repository.update_return_date(id,updateBookLoanRequest)

    if result == 0: 
      raise Exception()

    return result