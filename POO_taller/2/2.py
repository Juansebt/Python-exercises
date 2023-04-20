"""
Existen 3 tipos de Animales así: Los peces que pueden Nadar y Respirar; los perros que pueden
Ladrar y Respirar; los gatos que pueden Maullar y Respirar. Para cada cada uno de los animales
se tiene el registro de peso en Kg.
"""
from Gato import Gato
from Perro import Perro
from Pez import Pez

print("-----------------------------")

miGato = Gato(7)
miGato.Maullar()
miGato.Respirar()
print(f"{type(miGato).__name__} tiene un peso de: {miGato.getPeso()}Kg")
print("-----------------------------")

miPerro = Perro(14)
miPerro.Ladrar()
miPerro.Respirar()
print(f"{type(miPerro).__name__} tiene un peso de: {miPerro.getPeso()}Kg")
print("-----------------------------")

miPez = Pez(3)
miPez.Nadar()
miPez.Respirar()
print(f"{type(miPez).__name__} tiene un peso de: {miPez.getPeso()}Kg")
print("-----------------------------")
