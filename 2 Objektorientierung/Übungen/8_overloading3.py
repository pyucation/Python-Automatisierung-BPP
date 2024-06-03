"""
Aufgabe:
Stell dir vor du schreibst eine Quiz-Anwendung bei der du mit automatisierten Tests, die dein
Freund geschrieben hat, die Lösungen der Teilnehmer evaluieren willst.
Folgender Code ist gegeben. Schreibe eine Klasse "MyStr", welche bei einem Vergleich immer True
liefert und damit jedes Mal volle Punktzahl im Quiz gibt, unabhängig von der Antwort.

Hinweis: Nutze die __eq__ Methode.
"""

class MyStr:
    ...

# Frage 1: Wie heißt die Hauptstadt Deutschlands?
richtige_antwort = "Berlin"
antwort_teilnehmer = "München"

if richtige_antwort == antwort_teilnehmer:
    print("Richtig!")
else:
    print("Leider falsch!")

# mit eigener Klasse MyStr
richtige_antwort = MyStr("Berlin")
antwort_teilnehmer = MyStr("München")

if richtige_antwort == antwort_teilnehmer:
    print("Richtig!")
else:
    print("Leider falsch!")