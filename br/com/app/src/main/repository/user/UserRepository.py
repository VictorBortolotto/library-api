from database.Database import Database
from datetime import datetime

class UserRepository:
  def __init__(self):
    self.database = Database()
  
  def create_user(self, user):
    result = self.database.insert("insert into user (email,password,creation_date) values (?,?,?)", (
      user.email,
      user.password,
      datetime.now()
    ))

    return result

  def find_user_by_id(self, email):
    result = self.database.find_by_id("select count(*) as is_exists from user where email = ?", (email,))
    return result[0]

  def update_user_is_activate(self, id, deleteDate):
    return self.database.update_by_id("update user set is_active = 0, delete_date = ? where id = ?", (deleteDate,id))