"""
Aufgabe: Sie haben eine Klasse Person in einem älteren Python-Programm, die
Informationen über Personen verwaltet. Diese Klasse verwendet direkten Zugriff
auf die Attribute, was nicht ideal ist, da es keine Kontrolle über die Werte
gibt, die diesen Attributen zugewiesen werden. Ihre Aufgabe ist es, die Klasse
zu modernisieren, indem Sie den @property Decorator und die entsprechenden
Setter-Methoden verwenden, um eine Validierung und möglicherweise eine Formatierung
für die Attribute name und alter hinzuzufügen.

Hinweis: Die Funktion isinstance könnte hilfreich sein.
"""
class Person:
    def __init__(self, name, alter):
        self._name = name
        self._alter = alter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Name muss ein nicht-leerer String sein.")
        self._name = value

    @property
    def alter(self):
        return self._alter

    @alter.setter
    def alter(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Alter muss eine positive Ganzzahl sein.")
        self._alter = value


try:
    p = Person("Max", 30)
    print(p.name, p.alter)
    p.name = ""  # sollte eine Exception auslösen
except ValueError as e:
    print(e)

try:
    p.alter = -5  # sollte eine Exception auslösen
except ValueError as e:
    print(e)

