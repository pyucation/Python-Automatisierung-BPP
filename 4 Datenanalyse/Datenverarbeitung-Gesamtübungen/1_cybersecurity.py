"""
Aufgabe:

    1. Daten einlesen:
        Lies die Log-Daten aus der CSV-Datei mit Pandas ein. (cybersecurity_logs.csv)

    2. Daten vorverarbeiten:
        Konvertiere die timestamp-Spalte in das Datetime-Format.
        Gruppiere die Daten nach event_type und berechne die Gesamtzahl der packet_count für jeden Ereignistyp.

    3. Daten analysieren:
        Finde heraus, welche IP-Adresse die meisten Ereignisse ausgelöst hat.
        Bestimme den Zeitraum mit der höchsten Anzahl an Paketen.

    4. Daten visualisieren:
        Erstelle ein Liniendiagramm, das die Anzahl der Pakete pro Zeitstempel für jeden Ereignistyp zeigt.
        Erstellee ein Balkendiagramm, das die Gesamtzahl der Pakete für jeden Ereignistyp darstellt.
        Erstelle ein Kreisdiagramm, das den Anteil der verschiedenen Ereignistypen an der Gesamtanzahl der Pakete zeigt.

Hinweis: Die folgenden Funktionen könnten hilfreich sein:
- reset_index() (zusammen mit groupby)
- idxmax()
- unique()
- im Zusammenhang mit groupby kann man dieser Funktion ein pd.Grouper-Objekt übergeben,
dieses eignet sich hervorragend zur Verwendung von timestamp-Daten (hier gerne in die Lösung
schauen, wer nicht weiterkommt, das ist nicht trivial)         
"""
import pandas as pd
import matplotlib.pyplot as plt


# Daten einlesen


# Daten vorverarbeiten


# Analyse


# Visualisierung


# Liniendiagramm


# Balkendiagramm


# Kreisdiagramm
