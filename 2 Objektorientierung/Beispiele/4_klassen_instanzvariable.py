# ohne Klassenvariable
class Angestellter:

    def __init__(self, name, abteilung, personalnr, unternehmen):
        self.name = name
        self.abteilung = abteilung
        self.personalnr = personalnr
        self.unternehmen = unternehmen


a1 = Angestellter("Klaudia", "IT", 47628, "Python-Firma")
a2 = Angestellter("Gerhard", "HR", 84921, "Python-Firma")


# besser
class Angestellter2:
    unternehmen = "Python-Firma"

    def __init__(self, name, abteilung, personalnr):
        self.name = name
        self.abteilung = abteilung
        self.personalnr = personalnr

a3 = Angestellter2("Tobias", "Produktion", 99281)
print(a3.unternehmen == a2.unternehmen)

print("_"*20)
# weitere Beispiele

# Zähler
class Dog:
    num_of_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.num_of_dogs += 1

dog1 = Dog("Buddy")
dog2 = Dog("Rex")

print(Dog.num_of_dogs)


# Konfigurationen
class Config:
    database_url = "localhost"

    def __init__(self, user):
        self.user = user

config1 = Config("user1")
config2 = Config("user2")

print(config1.database_url)
print(config2.database_url)

Config.database_url = "remotehost"
print(config1.database_url)
print(config2.database_url)
