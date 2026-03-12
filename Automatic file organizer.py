import os
import shutil

# Create a new folder
folder_name = "NewFolder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Move a file into the folder
shutil.move("Automatic file organizer", folder_name)

print("File moved successfully!")