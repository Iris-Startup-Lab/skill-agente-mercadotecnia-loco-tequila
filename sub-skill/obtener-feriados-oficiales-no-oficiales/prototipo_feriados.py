# -*- coding: utf-8 -*-
"""prototipo_feriados.py - Prototipo exploratorio de APIs y scraping de feriados.

Exportado originalmente desde Google Colab.

# !pip install -q --upgrade holidays

from datetime import date, timedelta
import holidays
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

current_year = date.today().year

mx_holidays = holidays.MX(years=[current_year])

for date, name in sorted(mx_holidays.items()):
  print(f'{date}: {name}')

"""### Días no oficiales"""

wikipedia_url = f'https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_festivos_en_M%C3%A9xico'

print(f"Attempting to scrape: {wikipedia_url}")

unofficial_holidays_scraped = []

try:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(wikipedia_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    print("\n--- Found Wikipedia annex page. Looking for tables. ---")

    tables = soup.find_all('table', {'class': 'wikitable'})

    if not tables:
        print("No wikitable found on the page. Scraping might not be successful.")

    spanish_months = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
        'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }

    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['th', 'td'])
            col_texts = [ele.get_text(strip=True) for ele in cols]

            date_pattern = re.compile(r'(\d{1,2})\s+de\s+([a-záéíóúüñ]+)', re.IGNORECASE)

            for i, text in enumerate(col_texts):
                match = date_pattern.search(text)
                if match:
                    day = int(match.group(1))
                    month_name = match.group(2).lower()
                    month = spanish_months.get(month_name)

                    if day and month:
                        try:
                            hol_date = date(current_year, month, day)
                            name = text.replace(match.group(0), '').strip()
                            if not name and i + 1 < len(col_texts):
                                name = col_texts[i+1]
                            if not name:
                                name = f"Día {day} de {month_name.capitalize()}"


                            name = re.sub(r'\s*\((\d{4})\)', '', name).strip()
                            name = name.split('(', 1)[0].strip()

                            unofficial_holidays_scraped.append((hol_date, name, 'No oficial'))
                            break
                        except ValueError as ve:
                            pass

    print(f"--- Finished extracting raw holidays from tables. Found {len(unofficial_holidays_scraped)} entries. ---\n")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}\n")
except Exception as e:
    print(f"An error occurred during parsing: {e}\n")

all_holidays = []

for hol_date, hol_name in mx_holidays.items():
    all_holidays.append((hol_date, hol_name, 'Official'))

for hol_date, hol_name, hol_type in unofficial_holidays_scraped:
    if not any(h[0] == hol_date and h[1] == hol_name for h in all_holidays):
        all_holidays.append((hol_date, hol_name, hol_type))

all_holidays.sort(key=lambda x: x[0])

print("--- Combined Holidays (Official and Scraped) for the current year ---")
for hol_date, hol_name, hol_type in all_holidays:
    print(f'{hol_date.strftime("%Y-%m-%d")}: {hol_name} ({hol_type})')

holidays_df = pd.DataFrame(all_holidays, columns=['Fecha', 'Día Festivo', 'Tipo'])


holidays_df['priority'] = holidays_df['Tipo'].apply(lambda x: 0 if x == 'Official' else 1)


def create_match_key(row):
    date_str = row['Fecha'].strftime('%Y-%m-%d')
    name = row['Día Festivo'].lower()

    if 'new year\'s day' in name or 'año nuevo' in name or 'víspera delaño nuevo' in name:
        return f"{date_str}-año nuevo"
    if 'constitution day' in name or 'día de la constitución' in name:
        return f"{date_str}-día de la constitución"
    if 'benito juárez\'s birthday' in name or 'natalicio de benito juárez' in name or 'natalicio debenito juárez' in name:
        return f"{date_str}-natalicio de benito juárez"
    if 'labor day' in name or 'día del trabajador' in name:
        return f"{date_str}-día del trabajador"
    if 'independence day' in name or 'día de la independencia' in name or 'aniversario de laindependencia' in name:
        return f"{date_str}-día de la independencia"
    if 'revolution day' in name or 'día de la revolución mexicana' in name or 'día delarevolución mexicana' in name:
        return f"{date_str}-día de la revolución mexicana"
    if 'christmas day' in name or 'navidad' in name:
        return f"{date_str}-navidad"

    clean_name = re.sub(r'\s*\((\d{4}|\w+)\)', '', name).strip()
    clean_name = clean_name.split('(', 1)[0].strip()
    clean_name = clean_name.replace('de los reyes magos', 'de reyes magos')
    clean_name = clean_name.replace('día de la candelaria', 'candelaria')
    clean_name = re.sub(r'\b(día |aniversario |natalicio |conmemoración |de |la |el |los |las |y )\b', '', clean_name).strip()
    clean_name = ' '.join(sorted(list(set(clean_name.split()))))
    return f"{date_str}-{clean_name}"

holidays_df['match_key'] = holidays_df.apply(create_match_key, axis=1)

holidays_df = holidays_df.sort_values(by=['match_key', 'priority', 'Día Festivo'], ascending=[True, True, True])

holidays_df = holidays_df.drop_duplicates(subset=['match_key'], keep='first')

holidays_df = holidays_df.drop(columns=['priority', 'match_key'])

holidays_df = holidays_df.sort_values(by=['Fecha']).reset_index(drop=True)

## Filtros
# Lista actualizada con las cadenas exactas encontradas en el DataFrame para una eliminación precisa.
no_desire_days = ['Conmemoración de los sismos de1985,2017y2022',
                  'Colisión de trenes en Indios Verdes',
                  'Conmemoración de laMasacre de Tlatelolco',
                  'Colisión de trenes en el Metro de la Ciudad de México de 1975',
                  'En conmemoración del',
                  'Del 16 al',
                  'Conmemoración delEl Halconazo',
                  'Accidente del Metro de la Ciudad de México de 2021',
                  'Conmemoración de laMasacre en La Alameda',
                  'Gesta Heroica delBatallón de San Patricioen la...',
                  'Conmemoración de la gesta heroica del Batallón...'
                 ]

# Filter out rows where 'Día Festivo' is in the no_desire_days list
holidays_df = holidays_df[~holidays_df['Día Festivo'].isin(no_desire_days)]

# Filter out rows where 'Día Festivo' is empty or contains only whitespace
holidays_df = holidays_df[holidays_df['Día Festivo'].str.strip().astype(bool)]

display(holidays_df)

import matplotlib.pyplot as plt
import seaborn as sns

df_grouped = holidays_df.groupby('Fecha').size().reset_index(name='size')