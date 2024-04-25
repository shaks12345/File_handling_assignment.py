def create_file():
    try:
        with open("my_file.txt", "c") as file:
            file.write("This is line 1\n")
            file.write("796598\n")
            file.write("Another line with text and numbers\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error creating file: {e}")
    else:
        print("File created successfully.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("Contents of my_file.txt:")
            print(contents)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to read the file.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("834875\n")
            file.write("Appending another line with text and numbers\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error appending to file: {e}")
    else:
        print("Content appended successfully.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
