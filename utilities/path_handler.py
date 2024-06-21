import os


# Return the database directory.
def get_database_directory():
    try:
        current_directory = os.getcwd()
        return os.path.abspath(os.path.join(current_directory, "database"))
    except Exception as e:
        print(f"Error getting the database directory: {e}")
        return None


# Function to get the TXT directory within the database directory.
def get_txt_directory():
    try:
        database_directory = get_database_directory()
        if database_directory:
            txt_directory = os.path.join(database_directory, "txt")
            if not os.path.exists(txt_directory):
                os.makedirs(txt_directory)  # Create the directory if it doesn't exist.
            return os.path.abspath(txt_directory)
        else:
            return None
    except Exception as e:
        print(f"Error getting the TXT directory: {e}")
        return None


# Function to get the CSV directory within the database directory.
def get_csv_directory():
    try:
        database_directory = get_database_directory()
        if database_directory:
            csv_directory = os.path.join(database_directory, "csv")
            if not os.path.exists(csv_directory):
                os.makedirs(csv_directory)  # Create the directory if it doesn't exist.
            # Append a slash '/' to the directory path
            csv_directory = os.path.abspath(csv_directory) + "/"
            return csv_directory
        else:
            return None
    except Exception as e:
        print(f"Error getting the CSV directory: {e}")
        return None


# Function to get the images directory within the database directory.
def get_images_directory():
    try:
        database_directory = get_database_directory()
        if database_directory:
            images_directory = os.path.join(database_directory, "images")
            if not os.path.exists(images_directory):
                os.makedirs(
                    images_directory
                )  # Create the directory if it doesn't exist.
            # Append a slash '/' to the directory path
            images_directory = os.path.abspath(images_directory) + "/"
            return images_directory
        else:
            return None
    except Exception as e:
        print(f"Error getting the images directory: {e}")
        return None


# Return the name of the first .txt file found in the specified directory.
def get_txt_file_in_directory(directory):
    try:
        txt_files = [file for file in os.listdir(directory) if file.endswith(".txt")]
        if txt_files:
            return txt_files[0]
        else:
            raise FileNotFoundError("No .txt file found in the directory.")
    except Exception as e:
        print(f"Error getting the .txt file in the directory: {e}")
        return None


# Return the full path of the first .txt file found in the database directory.
def get_first_txt_file_path_from_database():
    try:
        database_directory = get_txt_directory()
        if database_directory is not None:
            txt_file = get_txt_file_in_directory(database_directory)
            if txt_file is not None:
                return os.path.join(database_directory, txt_file)
            else:
                print("No .txt file found in the database directory.")
                return None
        else:
            print("Database directory not found.")
            return None
    except Exception as e:
        print(f"Error getting the full path of the .txt file: {e}")
        return None
