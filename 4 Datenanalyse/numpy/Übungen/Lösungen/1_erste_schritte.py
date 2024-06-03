"""
Aufgabe:
    1. Array Erstellung:
        Erstelle ein NumPy Array aus einer Python-Liste mit den Werten [5, 10, 15, 20, 25].
        Konvertiere die Liste [[1, 2, 3], [4, 5, 6], [7, 8, 9]] in ein 2D NumPy Array und gib es aus.

    2. Array-Attribute:
        Überprüfe die Dimension, Form und Größe des in Aufgabe 1 erstellten 2D Arrays.

    3. Spezielle Arrays:
        Erstelle ein Array mit Nullen der Größe 3x3.
        Erstelle ein Array mit Einsen der Größe 2x2.
        Erstelle ein Einheitsmatrix (Identity Matrix) der Größe 4x4.

    4. Array Manipulation:
        Ändere das erste Element des aus der Liste erstellten Arrays zu 100.
        Multipliziere jedes Element des 2D Arrays mit 2 und gib das resultierende Array aus.

    5. Berechnungen mit Arrays:
        Berechne die Summe aller Elemente in dem 2D Array.
        Berechne den Durchschnitt der Werte im ursprünglichen 1D Array.

    Zusatz: Verwende eine Bedingung, um alle Elemente des 2D Arrays zu filtern,
    die größer als 5 sind.
"""
import numpy as np

# 1.
# Erstelle ein NumPy Array aus einer Liste
array1 = np.array([5, 10, 15, 20, 25])
print(array1)

# Konvertiere die Liste in ein 2D NumPy Array
list2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2d = np.array(list2d)
print(array2d)


# 2.
# Überprüfe die Dimension, Form und Größe des 2D Arrays
print("Dimension:", array2d.ndim)
print("Form:", array2d.shape)
print("Größe:", array2d.size)


# 3.
# Erstelle ein Array mit Nullen
zeros_array = np.zeros((3, 3))
print(zeros_array)

# Erstelle ein Array mit Einsen
ones_array = np.ones((2, 2))
print(ones_array)

# Erstelle eine Einheitsmatrix
identity_matrix = np.eye(4)
print(identity_matrix)


# 4.
# Ändere das erste Element des ersten Arrays zu 100
array1[0] = 100
print(array1)

# Multipliziere jedes Element des 2D Arrays mit 2
array2d_multiplied = array2d * 2
print(array2d_multiplied)


# 5.
# Berechne die Summe aller Elemente im 2D Array
sum_2d = array2d.sum()
print("Summe aller Elemente:", sum_2d)

# Berechne den Durchschnitt der Werte im ursprünglichen 1D Array
average_1d = array1.mean()
print("Durchschnitt der Werte:", average_1d)


# Zusatz
# Filtere alle Elemente des 2D Arrays, die größer als 5 sind
filtered_elements = array2d[array2d > 5]
print(filtered_elements)
