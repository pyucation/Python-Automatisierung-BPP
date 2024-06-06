"""
Aufgabe: Schreibe eine einfache grafische Benutzeroberfläche (GUI) mit Tkinter,
die es Benutzern ermöglicht, Aufgaben zu einer To-Do-Liste hinzuzufügen und die
hinzugefügten Aufgaben in einer Liste anzuzeigen.

Hinweis: Verwende "listbox" oder "label" zum Darstellen der Aufgaben.
"""
import tkinter as tk
import os


root = tk.Tk()

root.title("Meine To-Do-Liste")
root.geometry("400x500")

todos = []

# Hinzufügen einer Aufgabe zur Liste
def add_task():
    # überprüfen, ob das Eingabefeld nicht leer ist
    task = entry.get().strip()
    if task:
        # Aufgabe zur Listbox hinzufügen
        listbox.insert(tk.END, task)
        todos.append(task)
        # Leeren des Eingabefelds nach dem Hinzufügen
        entry.delete(0, tk.END)

# Löschen der zuletzt hinzugefügten Aufgabe
def delete_task():
    try:
        index = listbox.curselection()[0]
        # zuletzt ausgewählten Eintrag löschen
        listbox.delete(index)
        # TODO: alte todos in Datei speichern
        todos.pop(index)
    except:
        # falls kein Eintrag ausgewählt, wird nichts gemacht
        pass

def exit_todo():
    print(todos)
    with open("meine_todos.txt", "w", encoding="utf-8") as f:
        for todo in todos:
            f.write(todo + "\n")
    exit()

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

if os.path.exists("meine_todos.txt"):
    with open("meine_todos.txt", "r") as f:
        for todo in f:
            # strip() nutzen, um den Whitespace zu entfernen
            todo = todo.strip()
            listbox.insert(tk.END, todo)
            todos.append(todo)

# Button zum Beenden und Speichern der übrigen Todos
exit_button = tk.Button(root, text="Exit", command=exit_todo)
exit_button.pack(pady=10)

# Event-Schleife
root.mainloop()
