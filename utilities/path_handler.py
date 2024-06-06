import os

# Return the database directory.
def get_database_directory():
    try:
        current_directory = os.getcwd()
        return os.path.abspath(os.path.join(current_directory, 'database'))
    except Exception as e:
        print(f"Error getting the database directory: {e}")
        return None

# Return the name of the first .txt file found in the specified directory.
def get_txt_file_in_directory(directory):
    try:
        txt_files = [file for file in os.listdir(directory) if file.endswith('.txt')]
        if txt_files:
            return os.path.join(directory, txt_files[0])
        else:
            raise FileNotFoundError("No .txt file found in the directory.")
    except Exception as e:
        print(f"Error getting the .txt file in the directory: {e}")
        return None

# Return the full path of the first .txt file found in the database directory.
def get_full_path_of_first_database_txt_file():
    try:
        database_directory = get_database_directory()
        if database_directory is not None:
            return get_txt_file_in_directory(database_directory)
        else:
            print("Database directory not found.")
            return None
    except Exception as e:
        print(f"Error getting the full path of the .txt file: {e}")
        return None