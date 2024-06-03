"""
Aufgabe:
Schreibe eine einfache Klasse 'Auto', welche folgende Attribute und Methoden besitzt:

Attribute:
+ farbe
+ fahrgestellnummer
+ max_geschwindigkeit
+ aktuelle_geschwindigkeit

Methoden:
+ umlackieren -> ändert die Farbe des Autos
+ beschleunigen -> ändert die aktuelle Geschwindigkeit um einen übergebenen Wert bis die
maximale Geschwindigkeit erreicht ist
+ berechne_bremsweg -> gibt den Bremsweg abhängig von der aktuellen Geschwindigkeit wieder
"""

class Auto:

    def __init__(self, farbe, fahrgestellnr, max_geschwindigkeit):
        self.farbe = farbe
        self.fahrgestellnr = fahrgestellnr
        self.max_v = max_geschwindigkeit
        self.v_aktuell = 0

    def umlackieren(self, neue_farbe):
        self.farbe = neue_farbe

    def beschleunigen(self, v):
        if self.v_aktuell + v < self.max_v:
            self.v_aktuell += v
        else:
            print("Max. Geschwindigkeit ist fast erreicht.")

    def berechne_bremsweg(self):
        bremsweg = self.v_aktuell ** 2 / 100
        return bremsweg
    

auto1 = Auto("grün", 1234, 320)
auto1.umlackieren("schwarz")

auto1.beschleunigen(130)
print(auto1.berechne_bremsweg(), "m")