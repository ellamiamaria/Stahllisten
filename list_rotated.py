import tabula
import pandas as pd


def get_clean_list_from_pdf(checked_list):
    plans = pd.read_excel(r"E:\Projekte\Stahllisten\Output\Stahllisteconv.xlsx")
    print(plans)
    for files in checked_list:
        """read PDF with Tabula& convert into *.csv File"""
        tabula.convert_into(input_path=fr"E:\Projekte\Stahllisten\Listen\{files}",
                            output_path=rf"E:\Projekte\Stahllisten\Output\outputliste.csv",
                            output_format="csv", pages="all")

        """Import *.csv file as Pandas Dataframe"""
        new_data = pd.read_csv(r"E:\Projekte\Stahllisten\Output\outputliste.csv", header=None)
        new_data = new_data.fillna(0)
        headname = files[0:10]
        plans[f"{headname}"] = new_data[2] + new_data[6]

    plans.to_excel(r"E:\Projekte\Stahllisten\Output\Stahllisteconv.xlsx")
