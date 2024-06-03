"""
Aufgaben:
1. Verwendung von iloc:
    Zugriff auf die dritte Zeile des DataFrames und gib sie aus.
    Zugriff auf die Spalten 'Abteilungsname' und 'Mitarbeiterzahl' der ersten drei Zeilen.
2. Verwendung von loc:
    Zugriff auf alle Zeilen, in denen die Mitarbeiterzahl größer als 20 ist.
    Zugriff auf die Abteilung mit der Abteilungs-ID 104 und gib alle zugehörigen Daten aus.
3. Kombinierter Zugriff:
    Verwende loc und iloc, um die 'Mitarbeiterzahl' der Abteilungen 'IT' und
    'Marketing' auszugeben (Hinweis: Nutze loc für die Namen und iloc für die Positionen).
4. Aktualisiere die 'Mitarbeiterzahl' der 'Finanzen'-Abteilung auf 28 mit loc.
5. Füge eine neue Abteilung hinzu, indem du loc verwendest, mit der ID 106 und
dem Namen 'Kundenservice', 18 Mitarbeitern und dem Standort 'Leipzig'.
"""
import pandas as pd


data = {
    'Abteilungs-ID': [101, 102, 103, 104, 105],
    'Abteilungsname': ['HR', 'Marketing', 'Finanzen', 'IT', 'Produktion'],
    'Mitarbeiterzahl': [15, 20, 25, 30, 35],
    'Standort': ['Berlin', 'München', 'Frankfurt', 'Hamburg', 'Stuttgart']
}
df = pd.DataFrame(data)
df.set_index('Abteilungs-ID', inplace=True)

print(df.head())
