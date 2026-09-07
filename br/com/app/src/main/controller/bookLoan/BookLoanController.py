from flask import request
from domain.dto.bookLoan.CreateBookLoanDto import CreateBookLoanDto
from domain.dto.bookLoan.UpdateBookLoanRequest import UpdateBookLoanRequest
from service.bookLoan.CreateBookLoanService import CreateBookLoanService
from service.bookLoan.UpdateBookLoanService import UpdateBookLoanService
from service.bookLoan.FindAllBookLoanService import FindAllBookLoanService
from service.bookLoan.FindBookLoanService import FindBookLoanService

from utils.ApiResponse import ApiResponse

from domain.exceptions.ConflictException import ConflictException
from domain.exceptions.NotFoundException import NotFoundException
from domain.exceptions.InsufficientQuantityException import InsufficientQuantityException

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

      book_loan_dto = CreateBookLoanDto(
        json.get("book_id"),
        json.get("client_id"),
        json.get("loan_date"),
        json.get("loan_quantity"),
        json.get("expeted_return_date"),
      )

      try:
        book = self.create_book_loan_service.create_book_loan(book_loan_dto)

        return ApiResponse.created(
          "Book loan with success.",
          book
        )

      except NotFoundException:
        return ApiResponse.not_found(
          "Book not found."
        )
      
      except InsufficientQuantityException:
        return ApiResponse.conflict(
          "Insufficient copies available for loan."
        )
      
      except Exception:
        return ApiResponse.conflict(
          "Error to update book quantity."
        )

    @self.app.route(self.default_route + "/<id>", methods=['PUT'])
    def update_book_loan(id):
      json = request.get_json()

      update_book_loan_dto = UpdateBookLoanRequest(
        json.get("book_id"),
        json.get("return_date"),
        json.get("is_book_already_returned"),
        json.get("returned_quantity"),
      )

      try:
        self.update_book_loan_service.update_book_loan_service(id, update_book_loan_dto)

        return ApiResponse.ok(
          "Book returned successfully."
        )
      
      except NotFoundException:
        return ApiResponse.not_found(
          "Book or loan not found."
        )
      
      except ConflictException:
        return ApiResponse.conflict(
          "The quantity of returned books is greater than the quantity of rented books."
        )
      
      except Exception:
        return ApiResponse.internal_server_error(
          "Error to update book loan data."
        )

    @self.app.route(self.default_route + "/<id>", methods=['GET'])
    def find_book_loan_by_id(id):
      try:
        book_loan = self.find_book_loan_by_id_service.find_book_loan_by_id(id)

        return ApiResponse.ok(
          "",
          book_loan
        )
      except NotFoundException:
        return ApiResponse.not_found(
          "Book or loan not found."
        )
      
    @self.app.route(self.default_route + "/all/<idClient>", methods=['GET'])
    def find_all_book_loan(idClient):
      try:
        book_loan_list = self.find_all_book_loan_service.find_all_book_loan_service(idClient)

        return ApiResponse.ok(
          "",
          book_loan_list
        )
      except NotFoundException:
        return ApiResponse.not_found(
          "Books loan not found."
        )