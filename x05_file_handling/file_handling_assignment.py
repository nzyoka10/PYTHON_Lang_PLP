# Function to create a new file
def create_file():
    try:
        # Open the file in write mode ('w')
        with open("my_file.txt", 'w') as file:
            # Write some lines of text to the file
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line here\n")
        print("\n --- File creation successful. ---")
    except PermissionError:
        # Handle permission error
        print("Permission denied to create file.")
    except Exception as e:
        # Handle other exceptions
        print("An error occurred:", e)


# Function to read and display the content of the file
def read_file():
    try:
        # Open the file in read mode ('r')
        with open("my_file.txt", 'r') as file:
            print("Contents of my_file.txt:")
            # Read each line and display it
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        # Handle file not found error
        print("File not found.")
    except Exception as e:
        # Handle other exceptions
        print("An error occurred:", e)


# Function to append additional content to the file
def append_to_file():
    try:
        # Open the file in append mode ('a')
        with open("my_file.txt", 'a') as file:
            # Append some lines of text to the file
            file.write("Appending line 1\n")
            file.write("67890\n")
            file.write("Yet another line\n")
        print("Appending successful.")
    except PermissionError:
        # Handle permission error
        print("Permission denied to append to file.")
    except Exception as e:
        # Handle other exceptions
        print("An error occurred:", e)


# Main section
if __name__ == "__main__":
    # Call functions to perform file operations
    create_file()       # Create the file
    read_file()         # Read and display file contents
    append_to_file()    # Append additional content to the file
