from repository.book.BookRepository import BookRepository
from domain.exceptions.NotFoundException import NotFoundException

class FindAllBooksService:
  def __init__(self):
    self.book_repository = BookRepository()

  def find_all_books(self):
    books = self.book_repository.find_all_books()

    if books is None or books == []:
      raise NotFoundException()

    return books