import tabula
import pandas as pd


def get_clean_list_from_pdf(checked_list, output, path):
    index = ["6", "8", "10", "12", "14", "16", "18", "20", "22", "25", "26", "28", "32", "36", "40"]
    try:
        f = open(fr"{output}\Stahllisteconv.xlsx")
        plans = pd.read_excel(fr"{output}\Stahllisteconv.xlsx", index_col=[0])

    except IOError:
        plans = pd.DataFrame()
        plans["DN mm"] = index
        checked = open("checked_files.txt", "w")
        checked.close()

    for files in checked_list:
        """read PDF with Tabula& convert into *.csv File"""
        tabula.convert_into(input_path=fr"{path}\{files}",
                            output_path=rf"{output}\outputliste.csv",
                            output_format="csv", pages="all")

        """Import *.csv file as Pandas Dataframe"""
        new_data = pd.read_csv(rf"{output}\outputliste.csv", header=None)
        new_data = new_data.fillna(0)
        headname = files[0:10]

        """Check import values - 6 or 34 columns?"""
        data_size = len(new_data.columns)
        if data_size == 7:
            plans[f"{headname}"] = new_data[2] + new_data[6]

        else:
            plans[f"{headname}"] = new_data[4]

    plans.to_excel(rf"{output}\Stahllisteconv.xlsx")

