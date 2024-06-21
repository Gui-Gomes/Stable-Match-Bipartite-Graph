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


# Return the list of .txt files found in the specified directory.
def get_txt_files_in_directory(directory):
    try:
        txt_files = [file for file in os.listdir(directory) if file.endswith(".txt")]
        if txt_files:
            return txt_files
        else:
            raise FileNotFoundError("No .txt file found in the directory.")
    except Exception as e:
        print(f"Error getting the .txt files in the directory: {e}")
        return None


# Allow the user to choose a .txt file and return its full path.
def choose_txt_file_from_directory():
    try:
        txt_directory = get_txt_directory()
        if txt_directory is not None:
            txt_files = get_txt_files_in_directory(txt_directory)
            if txt_files is not None:
                print("Choose a file by entering the corresponding number:")
                for idx, file in enumerate(txt_files, start=1):
                    print(f"{idx}. {file}")

                choice = int(input("Enter the number of the file you want: "))
                if 1 <= choice <= len(txt_files):
                    chosen_file = txt_files[choice - 1]
                    return os.path.join(txt_directory, chosen_file)
                else:
                    print("Invalid choice.")
                    return None
            else:
                print("No .txt file found in the database directory.")
                return None
        else:
            print("Database directory not found.")
            return None
    except Exception as e:
        print(f"Error getting the full path of the .txt file: {e}")
        return None
