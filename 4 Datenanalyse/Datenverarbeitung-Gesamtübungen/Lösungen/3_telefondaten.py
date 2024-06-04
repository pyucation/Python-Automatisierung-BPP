"""
Aufgabe:
Analysiere die Telefondaten aus der Datei "telefondaten.csv":

    1. Überprüfe die Datei auf fehlende Daten und bereinige Sie ggfs.
    2. Grundlegende Statistiken:
        Berechne die durchschnittliche Anrufdauer.
        Ermittele die häufigsten Anrufer und Empfänger.
        Zeige die Verteilung der Anrufdauer.
    3. Erweiterte Analysen:
        Analysiere die Anzahl der Anrufe pro Tag.
        Untersuche die Verteilung der Anrufe nach Standort.
        Finde heraus, ob es einen Zusammenhang zwischen der Anrufdauer und dem Standort gibt.
    4. Visualisierung:
        Erstelle ein Histogramm der Anrufdauer.
        Visualisiere die häufigsten Anrufer und Empfänger mit einem Balkendiagramm.
        Erstelle ein Liniendiagramm, das die Anzahl der Anrufe pro Tag zeigt.
"""
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('4 Datenanalyse/Datenverarbeitung-Gesamtübungen/telefondaten.csv')

print(df.head())

print(df.isnull().sum())

# durchschnittliche Anrufdauer berechnen
durchschnittliche_dauer = df['Dauer (Minuten)'].mean()
print(f'Durchschnittliche Anrufdauer: {durchschnittliche_dauer} Minuten')

# häufigste Anrufer und Empfänger ermitteln
häufigste_anrufer = df['Anrufer'].value_counts()
häufigste_empfänger = df['Empfänger'].value_counts()
print('Häufigste Anrufer:')
print(häufigste_anrufer)
print('Häufigste Empfänger:')
print(häufigste_empfänger)

# Anrufdauer-Verteilung anzeigen
plt.figure(figsize=(10, 6))
plt.hist(df['Dauer (Minuten)'], bins=10)
plt.title('Verteilung der Anrufdauer')
plt.xlabel('Dauer (Minuten)')
plt.ylabel('Anzahl')
plt.show()

# Anzahl der Anrufe pro Tag analysieren
df['Datum'] = pd.to_datetime(df['Zeitstempel']).dt.date
anrufe_pro_tag = df['Datum'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
anrufe_pro_tag.plot(kind='line')
plt.title('Anzahl der Anrufe pro Tag')
plt.xlabel('Datum')
plt.ylabel('Anzahl der Anrufe')
plt.show()

# Verteilung der Anrufe nach Standort analysieren
standort_verteilung = df['Standort'].value_counts()
plt.figure(figsize=(10, 6))
standort_verteilung.plot(kind='bar')
plt.title('Verteilung der Anrufe nach Standort')
plt.xlabel('Standort')
plt.ylabel('Anzahl der Anrufe')
plt.show()
