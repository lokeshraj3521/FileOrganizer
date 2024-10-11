# File Organizer 🗂️

A Python script that automatically organizes files into folders based on their file extensions. This script is helpful when your download or work folder is cluttered with files of different types, and you want to organize them in one go.

## 🚀 Features

- Automatically sorts files into folders based on their extension.
- Creates new folders for file extensions if they don’t exist.
- Efficiently moves files from the main directory to their respective subfolders.

## 📂 How It Works

1. The script prompts the user for a directory path.
2. It scans the folder and identifies all the files.
3. For each file, it checks the file extension and moves it to a folder named after that extension (e.g., all `.txt` files go into a `txt` folder).
4. If a folder for that extension doesn't exist, the script creates one and then moves the file.
