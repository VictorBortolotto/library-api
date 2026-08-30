from repository.book.BookRepository import BookRepository
from utils.ApiResponse import ApiResponse
from domain.model.Book import Book

class FindBookByIdService:
  def __init__(self):
    self.book_repository = BookRepository()

  def find_book_by_id(self, id):
    book = self.book_repository.find_book_by_id(id)

    if book is None:
      return ApiResponse.not_found("Book not found.")

    return ApiResponse.ok("", book)