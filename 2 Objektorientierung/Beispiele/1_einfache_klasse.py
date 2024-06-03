class Person:

    # Konstruktur
    def __init__(self, name, alter, lieblingsfarbe):
        self.name = name
        self.alter = alter
        self.lieblingsfarbe = lieblingsfarbe

    # Methode
    def aendere_lieblingsfarbe(self, neue_farbe):
        self.lieblingsfarbe = neue_farbe

    # Methode
    def feiere_geburstag(self):
        print("Happy Birthday!")
        self.alter += 1


p1 = Person("Hans", 28, "gelb")
print(p1.lieblingsfarbe)

p1.aendere_lieblingsfarbe("blau")
print(f"Meine neue Lieblingsfarbe: {p1.lieblingsfarbe}")

p1.feiere_geburstag()
print(p1.alter)
