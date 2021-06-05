import os
import shutil

# file extension
dict_items = {
    'Audio_extension': ('.mp3', '.wav'),
    'vedio_extension': ('.mp4', '.mkv', '.MKV'),
    'document_extension': ('.pdf', '.txt', 'doc')
}

# user input
folderPath = input("Enter folder path:- ")

# define fuction


def file_finder(Folder_path, file_extension):
    files = []
    for file in os.listdir(Folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files


# file working
for extension_type, extension_tuple in dict_items.items():
    Folder_name = extension_type.split('_')[0] + ' Files'
    Folder_path = os.path.join(folderPath, Folder_name)
    os.mkdir(Folder_path)
    for item in file_finder(folderPath, extension_tuple):
        item_path = os.path.join(folderPath, item)
        item_new_path = os.path.join(Folder_path, item)
        shutil.move(item_path, item_new_path)
