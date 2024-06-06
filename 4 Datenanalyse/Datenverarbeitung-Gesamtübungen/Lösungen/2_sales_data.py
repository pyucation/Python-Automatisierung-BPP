"""
Aufgabe:
1. Lese die CSV-Dateien der Verkaufszahlen für die einzelnen Monate als Pandas
Dataframe ein.
2. Kombiniere die einzelnen Dateframes zu einem Quartals-Dataframe. (Hinweis:
pd.concat())
3. Berechne den Gesamtumsatz pro Monat und finde heraus, welches Produkt den höchsten
Umsatz erzielt hat.
4. Fasse die Stückzahlen pro Kategorie zusammen.
5. Erstelle ein Diagramm, um die Verkaufszahlen und eins, um die Umsätze darzustellen.
6. Erstelle eine Excel-Datei mit 3 Worksheets:
    - Verkaufsdaten: Die Daten mit den Spalten Produkt, Kategorie, Stückzahl, Umsatz und Monat
    - Monatlicher Umsatz: Spalten Monat und Umsatz, jeweil für die einzelnen Monate
    - Verkäufe nach Kategorie: Spalten Kategorie und Stückzahl, jeweils für Elektronik und Zubehör
    Hinweis: groupby(...).sum() liefert `pd.Series` (eine Serie ist quasi wie eine einzelne
    Spalte eines Dataframes) zurück. Dieser kann mit der Funktion .to_frame()
    wieder in einen Dataframe umgewandelt werden. Diesen kannst du anschließend mit .to_excel()
    in eine Excel-Datei schreiben, wie in den Beispielen zuvor.
7. (Zusatz, zeige ich dir) Erstelle einen Abschlussbericht als PDF-Datei.
"""
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# CSV-Daten einlesen
df_january = pd.read_csv('4 Datenanalyse/Datenverarbeitung-Gesamtübungen/sales_january.csv')
df_february = pd.read_csv('4 Datenanalyse/Datenverarbeitung-Gesamtübungen/sales_february.csv')
df_march = pd.read_csv('4 Datenanalyse/Datenverarbeitung-Gesamtübungen/sales_march.csv')

# Monatsspalte hinzufügen
df_january['Monat'] = 'Januar'
df_february['Monat'] = 'Februar'
df_march['Monat'] = 'März'

# Daten kombinieren
df = pd.concat([df_january, df_february, df_march], ignore_index=True)
print(df)

# Analysen durchführen
# 1. Gesamtumsatz pro Monat
monthly_revenue = df.groupby('Monat')['Umsatz'].sum()

# 2. Produkt mit dem höchsten Umsatz
top_product = df.groupby('Produkt')['Umsatz'].sum().idxmax()

# 3. Verkaufszahlen nach Kategorien
category_sales = df.groupby('Kategorie')['Stückzahl'].sum()

# Ergebnisse visualisieren
# Gesamtumsatz pro Monat
plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind='bar')
plt.title('Gesamtumsatz pro Monat')
plt.xlabel('Monat')
plt.ylabel('Umsatz')
plt.savefig('monthly_revenue.png')
plt.show()

# Verkaufszahlen nach Kategorien
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar')
plt.title('Verkaufszahlen nach Kategorien')
plt.xlabel('Kategorie')
plt.ylabel('Stückzahl')
plt.savefig('category_sales.png')
plt.show()

# Daten in eine Excel-Datei speichern
excel_path = 'sales_data.xlsx'
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Verkaufsdaten')
    monthly_revenue.to_frame(name='Umsatz').to_excel(writer, sheet_name='Monatlicher Umsatz')
    category_sales.to_frame(name='Stückzahl').to_excel(writer, sheet_name='Verkäufe nach Kategorie')

print(f'Daten wurden erfolgreich in {excel_path} gespeichert.')

# Bericht erstellen mit FPDF
# dazu erstellen wir eine Klasse
class PDF(FPDF):

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Verkaufsbericht', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Seite {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_image(self, image_path):
        self.image(image_path, 10, 60, 190)

# PDF-Dokument erstellen
pdf = PDF()
pdf.add_page()

pdf.chapter_title('Gesamtumsatz pro Monat')
pdf.add_image('monthly_revenue.png')

# neue Seite
pdf.add_page()

pdf.chapter_title('Verkaufszahlen nach Kategorien')
pdf.add_image('category_sales.png')

# neue Seite
pdf.add_page()

pdf.chapter_title('Zusammenfassung')
summary_text = f"""
Der Gesamtumsatz pro Monat zeigt, dass der höchste Umsatz im Januar erzielt wurde.
Das Produkt mit dem höchsten Umsatz ist {top_product}.
Die Verkaufszahlen nach Kategorien zeigen, dass Elektronikprodukte am meisten verkauft wurden.
"""
pdf.chapter_body(summary_text)

# PDF speichern
pdf_output_path = 'sales_report.pdf'
pdf.output(pdf_output_path)
print(f'Der Bericht wurde erfolgreich in {pdf_output_path} gespeichert.')

# Aufräumen (das ist natürlich optional): temporäre Bilder löschen
os.remove('monthly_revenue.png')
os.remove('category_sales.png')
