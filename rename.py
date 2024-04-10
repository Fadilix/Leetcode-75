import os

# Specify the directory path
directory_path = os.getcwd()

# List all items (files and folders) in the specified directory
items = os.listdir(directory_path)
items = [folder for folder in items if folder != ".git"]

# Loop through each item
for item in items:
    # Construct the full path to the item
    item_path = os.path.join(directory_path, item)
    # Check if the item is a directory
    if os.path.isdir(item_path):
        # Rename the directory by adding "0" behind the original name
        new_name = f"0{item}"
        # Construct the full path to the new directory name
        new_item_path = os.path.join(directory_path, new_name)
        # Rename the directory
        os.rename(item_path, new_item_path)
