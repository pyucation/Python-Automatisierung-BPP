"""
Aufgabe: Schreibe eine einfache grafische Benutzeroberfläche (GUI) mit Tkinter,
die es Benutzern ermöglicht, Aufgaben zu einer To-Do-Liste hinzuzufügen und die
hinzugefügten Aufgaben in einer Liste anzuzeigen.

Hinweis: Verwende "listbox" oder "label" zum Darstellen der Aufgaben.
"""
import tkinter as tk


root = tk.Tk()

root.title("Meine To-Do-Liste")
root.geometry("400x300")

# Hinzufügen einer Aufgabe zur Liste
def add_task():
    # überprüfen, ob das Eingabefeld nicht leer ist
    task = entry.get().strip()
    if task:
        # Aufgabe zur Listbox hinzufügen
        listbox.insert(tk.END, task)
        # Leeren des Eingabefelds nach dem Hinzufügen
        entry.delete(0, tk.END)

# Löschen der zuletzt hinzugefügten Aufgabe
def delete_task():
    try:
        # zuletzt ausgewählten Eintrag löschen
        listbox.delete(listbox.curselection()[0])
    except:
        # falls kein Eintrag ausgewählt, wird nichts gemacht
        pass

# Eingabefeld
entry = tk.Entry(root)
entry.pack(pady=10)

# Button zum Hinzufügen
add_button = tk.Button(root, text="Hinzufügen", command=add_task)
add_button.pack(pady=5)

# Button zum Löschen
delete_button = tk.Button(root, text="Löschen", command=delete_task)
delete_button.pack(pady=5)

# Listbox zur Anzeige der Aufgaben
listbox = tk.Listbox(root)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Event-Schleife
root.mainloop()
