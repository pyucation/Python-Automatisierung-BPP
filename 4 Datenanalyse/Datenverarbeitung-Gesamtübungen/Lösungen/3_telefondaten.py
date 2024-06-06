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
print(häufigste_anrufer) # theoretisch noch .idxmax())
print('Häufigste Empfänger:')
print(häufigste_empfänger) # theoretisch noch .idxmax())

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
anrufe_pro_tag.plot(kind='line', rot=45)
plt.title('Anzahl der Anrufe pro Tag')
plt.xlabel('Datum')
plt.ylabel('Anzahl der Anrufe')
plt.show()

# häufigste Empfänger und Anrufer
plt.figure()
anrufer = df["Anrufer"].value_counts()
empfaenger = df["Empfänger"].value_counts()
# anrufer.plot(kind='bar', position=0.1, color="green", width=0.3)
# empfaenger.plot(kind='bar', position=0.9, color="orange", width=0.3)

# wir nutzen die erste Indexspalte, um uns eine numerische x-Achse zu bauen
import numpy as np
x1 = np.arange(len(anrufer.index))
x2 = np.arange(len(empfaenger.index))
plt.bar(x1 - 0.2, anrufer, color="green", width=0.3, label="Anrufer")
plt.bar(x2 + 0.2, empfaenger, color="orange", width=0.3, label="Empfänger")
# TODO: Hannelore Schmidt ist so nciht richtig!
plt.xticks(x1, anrufer.index)
plt.title("Anrufer vs. Empfänger pro Person")
plt.ylabel("Anzahl")
plt.legend(loc="upper right")
plt.show()

# Verteilung der Anrufe nach Standort analysieren
standort_verteilung = df['Standort'].value_counts()
plt.figure(figsize=(10, 6))
standort_verteilung.plot(kind='bar')
plt.title('Verteilung der Anrufe nach Standort')
plt.xlabel('Standort')
plt.ylabel('Anzahl der Anrufe')
plt.show()
