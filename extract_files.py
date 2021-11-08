import os


def extract_all_files(path):
    """Extract all files from given folder"""
    file_list = []
    for file in os.listdir(rf"{path}"):
           file_list.append(file)
    return file_list

def check_files(liste):
    """Check if files have already been converted into excel"""
    with open(r"C:\Users\ellag\PycharmProjects\stahllisten\checked_files.txt") as f:
        list_checked = f.readlines()
        list_cleared = []

        for element in list_checked:
            list_cleared.append(element.strip())

        for element in list(liste):
            if element in list(list_cleared):
                liste.remove(element)        
    return liste


def create_new_checked_files(file_list):
    """Create new check file for coming updates"""
    with open("checked_files.txt", "w") as checked:
        for files in file_list:
            checked.write(files + "\n")
