import pandas as pd

df = pd.read_excel("vbs_persoonlike_inligting.xlsx")

def search_info(name):
    name = name.strip().lower()
    person = df[df["Name"].str.lower() == name.lower()]
    if not person.empty:
        return person.iloc[0].to_dict()
    else:
        return "Geen persoon soos dit bestaan nie."