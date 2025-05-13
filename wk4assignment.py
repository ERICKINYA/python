def modify_content(content):
    # Example modification: convert to uppercase
    return content.upper()

def main():
    try:
        filename = input("Enter the name of the file to read: ")
        with open(filename, 'r') as infile:
            content = infile.read()
        
        modified_content = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print(" Error: You don't have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
