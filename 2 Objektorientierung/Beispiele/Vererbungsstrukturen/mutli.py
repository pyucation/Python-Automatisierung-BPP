# Achtung: Diamond-Problem möglich bei Multi-Vererbung!!

class Tier:

    def __init__(self, farbe) -> None:
        self.farbe = farbe

    def atmen(self):
        print("Ich atme.")


class Vogel:

    def __init__(self, kann_fliegen):
        self.kann_fliegen = kann_fliegen

    def abheben(self):
        if self.kann_fliegen:
            print("Ich hebe ab.")
        else:
            print("Ich kann nicht fliegen :(")


class Pinguin(Tier, Vogel):

    def __init__(self, kann_fliegen, farbe):
        Tier.__init__(farbe)
        Vogel.__init__(kann_fliegen)

    def tauchen(self):
        self.atmen()
        print("ich tauche ab ...")
