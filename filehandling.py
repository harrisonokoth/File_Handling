def create_file():
    try:
        # File Creation: Creating a new file and writing initial content
        with open("my_file.txt", 'w') as file:
            file.write("Line 1: Hello, World!\n")
            file.write("Line 2: Python file handling is fun.\n")
            file.write("Line 3: Number of stars: 5\n")
        print("File 'my_file.txt' created and written successfully.")

    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file():
    try:
        # File Reading and Display
        with open("my_file.txt", 'r') as file:
            content = file.read()
        print("File content:")
        print(content)

    except FileNotFoundError:
        print("File not found: Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        # File Appending: Appending additional lines
        with open("my_file.txt", 'a') as file:
            file.write("Line 4: Appending more text.\n")
            file.write("Line 5: Learning Python is great!\n")
            file.write("Line 6: End of file.\n")
        print("Lines appended successfully.")

    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        create_file()
        read_file()
        append_to_file()
        read_file()  # Display updated content

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations completed.")

if __name__ == "__main__":
    main()
