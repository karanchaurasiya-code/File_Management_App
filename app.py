import os
import time



# Create new file function 
def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File '{filename}' created successfully!")
    except FileExistsError:
        print(f"File '{filename}' already exists!")
    except Exception as e:
        print(f"An error occurred: {e}")

# View all files in the current directory
def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found!")
    else:
        print("Files in directory:")
        for file in files:
            print(file)

# Delete file function 
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"'{filename}' has been deleted successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Read file function 
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Edit file function (append data)
def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Enter data to add: ")
            f.write(content + "\n")
            print(f"Content added to '{filename}' successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Search for a File function 
def search_file(filename):
    if filename in os.listdir():
        print(f"'{filename}' exists in the current directory.")
    else:
        print("File not found.")

# Rename file function 
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"'{old_name}' renamed to '{new_name}' successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Display file info function 
def file_info(filename):
    try:
        stats = os.stat(filename)
        print(f"Size: {stats.st_size} bytes")
        print(f"Created: {time.ctime(stats.st_ctime)}")
        print(f"Last Modified: {time.ctime(stats.st_mtime)}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function 
def main():
    while True:
        print("\nFile Management App")
        print("1: Create file")
        print("2: View files")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Search file")
        print("7: Rename file")
        print("8: File info")
        print("9: Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter the file name to create: ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter the file name to delete: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the file name to read: ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the file name to edit: ")
            edit_file(filename)
        elif choice == '6':
            filename = input("Enter the file name to Search: ")
            search_file(filename)
        elif choice == '7':
            old_name = input("Enter the current file name: ")
            new_name = input("Enter the new file name: ")
            rename_file(old_name, new_name) 
        elif choice == '8':
            filename = input("Enter the file name to get info: ")
            file_info(filename)   

        elif choice == '9':
            print("Closing the app.")
            print("-" * 30)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
