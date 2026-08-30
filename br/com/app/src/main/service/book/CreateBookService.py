from repository.book.BookRepository import BookRepository
from utils.ApiResponse import ApiResponse
from domain.model.Book import Book

class CreateBookService:
  def __init__(self):
    self.book_repository = BookRepository()

  def create_book(self, bookDto):
    book_exists = self.book_repository.find_book_by_title(bookDto.title)

    if book_exists > 0:
      return ApiResponse.conflict("Book already exists.")

    result = self.book_repository.create_book(bookDto)

    bookResponse = Book(result,bookDto.title,bookDto.description,bookDto.quantity)

    return ApiResponse.created("Book created with success.", bookResponse)