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
        self.name = name
        self.alter = alter
