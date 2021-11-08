import pandas
import tabula
import pandas as pd
import numpy as np
from extract_files import extract_all_files
import io


def get_clean_list_from_pdf(liste):
    index = ["6", "8", "10", "12", "14", "16", "18", "20", "22", "25", "26", "28", "32", "36", "40"]
    plans = pandas.DataFrame(index=index)
    x = 1
    for files in liste:
        """read PDF with Tabula& convert into *.csv File"""
        tabula.convert_into(input_path=fr"E:\Projekte\Stahllisten\Listen\{files}",
                            output_path=rf"E:\Projekte\Stahllisten\Output\outputliste.csv",
                            output_format= "csv", pages="all")

        """Import *.csv file as Pandas Dataframe"""
        new_data = pd.read_csv(r"E:\Projekte\Stahllisten\Output\outputliste.csv", header=None)
        print(new_data)
        new_data = new_data.fillna(0)
        print(new_data)
        plans[f"fix Gew.kg{x}"] = new_data[2]
        print(plans)
        plans[f"bearb. Gew. kg{x}"] = new_data[6]
        plans[f"{files}"] = plans[f"fix Gew.kg{x}"] + plans[f"bearb. Gew. kg{x}"]
        x += 1

    print(plans)





get_clean_list_from_pdf(extract_all_files())

