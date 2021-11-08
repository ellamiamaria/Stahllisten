import pandas
import tabula
import pandas as pd
from extract_files import extract_all_files
import io


def get_clean_list_from_pdf(liste):
    number_of_tables = list(range(1, 501))
    columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for files in liste:
        """read PDF Tabula"""
        data = tabula.io.read_pdf(fr"E:\Projekte\Stahllisten\Listen\{files}", output_format="dataframe",
                                  pandas_options={"header": None}, pages="all")
        """Return splitted string without header"""
        data = str(data[0])
        data = data.split()
        del data[0:7]
        x = 0
        y = 8
        """Assort Data in Data Frame with Values for each row"""
        data_list = []
        for new_row in range(round(len(data) / 8)):
            new_row = data[x:y]
            data_list.append(new_row)
            x += 8
            y += 8
        new_data = pd.DataFrame(data_list, columns= columns)
        print(new_data)


get_clean_list_from_pdf(extract_all_files())
