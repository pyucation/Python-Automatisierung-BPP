"""
Aufgabe:
Schreibe eine einfache grafische Benutzeroberfläche (GUI) mit Tkinter, die es
Benutzern ermöglicht, Beträge von Euro in US-Dollar umzurechnen. Das Programm
sollte einfach zu bedienen sein und die Grundfunktionen der Datenverarbeitung
mit Tkinter nutzen.
"""
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()

root.title("Währungsrechner")
root.geometry("300x200")

# Umrechnen von Euro in US-Dollar
def convert_currency():
    try:
        # TODO: dein Code hier
        ...
    except ValueError:
        # Fehlermeldung anzeigen, wenn die Eingabe keine gültige Zahl ist
        messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Zahl ein")

# TODO: ... hier muss auch noch Code stehen

root.mainloop()
