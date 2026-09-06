from repository.book.BookRepository import BookRepository
from domain.exceptions.NotFoundException import NotFoundException

class DeleteBookService:
  def __init__(self):
    self.book_repository = BookRepository()

  def delete_book(self, id):
    book = self.book_repository.find_book_by_id(id)

    if book is None:
      raise NotFoundException()
    
    result = self.book_repository.delete_book(id)

    if result == 0:
      raise Exception()

    return result
