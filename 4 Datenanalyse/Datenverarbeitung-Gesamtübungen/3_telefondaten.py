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
