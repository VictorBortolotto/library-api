from database.Database import Database
from domain.model.Client import Client

class ClientRepository:
  def __init__(self):
    self.database = Database()

  def find_client_by_id(self, id):
    result = self.database.find_by_id("select id,user_id,name,phone,address,zip_code,city,neighborhood,country,is_active from client where id = ?", (id,))

    if result is None:
      return result

    id,user_id,name,phone,address,zip_code,city,neighborhood,country,is_active = result

    return Client(id,user_id,name,phone,address,zip_code,city,neighborhood,country,is_active)

  def create_client(self, client):
    result = self.database.insert("insert into client (user_id,name,phone,address,zip_code,city,neighborhood,country,is_active) values (?,?,?,?,?,?,?,?,?)", (
      client.user_id,
      client.name,
      client.phone,
      client.address,
      client.zip_code,
      client.city,
      client.neighborhood,
      client.country,
      1
    ))

    return result
  
  def update_client(self, id, client):
    result = self.database.update_by_id("update client set name = ?, phone = ?, address = ?, zip_code = ?,city = ?, neighborhood = ?, country = ? where id = ?", (
      client.name,
      client.phone,
      client.address,
      client.zip_code,
      client.city,
      client.neighborhood,
      client.country,
      id
    ))

    return result

  def update_client_is_activate(self,id):
    return self.database.update_by_id("update client set is_active = 0 where id = ?", (id))