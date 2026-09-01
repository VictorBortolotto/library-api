from database.Database import Database
from domain.model.Book import Book

class BookRepository:
  def __init__(self):
    self.database = Database()

  def create_book(self, bookDto):
    result = self.database.insert("insert into book (title, description, quantity) values (?,?,?)", (
      bookDto.title,
      bookDto.description,
      bookDto.quantity
    ))

    return result

  def update_book(self, id, bookDto):
    result = self.database.update_by_id("update book set title = ?, description = ?, quantity = ? where id = ?", (
      bookDto.title,
      bookDto.description,
      bookDto.quantity,
      id
    ))

    return result

  def find_book_by_id(self, id):
    result = self.database.find_by_id("select id, title, description, quantity from book where id = ?", (id,))

    if result is None:
      return result

    id,title,description,quantity = result

    return Book(id,title,description,quantity)
  
  def find_book_by_title(self, title):
    result = self.database.find_by_id("select count(title) from book where id = ?", (title,))

    return result[0]

  def find_all_books(self):
    results = self.database.find_all_by("select id, title, description, quantity from book", ())

    if results is None:
      return results

    book_list = []
    for result in results:
      id,title,description,quantity = result
      book_list.append(Book(id,title,description,quantity))

    return book_list

  def delete_book(self, id):
    result = self.database.delete_by_id("delete from book where id = ?", (id,))

    return result

  def update_book_quantity(self,id,newQuantity):
    result = self.database.update_by_id("update book set quantity = ? where id = ?", (
      newQuantity,
      id
    ))

    return result