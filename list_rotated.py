import pandas
import tabula
import pandas as pd
from extract_files import extract_all_files


def get_clean_list_from_pdf(liste):
    plans = pandas.DataFrame()
    plans["DN mm"] = ["6", "8", "10", "12", "14", "16", "18", "20", "22", "25", "26", "28", "32", "36", "40"]
    for files in liste:
        """read PDF with Tabula& convert into *.csv File"""
        tabula.convert_into(input_path=fr"E:\Projekte\Stahllisten\Listen\{files}",
                            output_path=rf"E:\Projekte\Stahllisten\Output\outputliste.csv",
                            output_format= "csv", pages="all")

        """Import *.csv file as Pandas Dataframe"""
        new_data = pd.read_csv(r"E:\Projekte\Stahllisten\Output\outputliste.csv", header=None)
        new_data = new_data.fillna(0)
        plans[f"{files}"] = new_data[2] + new_data[6]

    plans.to_excel(r"E:\Projekte\Stahllisten\Output\Stahllisteconv.xlsx")


get_clean_list_from_pdf(extract_all_files())

