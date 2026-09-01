from repository.book.BookRepository import BookRepository
from utils.ApiResponse import ApiResponse

class FindAllBooksService:
  def __init__(self):
    self.book_repository = BookRepository()

  def find_all_books(self):
    books = self.book_repository.find_all_books()

    if books is None or books == []:
      return ApiResponse.not_found("Books not found.")

    return ApiResponse.ok("", books)