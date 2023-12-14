import os
import shutil
from pathlib import Path


def organize_files(directory):
    # Define file type mappings
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

    # Ensure destination folders exist or create them
    create_destination_folders(directory, file_types.values())

    # Organize files based on their types
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower()

            if file_extension in file_types:
                destination_folder = os.path.join(directory, file_types[file_extension])
                move_file(file_path, destination_folder, filename)


def create_destination_folders(base_directory, folder_names):
    # Create destination folders if they don't exist
    for folder_name in folder_names:
        folder_path = os.path.join(base_directory, folder_name)
        Path(folder_path).mkdir(parents=True, exist_ok=True)


def move_file(source_path, destination_folder, filename):
    # Move file to the destination folder
    shutil.move(source_path, os.path.join(destination_folder, filename))


if __name__ == "__main__":
    # Example Usage:
    target_directory = "/path/your_directory"
    organize_files(target_directory)
