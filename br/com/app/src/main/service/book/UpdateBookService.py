from repository.book.BookRepository import BookRepository
from domain.exceptions.NotFoundException import NotFoundException
from domain.model.Book import Book

class UpdateBookService:
  def __init__(self):
    self.book_repository = BookRepository()

  def update_book(self, id, bookDto):
    book = self.book_repository.find_book_by_id(id)

    if book is None:
      raise NotFoundException()

    result = self.book_repository.update_book(id, bookDto)

    if result == 0:
      return Exception()

    return  Book(book.id,bookDto.title,bookDto.description,bookDto.quantity)