from repository.book.BookRepository import BookRepository
from repository.bookLoan.BookLoanRepository import BookLoanRepository
from utils.ApiResponse import ApiResponse

class UpdateBookLoanService:
  def __init__(self):
    self.book_repository = BookRepository()
    self.book_loan_repository = BookLoanRepository()

  def update_book_loan_service(self,id,updateBookLoanRequest):
    book = self.book_repository.find_book_by_id(updateBookLoanRequest.book_id)

    if book is None:
      return ApiResponse.not_found("Book not found.")

    bookLoan = self.book_loan_repository.find_book_loan_by_id(id)

    if bookLoan is None:
      return ApiResponse.not_found("Loan not found.")

    returned_quantity = bookLoan.loan_quantity - updateBookLoanRequest.returned_quantity
    if returned_quantity > 0 and updateBookLoanRequest.is_book_already_returned:
      updateBookLoanRequest.is_book_already_returned = False

    if bookLoan.loan_quantity > bookLoan.returned_quantity and updateBookLoanRequest.returned_quantity < bookLoan.loan_quantity and updateBookLoanRequest.returned_quantity > 0:
      updateBookLoanRequest.returned_quantity = bookLoan.returned_quantity + updateBookLoanRequest.returned_quantity

    if bookLoan.loan_quantity < updateBookLoanRequest.returned_quantity:
      return ApiResponse.conflict("The quantity of returned books is greater than the quantity of rented books.")

    if bookLoan.loan_quantity != bookLoan.returned_quantity:
      newQuantity = book.quantity + updateBookLoanRequest.returned_quantity

    self.book_repository.update_book_quantity(id, newQuantity)
    result = self.book_loan_repository.update_return_date(id,updateBookLoanRequest)

    if result == 0: 
      return ApiResponse.bad_request("Error to update book loan data.")

    return ApiResponse.ok("Book returned successfully.")