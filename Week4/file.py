# File Read & Write with Error Handling

# Ask the user for the original filename
original_filename = input("Enter the filename to read: ")

try:
    # Try to open and read the file
    with open(original_filename, "r") as infile:
        content = infile.read()
    
    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()
    
    # Ask the user for the new filename
    new_filename = input("Enter the filename to save the modified content: ")
    
    # Write the modified content to the new file
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)
    
    print(f"Success! Modified file created: {new_filename}")

except FileNotFoundError:
    print(f"Error: The file '{original_filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read/write the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")