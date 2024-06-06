import tkinter as tk


# Hauptfensters erstellen
root = tk.Tk()

# Fenstertitel
root.title("Einfache Tkinter App")

# Fenstergröße
root.geometry("300x150")

# Funktion, die aufgerufen wird, wenn der Button geklickt wird
def on_button_click():
    # Übernahme des Textes aus dem Eingabefeld
    input_text = entry.get()
    # Aktualisieren des Labels mit dem Text aus dem Eingabefeld
    label.config(text="Du hast geschrieben: " + input_text)

# Eingabefeld erstellen und Positionieren im Fenster
entry = tk.Entry(root)
entry.pack(pady=10)

# Button, der beim Klicken die Funktion 'on_button_click' aufruft
button = tk.Button(root, text="Bestätigen", command=on_button_click)
button.pack(pady=10)

# Label zur Anzeige von Text und Positionieren im Fenster
label = tk.Label(root, text="Hier erscheint der Eingabetext")
label.pack(pady=10)

# Event-Schleife starten
root.mainloop()
