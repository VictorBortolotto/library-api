import os

class CreateFolderDatabase: 
  def create_folder():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(current_dir, "../../../../../../"))
    folder_path = os.path.join(root_dir, "database")
    os.makedirs(folder_path, exist_ok=True)