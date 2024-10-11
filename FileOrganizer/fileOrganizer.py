import os
import shutil

# Get the path from the user
path = input("Enter Path: ")

# Get the list of files in the directory
files = os.listdir(path)

# Iterate over each file
for file in files:
    # Get the filename and extension
    filename, extension = os.path.splitext(file)
    
    # Skip directories or files with no extension
    if extension:
        extension = extension[1:]  # Remove the leading dot from the extension
        
        # Check if the directory for the extension exists
        if os.path.exists(os.path.join(path, extension)):
            # Move the file to the corresponding folder
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
        else:
            # Create a new folder for the extension and move the file
            os.makedirs(os.path.join(path, extension))
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
