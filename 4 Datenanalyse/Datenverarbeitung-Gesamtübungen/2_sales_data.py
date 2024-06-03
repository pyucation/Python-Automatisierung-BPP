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
# diese imports werden nur für die Zusatzaufgabe benötigt
from fpdf import FPDF
import os

