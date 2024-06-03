"""
Aufgaben:
    1. Daten Laden und Überprüfen:
        Lade den Datensatz in einen DataFrame.
        Überprüfe die ersten zehn Einträge im DataFrame und gib die Namen der Spalten aus.

    2. Datenfilterung:
        Filtere die Daten, um nur die Einträge von Studenten im Bachelorstudium anzuzeigen.
        Filtere die Daten nach Studenten, deren Abschlussnote besser als 2.0 ist.

    3. Daten Sortieren:
        Sortiere die Daten nach der Abschlussnote in aufsteigender Reihenfolge.
        Sortiere die Daten nach dem Alter in absteigender Reihenfolge.

    4. Gruppierung und Aggregation:
        Berechne den Durchschnitt der Abschlussnoten für jedes Studienfach.
        Finde das am häufigsten genannte Lieblingsfarbe unter allen Studenten.

    5. Funktion anwenden:
        Schreibe eine Funktion, die die Matrikelnummer nimmt und den Buchstaben
        M an erste Stelle setzt. Der Rest der Matrikelnummer soll unverändert
        bleiben. Wende diese Funktion anschließend auf deinen Dataframe an.
        Bsp.: 1234 -> M1234

    Zusatz: Datenvisualisierung:
        Verwende Matplotlib, um die Verteilung der Abschlussnoten in einem Histogramm darzustellen.
"""
import pandas as pd
