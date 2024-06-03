class Auto:

    def __init__(self, marke, farbe, ps):
        self.marke = marke
        self.farbe = farbe
        self.ps = ps

    def fahren(self):
        print("Ich fahre!")


class LKW(Auto):

    def __init__(self, marke, farbe, ps, anhänger, max_ladegewicht):
        super().__init__(marke, farbe, ps)
        self.anhänger = anhänger
        self.max_ladegewicht = max_ladegewicht

    def anhänger_koppeln(self):
        if self.anhänger:
            print("Anhänger bereits vorhanden")
        else:
            self.anhänger = True


class Formel1Auto(Auto):

    def __init__(self, marke, farbe, ps, team):
        super().__init__(marke, farbe, ps)
        self.team = team

    def drs_aktivieren(self):
        print("I am speed!!")


a1 = Auto("Porsche", "grün", 360)
a1.fahren()

mein_lkw = LKW("MAN", "weiß", 500)
mein_lkw.fahren()
