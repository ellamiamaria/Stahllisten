from extract_files import extract_all_files, check_files
from list_rotated import get_clean_list_from_pdf
from extract_files import create_new_checked_files

file_list = extract_all_files()
checked_list = check_files(file_list)
get_clean_list_from_pdf(checked_list)


create_new_checked_files(file_list)