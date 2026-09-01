from flask import request
from domain.dto.bookLoan.CreateBookLoanDto import CreateBookLoanDto
from domain.dto.bookLoan.UpdateBookLoanRequest import UpdateBookLoanRequest
from service.bookLoan.CreateBookLoanService import CreateBookLoanService
from service.bookLoan.UpdateBookLoanService import UpdateBookLoanService
from service.bookLoan.FindAllBookLoanService import FindAllBookLoanService
from service.bookLoan.FindBookLoanService import FindBookLoanService

class BookLoanController:
  def __init__(self, app):
    self.app = app
    self.create_book_loan_service = CreateBookLoanService()
    self.update_book_loan_service = UpdateBookLoanService()
    self.find_book_loan_by_id_service = FindBookLoanService()
    self.find_all_book_loan_service = FindAllBookLoanService()
    self.default_route = "/loan"
    self.register_routes()

  def register_routes(self):
  
    @self.app.route(self.default_route, methods=['POST'])
    def create_book_loan():
      json = request.get_json()

      bookLoanDto = CreateBookLoanDto(
        json.get("book_id"),
        json.get("client_id"),
        json.get("loan_date"),
        json.get("loan_quantity"),
        json.get("expeted_return_date"),
      )

      return self.create_book_loan_service.create_book_loan(bookLoanDto)

    @self.app.route(self.default_route + "/<id>", methods=['PUT'])
    def update_book_loan(id):
      json = request.get_json()

      updateBookLoanDto = UpdateBookLoanRequest(
        json.get("book_id"),
        json.get("return_date"),
        json.get("is_book_already_returned"),
        json.get("returned_quantity"),
      )

      return self.update_book_loan_service.update_book_loan_service(id, updateBookLoanDto)

    @self.app.route(self.default_route + "/<id>", methods=['GET'])
    def find_book_loan_by_id(id):
      return self.find_book_loan_by_id_service.find_book_loan_by_id(id)
    
    @self.app.route(self.default_route + "/all/<idClient>", methods=['GET'])
    def find_all_book_loan(idClient):
      return self.find_all_book_loan_service.find_all_book_loan_service(idClient)