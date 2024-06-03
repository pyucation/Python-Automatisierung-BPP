"""
Aufgabe: Schreibe eine Klasse "Manager" mit folgenden Attributen und Methoden:
+ erhoehungsfaktor: 1.04 (gleich für alle Instanzen von "Manager")
+ name: str
+ abteilung: str
+ grundgehalt: int
+ betriebszugehörigkeit: int        # in Jahren
+ loyalitaets_bonus: int            # errechnet sich durch Betriebszugehörigkeit * 200

+ erhoehe_gehalt()                  # erhöht das Grundgehalt um den erhoehungsfaktor
+ erhalte_gehalt()                  # gibt das volle Jahresgehalt zurück
+ ist_arbeitstag()                  # erwartet ein Datum als Parameter und prüft, ob es ein
                                    # Arbeitstag für einen Manager ist oder nicht
                                    # Hinweis: https://www.geeksforgeeks.org/python-datetime-weekday-method-with-example/
+ from_string()                     # bekommt einen String von der Personalabteilung und
                                    # soll daraus eine Manager-Instanz erstellen
"""
import datetime

class Manager:

    erhoehungsfaktor = 1.04

    def __init__(self, name, abteilung, grundgehalt, betriebszugehoerigkeit):
        self.name = name
        self.abteilung = abteilung
        self.grundgehalt = grundgehalt
        self.betriebszugehoerigkeit = betriebszugehoerigkeit
        self.loayalitaets_bonus = self.betriebszugehoerigkeit * 200

    def erhoehe_gehalt(self):
        self.grundgehalt *= self.erhoehungsfaktor

    def erhalte_gehalt(self):
        return self.grundgehalt + self.loayalitaets_bonus

    @classmethod
    def from_string(cls, manager_str):
        name, abteilung, grundgehalt, betriebszugehoerigkeit = manager_str.split("-")
        return cls(name, abteilung, int(grundgehalt), int(betriebszugehoerigkeit))

    @staticmethod
    def ist_arbeitstag(datum):
        if datum.weekday() == 5 or datum.weekday() == 6:
            return False
        return True



m1 = Manager("Timo", "Produktion", 50000, 2)
m2 = Manager("Anna", "IT", 55000, 4)

hr_string_manager = "Alfred-Vorstand-80000-17"
datum = datetime.date(2016, 7, 10)

print(Manager.ist_arbeitstag(datum))
m3 = Manager.from_string(hr_string_manager)
print(m3.erhalte_gehalt())
