import tkinter as tk


# Hauptklasse für unsere Anwendung, die von tk.Tk abgeleitet ist.
class SimpleApp(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Einfache Tkinter App")

        self.geometry("300x200")

        self.label = tk.Label(self, text="Hallo, Tkinter!")
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Klick mich", command=self.on_button_click)
        self.button.pack(pady=20)

    def on_button_click(self):
        # Text des Labels ändern
        self.label.config(text="Button wurde geklickt!")


if __name__ == "__main__":
    app = SimpleApp()
    app.mainloop()
