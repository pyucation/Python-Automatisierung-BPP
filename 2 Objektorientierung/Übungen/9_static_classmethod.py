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
    ...


hr_string_manager = "Alfred-Vorstand-80000-17"
datum = datetime.date(2016, 7, 10)
