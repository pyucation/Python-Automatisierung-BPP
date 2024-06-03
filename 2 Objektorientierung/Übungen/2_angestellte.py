"""
Aufgabe: Schreibe eine Klasse "Angestellter", welche die folgenden Attribute und Methoden besitzt:
+ name: str
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
2) Schreibe dem Angestellten 2 eine Nachricht, in der du mit der Gehaltserhöhung prahlst.
3) Versetze den Angestellten 2 danach in eine andere Abteilung (Personalnummer ändern).
"""
