from flask import Flask
from controller.client.ClientController import ClientController
from controller.user.UserController import UserController
from controller.book.BookController import BookController
from controller.bookLoan.BookLoanController import BookLoanController
from database.Database import Database
from flask_cors import CORS
from utils.CreateFolderDatabase import CreateFolderDatabase
app = Flask(__name__)

CORS(app, resources={
    r"/note*": {
        "origins": ["null", "http://localhost:8080"],
        "methods": ["GET", "POST", "PUT", "DELETE", "PATCH"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

def create_database_folder():
  CreateFolderDatabase.create_folder()

def initialize_database():
  Database().create_table()

def main():
  UserController(app)
  ClientController(app)
  BookController(app)
  BookLoanController(app)

create_database_folder()
initialize_database()
main()

if __name__ == "__main__":
  app.run(port=8080)