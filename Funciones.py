#Funciones:
def mensaje():
    print("Hola mundo...")
    
def cuadrado(x):
    return x * x

def operaciones(n):
    y = n * n + 1
    z = n / 2
    return y, z

def persona(identifica="Pedro",apellido="Rojas",edad=15):
    print(identifica,apellido,edad)

#nombre, apellido, edad = "Juan", "Laguna", 18

valor = mensaje()
print(valor)

c = cuadrado(8)
print(c)

a,b = operaciones(9)
print(a,b)

persona(identifica="Andrés",apellido="Quintero",edad=18)