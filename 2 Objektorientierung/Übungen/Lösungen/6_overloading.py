"""
Problem: Wenn ich zwei Listen l1 und l2 habe und diese addieren möchte, werden sie "aneinander gehängt", statt
eine Addition durchzuführen.
Subtraktion und Multiplikation ist für Listen nicht definiert.
Das hat alles eine Berechtigung. Die folgende Übung dient ausschließlich didaktischen Zwecken.

Aufgabe: Nutze die gegebene Klasse "MyList", welche ähnlich zu Python's list Datentyp ist.
Implementiere drei Methoden, welche die Operatoren +, -, * überladen. Nutze dafür die entsprechenden
Dunder Methods:
__add__
__sub__
__mul__

Folgendes soll geleistet werden:
+: addiert die Elemente beider Objekte. Falls ein Objekt mehr Elemente als das andere haben sollten,
werden die überflüssigen Elemente einfach angehängt (quasi mit 0 addiert)
-: subtrahiert die Elemente beider Objekte. Falls ein Objekt mehr Elemente als das andere haben sollten,
werden die überflüssigen Elemente einfach angehängt, aber mit negativem Vorzeichen (quasi 0 - überschüssiges_element),
wenn das zweite Objekt länger ist, ansonsten kann es positiv bleiben
*: Elemente werden multipliziert, überschüssige Elemente werden ignoriert
"""

class MyList:

    def __init__(self, l: list[int|float] = None):
        self.items = l or []

    def append(self, item):
        self.items.append(item)

    def extend(self, l: 'MyList'):
        self.items.extend(l.items)

    def __len__(self):
        return len(self.items)


    def __add__(self, l: 'MyList'):
        new = []
        if len(l) < len(self):
            for index, element in enumerate(l.items):
                new.append(self.items[index] + element)
            new.extend(self.items[-index:])
        elif len(l) == len(self):
            for x, y in zip(self.items, l.items):
                new.append(x + y)
        else:
            for index, element in enumerate(self.items):
                new.append(l.items[index] + element)
            new.extend(l.items[-index:])
        return new

    
    def __sub__(self, l: 'MyList'):
        new = []
        if len(l) < len(self):
            for index, element in enumerate(l.items):
                new.append(self.items[index] - element)
            # oder mit normler for loop
            new.extend(self.items[-index:])
        elif len(l) == len(self):
            for x, y in zip(self.items, l.items):
                new.append(x - y)
        else:
            for index, element in enumerate(self.items):
                new.append(element - l.items[index])
            # oder mit normler for loop
            new.extend([-i for i in l.items[-index:]])
        return new
    

    def __mul__(self, l: 'MyList'):
        new = []
        if len(l) < len(self):
            for index, element in enumerate(l.items):
                new.append(self.items[index] * element)
        elif len(l) == len(self):
            for x, y in zip(self.items, l.items):
                new.append(x * y)
        else:
            for index, element in enumerate(self.items):
                new.append(element * l.items[index])
        return new
    

# Addition
l1 = MyList([1, 2, 3])
l2 = MyList([3, 4])
assert l1 + l2 == [4, 6, 3]

l1 = MyList([1, 2])
l2 = MyList([3, 4])
assert l1 + l2 == [4, 6]

l1 = MyList([1, 2])
l2 = MyList([3, 4, 5])
assert l1 + l2 == [4, 6, 5]


# Subtraktion
l1 = MyList([1, 2, 3])
l2 = MyList([3, 4])
assert l1 - l2 == [-2, -2, 3]

l1 = MyList([1, 2])
l2 = MyList([3, 4])
assert l1 - l2 == [-2, -2]

l1 = MyList([1, 2])
l2 = MyList([3, 4, 5])
assert l1 - l2 == [-2, -2, -5]


# Multiplikation
l1 = MyList([1, 2, 3])
l2 = MyList([3, 4])
assert l1 * l2 == [3, 8]

l1 = MyList([1, 2])
l2 = MyList([3, 4])
assert l1 * l2 == [3, 8]

l1 = MyList([1, 2])
l2 = MyList([3, 4, 5])
assert l1 * l2 == [3, 8]
