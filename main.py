from extract_files import extract_all_files, check_files
from list_rotated import get_clean_list_from_pdf
from extract_files import create_new_checked_files

"""Check Values!"""
"""Check path to checked_files.txt!"""


path = input("Bitte Input Ordner festlegen: ")
output = input("Bitte Output Ordner festlegen: ")
file_list = extract_all_files(path)
checked_list = check_files(file_list)
get_clean_list_from_pdf(checked_list, output, path)


create_new_checked_files(file_list)
