import sqlite3
import os
from pathlib import Path

class Database:
  def get_connection(self):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.abspath(os.path.join(base_dir, "../../../../../../database/database.db"))
    return sqlite3.connect(db_path)
  

  def create_table(self):
    conn = self.get_connection()
    cursor = conn.cursor()

    base_path = Path(__file__).resolve().parent.parent.parent
    sql_path = base_path / "resources" / "create_tables.sql"

    with sql_path.open("r", encoding="utf-8") as file:
        sql_script = file.read()

    cursor.executescript(sql_script)

    conn.commit()
    conn.close()

  def insert(self, query, query_params):
    conn = self.get_connection()
    cursor = conn.cursor()

    try:
      result = cursor.execute(query, query_params).lastrowid
      conn.commit()
      return result
    except Exception as err:
      print(err)
    finally:
      conn.close()

  def delete_by_id(self, query, id):
    conn = self.get_connection()
    cursor = conn.cursor()

    try:
      result = cursor.execute(query, id).rowcount
      conn.commit()
      return result
    except Exception as err:
      print(err)
    finally:
      conn.close()

  def find_by_id(self, query, id):
    conn = self.get_connection()
    cursor = conn.cursor()

    try:
      return cursor.execute(query, id).fetchone()
    except Exception as err:
      print(err)
    finally:
      conn.close()

  def find_all_by(self, query, query_params):
    conn = self.get_connection()
    cursor = conn.cursor()

    try:
      return cursor.execute(query, query_params).fetchall()
    except Exception as err:
      print(err)
    finally:
      conn.close()    

  def update_by_id(self, query, query_params):
    conn = self.get_connection()
    cursor = conn.cursor()

    try:
      result = cursor.execute(query, query_params).rowcount
      conn.commit()
      return result
    except Exception as err:
      print(err)
    finally:
      conn.close()