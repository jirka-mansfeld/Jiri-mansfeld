import requests
import xml.etree.ElementTree as ET
import csv
import pandas as pd
import plotly.graph_objects as go
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

url = "https://www.opec.org/basket/basketDayArchives.xml"

try:
    # Odešleme HTTP požadavek GET a získáme odpověď
    response = requests.get(url)

    # Zkontrolujeme, zda byl požadavek úspěšný (status code 200 značí úspěch)
    if response.status_code == 200:
        # Vytvoříme objekt ElementTree pro analýzu XML
        root = ET.fromstring(response.content)

        # Vytvoříme CSV soubor pro zápis dat
        with open("data.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)

            # Zde specifikujte logiku pro extrakci dat z XML a zápis do CSV
            for basket_list in root.findall(".//{http://tempuri.org/basketDayArchives.xsd}BasketList"):
                data = basket_list.get("data")
                val = basket_list.get("val")

                # Zápis dat do CSV souboru
                writer.writerow([data, val])

        print("Data byla uložena do souboru data.csv.")
    else:
        print("Nepodařilo se stáhnout data.")
except Exception as e:
    print("Došlo k chybě při zpracování XML:", str(e))




try:
    # Načtení dat z CSV souboru
    df = pd.read_csv("data.csv", header=None)

    # Přejmenování sloupců
    df.columns = ["data", "val"]

    # Vytvoření sloupce s procentuálním denním pohybem
    df["DailyChange"] = df["val"].pct_change() * 100

    # Vytvoření sloupce s procentuálním vývojem ceny
    df["PriceChange"] = (df["val"] - df["val"].iloc[0]) / df["val"].iloc[0] * 100

    # Uložení dat do nového CSV souboru
    df.to_csv("data_with_changes.csv", index=False)

    print("Data byla uložena do souboru data_with_changes.csv.")
except Exception as e:
    print("Došlo k chybě při zpracování dat:", str(e))




fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df['data'], y=df['PriceChange'], mode='lines', name='Price Change'))
fig1.update_layout(title='Procentuální vývoj ceny', xaxis_title='Datum', yaxis_title='Procentuální změna ceny')
fig1.write_image('price_change.png')

# Grafy s procentuálním vývojem ceny po letech
years = df['data'].str.split('-').str[0].unique()

for year in years:
    df_year = df[df['data'].str.startswith(year)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_year['data'], y=df_year['PriceChange'], mode='lines', name='Price Change'))
    fig.update_layout(title=f'Procentuální vývoj ceny - {year}', xaxis_title='Datum', yaxis_title='Procentuální změna ceny')
    fig.write_image(f'price_change_{year}.png')




# Načtení dat z CSV souboru
df = pd.read_csv("data_with_changes.csv")

# Převod sloupce "Date" na datový typ datetime
df["data"] = pd.to_datetime(df["data"])

# Seskupení dat podle roku
grouped_df = df.groupby(df["data"].dt.year)

# Výpočet průměrné hodnoty procentuálního denního pohybu pro každý rok
average_daily_change = grouped_df["DailyChange"].mean()

# Vytvoření DataFrame s průměrnými hodnotami procentuálního denního pohybu
result_df = pd.DataFrame({
    "Year": average_daily_change.index,
})

# Výpočet geometrického průměru
result_df["GeometricMean"] = grouped_df["DailyChange"].fillna(0).apply(lambda x: stats.gmean(x + 100) - 100)

# Uložení výsledného DataFrame do CSV souboru
result_df.to_csv("average_daily_change.csv", index=False)




# Načtení seskupeného DataFrame z CSV souboru
grouped_df = pd.read_csv("average_daily_change.csv")

# Vytvoření sloupcového grafu
plt.bar(grouped_df["Year"], grouped_df["GeometricMean"])

# Nastavení popisků os a názvu grafu
plt.xlabel("Year")
plt.ylabel("Average Daily Change")
plt.title("Average Daily Change by Year")

# Zobrazení grafu
plt.show()