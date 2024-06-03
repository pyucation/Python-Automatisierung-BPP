"""
Aufgabe: Schreibe ein Skript, das die folgenden Wetterdaten visualisiert.
Diese sollen, wie bei solchen Diagrammen üblich, in einem Diagramm dargestellt werden.
Hinweise: Die Funktionen ax1.twinx() zur Erstellung einer zweiten x-Achse könnte hilfreich sein.

Im Übungsordner befindet sich ein gespeichertes Diagramm, das zeigt, wie so ein Diagramm aussehen kann.
Die genaue Gestaltung ist natürlich dir überlassen.
"""
import matplotlib.pyplot as plt


# Daten
monate = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez']
temperaturen = [0.5, 1.0, 5.5, 9.0, 14.0, 18.5, 21.0, 20.0, 16.0, 10.0, 4.5, 1.0]
niederschlag = [50, 40, 55, 60, 70, 80, 90, 85, 70, 60, 55, 50]


fig, ax1 = plt.subplots()

# dein Code hier
