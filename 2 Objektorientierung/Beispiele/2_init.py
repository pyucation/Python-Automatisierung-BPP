class Auto:
    def __init__(self, farbe):
        self.farbe = farbe
        print("init wurde ausgeführt")

print("vor der 'Geburt' / Objekt wurde noch nicht erstellt")
mein_auto = Auto("rot")
print("nach der 'Geburt' / Objekt wurde erstellt")
