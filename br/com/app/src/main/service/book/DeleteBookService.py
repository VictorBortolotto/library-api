from repository.book.BookRepository import BookRepository
from utils.ApiResponse import ApiResponse
from domain.model.Book import Book

class DeleteBookService:
  def __init__(self):
    self.book_repository = BookRepository()

  def delete_book(self, id):
    book = self.book_repository.find_book_by_id(id)

    if book is None:
      return ApiResponse.not_found("Book not found.")
    
    result = self.book_repository.delete_book(id)

    if result == 0:
      return ApiResponse.bad_request("Error to delete book.")

    return ApiResponse.ok("Book deleted with success.")
