"""
Aufgabe:
Entwickelt eine einfache grafische Benutzeroberfläche (GUI) mit Tkinter, die es
Benutzern ermöglicht, Kontaktdaten (Name und Telefonnummer) zu einem
Adressbuch hinzuzufügen, diese anzuzeigen und einzelne Einträge zu löschen.
"""

import tkinter as tk
from tkinter import messagebox


root = tk.Tk()

root.title("Mein Adressbuch")
root.geometry("400x400")

# Liste zum Speichern der Kontakte
contacts = []

# Hinzufügen eines Kontakts
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    # überprüfen, ob beide Felder ausgefüllt sind
    if name and phone:
        contacts.append((name, phone))
        update_display()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Fehler", "Beide Felder müssen ausgefüllt sein")

# Aktualisieren der angezeigten Kontakte
def update_display():
    # tk.END ist eine Konstante, die das Ende eines Widgets angibt
    # also hier: lösche alle Einträge von Beginn an (0) bis Ende
    listbox.delete(0, tk.END)
    # füge dann alle Kontakte hinzu
    for name, phone in contacts:
        listbox.insert(tk.END, f"{name} ----- {phone}")

# Löschen eines ausgewählten Kontakts
def delete_contact():
    try:
        # Index des aktuell ausgewählten Eintrags speichern
        index = listbox.curselection()[0]
        listbox.delete(index)
        del contacts[index]
    except IndexError:
        messagebox.showerror("Fehler", "Bitte wählen Sie einen Kontakt zum Löschen aus")

# Funktion zur Filterung der Kontaktliste
def filter_contacts():
    filter_text = search_entry.get().strip().lower()
    filtered_contacts = [(name, phone) for name, phone in contacts if filter_text in name.lower()]
    listbox.delete(0, tk.END)
    for name, phone in filtered_contacts:
        listbox.insert(tk.END, f"{name}: {phone}")

# Eingabefelder für Name und Telefonnummer
name_label = tk.Label(root, text="Name:")
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)
phone_label = tk.Label(root, text="Telefonnummer:")
phone_label.pack(pady=5)
phone_entry = tk.Entry(root)
phone_entry.pack(pady=5)

# Buttons zum Hinzufügen und Löschen von Kontakten
add_button = tk.Button(root, text="Hinzufügen", command=add_contact)
add_button.pack(pady=5)
delete_button = tk.Button(root, text="Löschen", command=delete_contact)
delete_button.pack(pady=5)

# Suchfeld zur Filterung der Kontaktliste
search_entry = tk.Entry(root)
search_entry.pack(pady=5)
search_button = tk.Button(root, text="Suchen", command=filter_contacts)
search_button.pack(pady=5)

# Listbox zur Anzeige der Kontakte
listbox = tk.Listbox(root)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
