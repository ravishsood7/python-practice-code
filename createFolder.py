import os

# List of folder names based on the index provided
folders = [
    "Introduction to Python",
    "Getting Started",
    "Python Basics",
    "Strings",
    "Decision Control Instruction",
    "Repetition Control Instruction",
    "Console Ijo",
    "Lists",
    "Tuples",
    "Sets",
    "Dictionaries",
    "Comprehensions",
    "Functions",
    "Recursion",
    "Functional Programming",
    "Modules and Packages",
    "Namespaces",
    "Classes and Objects",
    "Intricacies of Classes and Objects",
    "Containership and Inheritance",
    "Iterators and Generators",
    "Exception Handling",
    "File Ijoo",
    "Miscellany",
    "Concurrency and Parallelism",
    "Synchronization"
]

# Directory where folders will be created
base_directory = "Let_Us_Python"

# Create the base directory if it doesn't exist
if not os.path.exists(base_directory):
    os.mkdir(base_directory)

# Create folders for each chapter
for folder in folders:
    folder_path = os.path.join(base_directory, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")