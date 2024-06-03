class Auto:
    def __init__(self, farbe):
        print(f"in init: {self}")
        self.farbe = farbe

    def farbe_ausgeben(self):
        print(self.farbe)

# hier sind wir außerhalb des Klassen-Scope
mein_auto = Auto("grün")
print(f"außerhalb von init: {mein_auto}")

# in beiden Fällen wird das selbe "Auto object" im Arbeitsspeicher abgerufen
print(mein_auto.farbe)
mein_auto.farbe_ausgeben()


""" ---------------------- """

# funkioniert exakt gleich
class AnderesAuto:
    def __init__(this, farbe):
        this.farbe = farbe

    def farbe_ausgeben(this):
        print(this.farbe)

mein_anderes_auto = AnderesAuto("gelb")
print(mein_anderes_auto.farbe)
mein_anderes_auto.farbe_ausgeben()


""" ---------------------- """

# was passiert, wenn wir diese Referenz weglassen?
class KomplettAnderesAuto:
    def __init__():
        pass

mein_komplett_anderes_auto = KomplettAnderesAuto()

# Antwort: Python braucht sie, wir kommen nicht drum herum
# ohne self. hätten wir nur eine lokale Variable definiert

class KomplettAnderesAuto:
    def __init__(self, farbe):
        meine_farbe = farbe # lokale Variable
        print(f"meine Farbe ist {meine_farbe}")

    def farbe_ausgeben(self):
        print(self.meine_farbe)

mein_komplett_anderes_auto = KomplettAnderesAuto("rot")
print(mein_komplett_anderes_auto.meine_farbe)
mein_komplett_anderes_auto.farbe_ausgeben()
