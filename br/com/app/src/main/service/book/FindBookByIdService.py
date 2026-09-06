from repository.book.BookRepository import BookRepository
from domain.exceptions.NotFoundException import NotFoundException

class FindBookByIdService:
  def __init__(self):
    self.book_repository = BookRepository()

  def find_book_by_id(self, id):
    book = self.book_repository.find_book_by_id(id)

    if book is None:
      raise NotFoundException()

    return book