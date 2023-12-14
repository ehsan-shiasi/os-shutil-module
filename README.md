# os-shutil-module
File Organizer
This simple Python script helps you organize files in a specified directory based on their types. It categorizes files into different folders according to their extensions.
Usage
Clone the repository:
git clone https://github.com/ehsan-shiasi/os-shutil-module.git

Move to the project directory:
cd os-shutil-module

Run the script:
python organize_files_os_shutil.py

Make sure to replace /path/to/your/directory in the script with the target directory path you want to organize.

Script Explanation
The script defines a function organize_files that takes a directory path as input and organizes files within that directory into subdirectories based on their file types. The supported file types and their corresponding subdirectories are specified in the file_types dictionary.

The script also includes helper functions:

create_destination_folders: Creates destination folders for each file type if they don't already exist.
move_file: Moves a file to its corresponding destination folder.
The example usage at the end of the script demonstrates how to use the organize_files function. Replace the target_directory variable with the path of the directory you want to organize.

Customization
Feel free to customize the file_types dictionary by adding or removing file types based on your requirements. You can extend the script to support additional file types by adding entries to the dictionary.

file_types = {
    "txt": "TextFiles",
    "docx": "WordDocuments",
    "pdf": "PDFs",
    "jpg": "Images",
    "mp4": "Videos",
    "csv": "CSVFiles",
    "zip": "ZipFiles"
    # Add more file types as needed
}

Contribution
Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are highly appreciated!

