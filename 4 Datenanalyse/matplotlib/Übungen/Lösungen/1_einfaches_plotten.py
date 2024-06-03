"""
Aufgabe: Erstelle ein einfaches Liniendiagramm mit zwei Plots:
1) gestrichelte gelbe Linie
2) gepunktete blaue Linie
Die Daten sind gegeben.

Füge außerdem eine Legende und Achsenbeschriftungen hinzu.
"""
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6]
y1 = [i**(1/2) for i in x]
y2 = [i/(i**2) for i in x]

# dein Plot hier
plt.plot(x, y1, linestyle="dashed", color="yellow", label="y1")
plt.plot(x, y2, linestyle="dotted", color="blue", label="y2")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
