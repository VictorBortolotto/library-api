from repository.book.BookRepository import BookRepository
from domain.exceptions.BookAlreadyExistsException import BookAlreadyExistsException
from domain.model.Book import Book

class CreateBookService:
  def __init__(self):
    self.book_repository = BookRepository()

  def create_book(self, bookDto):

    book_exists = self.book_repository.find_book_by_title(bookDto.title)

    if book_exists > 0:
      raise BookAlreadyExistsException()

    result = self.book_repository.create_book(bookDto)

    return Book(
      result,
      bookDto.title,
      bookDto.description,
      bookDto.quantity
    )