"""
Aufgabe: Gegeben ist folgender Code. Ergänze ihn um ein "verbosity" Level.

    Level 0 (default): Gibt nur die Gesamtanzahl der Zeilen, Wörter und Zeichen aus.
    Level 1: Gibt zusätzlich an, welche Datei gezählt wurde.
    Level 2: Gibt detaillierte Informationen zu den einzelnen Schritten
    des Zählens aus (z.B. "Counting lines...", "Counting words...", "Counting characters...").
"""
import argparse


def count_lines(file):
    return len(file.readlines())

def count_words(file):
    file.seek(0)
    return len(file.read().split())


def count_chars(file):
    file.seek(0)
    return len(file.read())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zähle Zeilen, Wörter und Zeichen in einem File.")

    parser.add_argument("filename", help="The file to count.")
    args = parser.parse_args()

    with open(args.filename, 'r') as file:
        lines = count_lines(file)
        words = count_words(file)
        chars = count_chars(file)

    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {chars}")
