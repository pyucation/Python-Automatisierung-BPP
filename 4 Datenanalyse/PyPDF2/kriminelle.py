# from PyPDF2 import PdfReader

# reader = PdfReader("4 Datenanalyse/PyPDF2/kriminelle.pdf")
# page = reader.pages[0]
# print(page.extract_text())

import PyPDF2
import pandas as pd
import matplotlib.pyplot as plt


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def parse_text_to_dataframe(text):
    # den Text in Abschnitte zerlegen und die relevanten Daten extrahieren
    data = []
    persons = text.split("Persönliche Daten")
    for person in persons[1:]:
        person_data = {}
        lines = person.strip().split("\n")
        # leider müssen wir die Merkmale einzeln parsen, da wir nur den
        # rohen Text extrahieren können
        for line in lines:
            if line.startswith("Name:"):
                person_data["Name"] = line.split(":")[1].strip()
            elif line.startswith("Geburtsdatum:"):
                person_data["Geburtsdatum"] = line.split(":")[1].strip()
            elif line.startswith("Geschlecht:"):
                person_data["Geschlecht"] = line.split(":")[1].strip()
            elif line.startswith("Nationalität:"):
                person_data["Nationalität"] = line.split(":")[1].strip()
            elif line.startswith("Aktuelle Adresse:"):
                person_data["Aktuelle Adresse"] = line.split(":")[1].strip()
            elif line.startswith("Größe:"):
                person_data["Größe"] = line.split(":")[1].strip()
            elif line.startswith("Gewicht:"):
                person_data["Gewicht"] = line.split(":")[1].strip()
            elif line.startswith("Augenfarbe:"):
                person_data["Augenfarbe"] = line.split(":")[1].strip()
            elif line.startswith("Haarfarbe:"):
                person_data["Haarfarbe"] = line.split(":")[1].strip()
            elif line.startswith("Straftaten:"):
                person_data["Straftaten"] = line.split(":")[1].strip()
            elif line.startswith("Verhaftungsdatum:"):
                person_data["Verhaftungsdatum"] = line.split(":")[1].strip()
            elif line.startswith("Verurteilungsdatum:"):
                person_data["Verurteilungsdatum"] = line.split(":")[1].strip()
            elif line.startswith("Urteilsdetails:"):
                person_data["Urteilsdetails"] = line.split(":")[1].strip()
            elif line.startswith("Strafe:"):
                person_data["Strafe"] = line.split(":")[1].strip()
            elif line.startswith("Standort:"):
                person_data["Standort"] = line.split(":")[1].strip()
            elif line.startswith("Zellennummer:"):
                person_data["Zellennummer"] = line.split(":")[1].strip()
            elif line.startswith("Verhalten:"):
                person_data["Verhalten"] = line.split(":")[1].strip()
        data.append(person_data)
    return pd.DataFrame(data)

# PDF-Datei einlesen
pdf_path = '4 Datenanalyse/PyPDF2/kriminelle.pdf'
text = extract_text_from_pdf(pdf_path)

# Text in DataFrame umwandeln
df = parse_text_to_dataframe(text)
print(df)

# Analysen durchführen
# 1. Verteilung der Straftaten
df['Straftaten'] = df['Straftaten'].str.split(',')
all_crimes = df.explode('Straftaten')['Straftaten'].str.strip()
crime_counts = all_crimes.value_counts()

# 2. Verurteilungszeiträume
df['Verurteilungsdatum'] = pd.to_datetime(df['Verurteilungsdatum'], format='%d.%m.%Y')
df['Verhaftungsdatum'] = pd.to_datetime(df['Verhaftungsdatum'], format='%d.%m.%Y')
df['Verurteilungszeitraum'] = (df['Verurteilungsdatum'] - df['Verhaftungsdatum']).dt.days
time_period_counts = df['Verurteilungszeitraum'].value_counts()

# 3. Geschlechterverteilung
gender_counts = df['Geschlecht'].value_counts()

# Ergebnisse visualisieren
# Verteilung der Straftaten
plt.figure(figsize=(10, 6))
crime_counts.plot(kind='bar')
plt.title('Verteilung der Straftaten')
plt.xlabel('Straftaten')
plt.ylabel('Anzahl')
plt.show()

# Verurteilungszeiträume
plt.figure(figsize=(10, 6))
time_period_counts.plot(kind='bar')
plt.title('Verurteilungszeiträume')
plt.xlabel('Tage zwischen Verhaftung und Verurteilung')
plt.ylabel('Anzahl')
plt.show()

# Geschlechterverteilung
plt.figure(figsize=(6, 6))
gender_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Geschlechterverteilung')
plt.ylabel('')
plt.show()

# Daten in eine Excel-Datei speichern
excel_path = 'kriminelle_daten.xlsx'
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Kriminelle Daten')
    crime_counts.to_frame(name='Anzahl').to_excel(writer, sheet_name='Straftaten Verteilung')
    time_period_counts.to_frame(name='Anzahl').to_excel(writer, sheet_name='Verurteilungszeiträume')
    gender_counts.to_frame(name='Anzahl').to_excel(writer, sheet_name='Geschlechterverteilung')
