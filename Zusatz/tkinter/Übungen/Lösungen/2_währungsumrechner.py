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
        # Betrag aus dem Eingabefeld lesen und in float type casten
        euro_amount = float(euro_entry.get())
        conversion_rate = 1.10
        dollar_amount = euro_amount * conversion_rate
        # Anzeigen des Ergebnisses im Label
        result_label.config(text=f"{euro_amount} Euro sind {dollar_amount:.2f} US-Dollar")
    except ValueError:
        # Fehlermeldung anzeigen, wenn die Eingabe keine gültige Zahl ist
        messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Zahl ein")

# Eingabefeld für Euro-Betrag
entry_label = tk.Label(root, text="Eingabe in Euro (z.B. 1.20):")
entry_label.pack(pady=10)
euro_entry = tk.Entry(root)
euro_entry.pack(pady=10)

# Button zur Umrechnung
convert_button = tk.Button(root, text="Umrechnen", command=convert_currency)
convert_button.pack(pady=5)

# Label zur Anzeige des Ergebnisses
result_label = tk.Label(root, text="Ergebnis wird hier angezeigt")
result_label.pack(pady=10)

root.mainloop()
