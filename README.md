Project: Sequential File Renamer 🧹
A Python script to clean up clutter in a folder by renaming files sequentially based on their type.

## About The Project
This script addresses the common problem of folders filled with files having inconsistent and messy names (e.g., screenshot-10-07-2025.png, image_final_v2.png, IMG_8432.jpg). The goal is to programmatically rename these files into a clean, numbered sequence for each file extension.

This exercise is designed to teach fundamental file system operations in Python using the standard os module.

## Core Functionality
Scans a Target Directory: Identifies all files within a specified folder.

Groups by File Type: Sorts files based on their extension (e.g., .png, .jpg, .pdf).

Sequential Renaming: Renames each file within a group to a simple numerical sequence (e.g., 1.png, 2.png, 3.png...). Each file type gets its own independent count.

### Example: Before & After
📂 Folder Before:

sfdsf.png
vfsf.png
this.png
design.png
photo_of_cat.jpg
vacation_pic.jpg
name.png
notes.txt
✨ Folder After:

1.png
2.png
3.png
4.png
5.png
1.jpg
2.jpg
1.txt
## Technical Requirements
The solution should be implemented in Python and must use the os module for all file system interactions. The key functions to be used are:

os.listdir(path): To get a list of all filenames in the target directory.

os.rename(source, destination): To perform the actual file renaming.

os.path.join(path, filename): To correctly construct full file paths that are compatible with any operating system.

## Conceptual Plan (How to build it)
Import the os module.

Python

import os
Define the Target Folder.
Create a variable holding the string path to the folder you want to organize.

Python

folder_path = "/path/to/your/cluttered/folder"
Get the List of Files.
Use os.listdir() to get all file and folder names from your target path.

Isolate Files and Group by Extension.

Iterate through the list of names from the previous step.

Check if each name is a file (and not a sub-folder).

Extract the file extension (e.g., .png from image.png).

Store the filenames in a dictionary where keys are the extensions and values are lists of files with that extension.

Python

# Example data structure
files_by_extension = {
    ".png": ["sfdsf.png", "vfsf.png", "this.png"],
    ".jpg": ["photo_of_cat.jpg", "vacation_pic.jpg"]
}
Iterate and Rename.

Loop through the files_by_extension dictionary (for each extension).

Inside this loop, initialize a counter to 1.

Start another loop to go through the list of filenames for the current extension.

For each filename:

Construct the old_file_path using os.path.join(folder_path, old_filename).

Construct the new_file_name (e.g., f"{counter}.png").

Construct the new_file_path using os.path.join(folder_path, new_file_name).

Call os.rename(old_file_path, new_file_path) to perform the renaming.

Increment the counter (counter += 1).

# File-manager
# File_manager
