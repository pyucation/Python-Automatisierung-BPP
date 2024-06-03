# Überladung und Polymorphismus beschreibt eigentlich die Möglichkeit verschiedene
# Implementierungen derselben Methode zu haben. Oder, Funktionen mit verschiedenen
# Attributen aufrufen zu können.
# Dieses Konzept wird bspw. in C++ und Java unterstützt. In Python gibt es dieses
# nicht in seiner ursprünglichen Form.

# Möglichkeit zur Überladung von Funktionen (kennen wir bereits):
# optionale Parameter
def add(a, b, c=0, d=0):
    return a + b + c + d

# oder mit *args
def add2(*args):
    return sum(args)


# wir können das Prinzip auch innerhalb einer Methode mit Typprüfungen nutzen
class MathOperations:
    def multiply(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a * b
        elif isinstance(a, str) and isinstance(b, int):
            return a * b
        else:
            raise TypeError("Unsupported types")


# was wir aber tun könne: Überschreiben von Operatoren und anderen "Magic Methods"/"Dunder Methods"
class Vogel:

    def __init__(self, art, kann_fliegen=True):
        self.art = art
        self.kann_fliegen = kann_fliegen

    def __add__(self, other: "Vogel"):
        if self.kann_fliegen and other.kann_fliegen:
            return Küken(self.art, True)
        else:
            return Küken(self.art, False)


class Küken(Vogel):

    def __init__(self, art, kann_fliegen, ist_süss=True):
        super().__init__(art, kann_fliegen)
        self.ist_süss = ist_süss

    def __str__(self):
        return f"Küken Object of type: {self.art}, cute: {self.ist_süss}"

v1 = Vogel("Huhn")
v2 = Vogel("Adler")

küken1 = v1 + v2
print(küken1)
küken2 = v2 + v1
print(küken2)

