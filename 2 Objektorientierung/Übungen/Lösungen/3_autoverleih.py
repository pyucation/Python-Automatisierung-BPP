"""
Aufgabe:
Du entwickelst ein Verwaltungssystem für eine Autovermietung. Diese Autovermietung
hat Trucks und Cars (normale Autos) im Sortiment. Schreibe eine Basisklasse
"Vehicle" mit den Attributen:
+ Marke
+ Modell
+ Baujahr
Außerdem soll es ein Attribut geben, welches ALLE Fahrzeuge zählt, die erstellt werden.

Die Klasse "Car" erbt von "Vehicle" und hat folgende Attribute:
+ Marke
+ Modell
+ Baujahr
+ Anzahl Türen

Die Klasse "Truck" erbt ebenfalls von "Vehicle" und hat folgende Attribute:
+ Marke
+ Modell
+ Baujahr
+ Maximales Ladegewicht


Jede Klasse hat eine Methode "description", welche spezifische Informationen zu einer
Instanz ausgibt. Implementiere diese Methode für die Basisklasse "Vehicle" und
überschreibe sie in den Kinder-Klassen.
"""

class Vehicle:
    vehicle_count = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Vehicle.vehicle_count += 1

    def description(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        # Aufruf des Konstruktors der Basisklasse
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def description(self):
        # Aufruf der Methode der Basisklasse
        base_description = super().description()
        return f"{base_description}, {self.number_of_doors} doors"

class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        # Aufruf des Konstruktors der Basisklasse
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def description(self):
        # Aufruf der Methode der Basisklasse
        base_description = super().description()
        return f"{base_description}, {self.payload_capacity} tons payload capacity"


car1 = Car("Toyota", "Corolla", 2020, 4)
truck1 = Truck("Volvo", "FH16", 2018, 25)

print(car1.description())
print(truck1.description())

print(f"Total number of vehicles: {Vehicle.vehicle_count}")
