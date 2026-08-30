from flask import request
from domain.dto.book.BookDto import BookDto
from service.book.CreateBookService import CreateBookService
from service.book.UpdateBookService import UpdateBookService
from service.book.DeleteBookService import DeleteBookService
from service.book.FindAllBooksService import FindAllBooksService
from service.book.FindBookByIdService import FindBookByIdService

class BookController:
  def __init__(self, app):
    self.app = app
    self.create_book_service = CreateBookService()
    self.update_book_service = UpdateBookService()
    self.delete_book_service = DeleteBookService()
    self.find_book_by_id_service = FindBookByIdService()
    self.find_all_books_service = FindAllBooksService()
    self.default_route = "/book"
    self.register_routes()

  
  def register_routes(self):

    @self.app.route(self.default_route, methods=['POST'])
    def create_book():
      json = request.get_json()

      bookDto = BookDto(json.get("title"),json.get("description"),json.get("quantity"))

      return self.create_book_service.create_book(bookDto)

    @self.app.route(self.default_route + "/<id>", methods=['PUT'])
    def update_book(id):
      json = request.get_json()

      bookDto = BookDto(json.get("title"),json.get("description"),json.get("quantity"))

      return self.update_book_service.update_book(id, bookDto)
    
    @self.app.route(self.default_route + "/<id>", methods=['GET'])
    def find_book_by_id(id):
      return self.find_book_by_id_service.find_book_by_id(id)
    
    @self.app.route(self.default_route, methods=['GET'])
    def find_all_books():
      return self.find_all_books_service.find_all_books()

    @self.app.route(self.default_route + "/<id>", methods=['DELETE'])
    def delete_book(id):
      return self.delete_book_service.delete_book(id)