"""
Aufgabe: Schreibe eine Klasse "Angestellter", welche die folgenden Attribute und Methoden besitzt:
+ vornamename: str
+ nachname: str
+ alter: int
+ jahresgehalt: int
+ personalnummer: int
+ postfach: list

+ erhoehe_gehalt(faktor: float) -> None
+ aendere_personalnummer(nummer: int) -> None
+ get_email() -> str
+ sende_nachricht(empfaenger: Angestellter, inhalt: str) -> None
+ empfange_nachricht(inhalt: str) -> int    # Rückgabe kann auch None sein, aber häufig verwendet man
sogenannte Statuscodes (200 = erfolgreich), um den Erfolg zu überprüfen (bekanntester: 404)

Erstelle anschließend zwei Angestellte.
1) Erhöhe das Gehalt vom Angstellten 1 um 4%.
2) Lass dir von beiden Angestellten die Email-Adresse ausgeben.
3) Schreibe dem Angestellten 2 eine Nachricht, in der du mit der Gehaltserhöhung prahlst.
4) Versetze den Angestellten 2 danach in eine andere Abteilung (Personalnummer ändern).
"""

class Angestellter:

    def __init__(self, vorname, nachname, alter, jahresgehalt, personalnummer):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.jahresgehalt = jahresgehalt
        self.personalnummer = personalnummer
        self.postfach = []

    # erhöht/verringert das Jahresgehalt um einen Faktor, -1 <= faktor <= 1
    def erhoehe_gehalt(self, faktor):
        self.jahresgehalt *= 1 + faktor

    # ändert die Personalnummer
    def aendere_personalnummer(self, nummer):
        self.personalnummer = nummer

    # liefert die Email-Adresse des Empfängers
    def get_email(self):
        return f"{self.vorname}.{self.nachname}@beispielfirma.de"

    # sendet eine Nachricht an den "empfaenger" mit dem Inhalt "inhalt"
    def sende_nachricht(self, empfaenger, inhalt):
        return empfaenger.empfange_nachricht(inhalt)

    # fügt eine empfangene Nachricht zum Postfach hinzu
    def empfange_nachricht(self, inhalt):
        # hier könnte man eine Fehlerbehandlung machen
        # aber wir wollen es nicht unnötig kompliziert machen
        self.postfach.append(inhalt)
        return 200


if __name__ == "__main__":
    a1 = Angestellter("Peter", "Müller", 29, 49000, 92376)
    a2 = Angestellter("Hans", "Klausen", 48, 65000, 28492)

    # 1)
    a1.erhoehe_gehalt(0.04)
    print(a1.jahresgehalt)

    # 2)
    print(a1.get_email())
    print(a2.get_email())

    # 3)
    msg = "Hallo Hans, schau mal meine geile Gehaltserhöhung an!"
    status = a1.sende_nachricht(a2, msg)
    if status == 200:
        print("Erfolgreich gesendet")
        print(a2.postfach)
    else:
        print("Ein Fehler ist aufgetreten.")

    # 4)
    a2.aendere_personalnummer(72894)
    print(a2.personalnummer)
