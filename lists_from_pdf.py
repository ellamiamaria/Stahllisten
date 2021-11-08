import pandas
import tabula
import pandas as pd
from extract_files import extract_all_files
import io


def get_clean_list_from_pdf(liste):
    columns = ["A", "DN mm", "Länge fix", "Gewicht fix kg", "kg/m", "B", "Länge bearb.", "Gewicht bearb"]
    data_list = []
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
        for new_row in range(round(len(data) / 8)):
            new_row = data[x:y]
            data_list.append(new_row)
            x += 8
            y += 8
    new_data = pd.DataFrame(data_list, columns=columns)
    return new_data


all_data = get_clean_list_from_pdf(extract_all_files())
del all_data["A"]
del all_data["B"]
all_data.to_excel(excel_writer=r"E:\Projekte\Stahllisten\Output\outputliste.xlsx")
