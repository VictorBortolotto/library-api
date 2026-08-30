from repository.book.BookRepository import BookRepository
from utils.ApiResponse import ApiResponse
from domain.model.Book import Book

class UpdateBookService:
  def __init__(self):
    self.book_repository = BookRepository()

  def update_book(self, id, bookDto):
    book = self.book_repository.find_book_by_id(id)

    if book is None:
      return ApiResponse.not_found("Book not found.")

    result = self.book_repository.update_book(id, bookDto)

    if result == 0:
      return ApiResponse.bad_request("Error to update book.")

    bookResponse = Book(book.id,bookDto.title,bookDto.description,bookDto.quantity)

    return ApiResponse.ok("Book updated with success.", bookResponse)