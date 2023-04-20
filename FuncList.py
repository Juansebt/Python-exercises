#Función que recibe una lista de números y devuelve los números al cuadrado
def numCuadrados(numeros):
    cuadrados = []
    cantLista = len(numeros)
    
    for i in range(cantLista):
        cuadrados.append(numeros[i]**2)
    return cuadrados

listaCuadrados = numCuadrados([7,8,9,9,4,5,6,1])
print(listaCuadrados)