class Angestellter:

    def __init__(self, name):
        # public: von überall (auch außerhalb) der Klasse zugreifbar
        self.name = name
        # protected: nur von innerhalb der Klasse und der Unterklassen zugreifbar
        self._gehalt = 50000
        # private: nur innerhalb der Klasse zugänglich
        self.__pin = "123"

    # Getter und Setter bieten einen kontrollierten Zugriff auf private und geschützte Attribute
    def get_gehalt(self):
        return self._gehalt
    
    def set_gehalt(self, neues_gehalt):
        # beispielhafte Überprüfung
        if isinstance(neues_gehalt, int):
            self._gehalt = neues_gehalt
        else:
            raise TypeError("Value must be an integer")
        
    def ueberpruefe_pin(self, pin):
        if pin == self.__pin:
            print("Success!")
        else:
            print("Wrong Pin!")
        

a1 = Angestellter("Thomas")

# public Attribut
print(a1.name)
# protected Attribut
print(a1._gehalt)
# private Attribut - Fehler!
# print(a1.__pin)

a1.ueberpruefe_pin("345")
print("_"*20)


# besser: @property Decorator verwenden
class Angestellter2:

    def __init__(self, name):
        self._name = name # jetzt auch protected
        self._gehalt = 50000
        self.__pin = "123"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Name muss ein nicht-leerer String sein.")
        self._name = value

    @property
    def gehalt(self):
        return self._gehalt
    
    @gehalt.setter
    def gehalt(self, new):
        if isinstance(new, int):
            self._gehalt = new
        else:
            raise ValueError("Value must be an integer")
        
a2 = Angestellter2("Klaus")
print(a2.gehalt)

# a2.name = 123 # Fehler!
a2.name = "Hannelore"
print(a2.name)
