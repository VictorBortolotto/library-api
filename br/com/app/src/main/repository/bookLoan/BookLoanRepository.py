from database.Database import Database
from domain.model.BookLoan import BookLoan
from datetime import datetime

class BookLoanRepository:
  def __init__(self):
    self.database = Database()

  def create_loan(self, createBookLoanDto):
    result = self.database.insert("insert into book_loan (book_id, client_id, loan_date, expeted_return_date, loan_quantity) values (?,?,?,?,?)", (
      createBookLoanDto.book_id,
      createBookLoanDto.client_id,
      createBookLoanDto.loan_date,
      createBookLoanDto.expeted_return_date,
      createBookLoanDto.loan_quantity
    ))

    return result

  def find_book_loan_by_id(self, id):
    result = self.database.find_by_id("select id, book_id, client_id, loan_date, expeted_return_date, return_date, returned_quantity, loan_quantity, is_book_already_returned from book_loan where id = ?",(id,))

    if result is None:
      return result

    id, book_id, client_id, loan_date, expeted_return_date, return_date, returned_quantity, loan_quantity, is_book_already_returned = result

    return BookLoan(id, book_id, client_id, loan_date, expeted_return_date, return_date, returned_quantity, loan_quantity, is_book_already_returned)
  
  def find_all_book_loan_by_id_client(self, idClient):
    results = self.database.find_all_by("select id, book_id, client_id, loan_date, expeted_return_date, return_date, returned_quantity, loan_quantity, is_book_already_returned from book_loan where client_id = ?",(idClient,))

    if results is None:
      return results

    book_loan_list = []
    for result in results:
      id, book_id, client_id, loan_date, expeted_return_date, return_date, returned_quantity, loan_quantity, is_book_already_returned = result
      book_loan_list.append(BookLoan(id, book_id, client_id, loan_date, expeted_return_date, return_date, returned_quantity, loan_quantity, is_book_already_returned))

    return book_loan_list

  def update_return_date(self,id,updateBookLoanDto):
    result = self.database.update_by_id("update book_loan set return_date = ?, is_book_already_returned = ?, returned_quantity = ? where id = ?", (
      updateBookLoanDto.return_date,
      updateBookLoanDto.is_book_already_returned,
      updateBookLoanDto.returned_quantity,
      id
    ))

    return result
    