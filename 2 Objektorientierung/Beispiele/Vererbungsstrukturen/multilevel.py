class Person:

    def __init__(self, name, geburtstag):
        self.name = name
        self.geburtstag = geburtstag

    def feiere_geburtstag(self, datum):
        if datum == self.geburtstag:
            print("Happy Birthday!")


class Angestellter(Person):

    def __init__(self, name, geburtstag, personalnr, gehalt):
        super().__init__(name, geburtstag)
        self.personalnr = personalnr
        self.gehalt = gehalt

    def get_email(self):
        return f"{self.name}-{self.personalnr}@firma.de"
    

class ITMitarbeiter(Angestellter):

    def __init__(self, name, geburtstag, personalnr, gehalt, admin_rechte):
        super().__init__(name, geburtstag, personalnr, gehalt)
        self.admin_rechte = admin_rechte

    def bringe_system_zum_absturz(self):
        if self.admin_rechte:
            print(f"{self.personalnr} schickt euch in den Feierabend")
            