from database.Database import Database
from datetime import datetime
from utils.HashUtils import HashUtils
from domain.dto.user.UserDto import UserDto

class UserRepository:
  def __init__(self):
    self.database = Database()
    self.hash_utils = HashUtils()
  
  def create_user(self, user):
    passwordHash = self.hash_utils.gen_hash(user.password)
    result = self.database.insert("insert into user (email,password,creation_date) values (?,?,?)", (
      user.email,
      passwordHash,
      datetime.now()
    ))

    return result

  def find_user_by_email(self, email):
    result = self.database.find_by_id("select count(*) as is_exists from user where email = ?", (email,))
    return result[0]

  def find_user_by_id(self, id):
    result = self.database.find_by_id("select email, password from user where email = ?", (id,))

    if result is None:
      return result

    email,password=result
    return UserDto(email,password)

  def update_user_is_activate(self, id, deleteDate):
    return self.database.update_by_id("update user set is_active = 0, delete_date = ? where id = ?", (deleteDate,id))