"""
La empresa de Aviacion XYZ (Qatar Airways) quiere tener un Registro de los vuelos diarios con la siguiente
información: número de vuelo, fecha, ciudad origen del vuelo, ciudad destino del vuelo, listado
de pasajeros. 
"""
from Empresa import Empresa

import os

opcion = 0

Aerolinea = Empresa("Avianca")

def registrarVuelo():
    numeroVuelo = input("\tIngrese el número del vuelo: ")
    fecha = input(f"\tIngrese la fecha del vuelo {numeroVuelo} (dd/mm/yyyy): ")
    ciudadOrigen = input(f"\tIngrese ciudad de origen del vuelo {numeroVuelo}: ")
    ciudadDestino = input(f"\tIngrese la ciudad del destino del vuelo {numeroVuelo}: ")
    Aerolinea.registrarVuelo(numeroVuelo,fecha,ciudadOrigen,ciudadDestino)
    print("\n\tVuelo registrado con exito")
    
def agregarPasajero(numVuelo,nombre,identificacion,edad):
    for vuelo in Aerolinea.getListaVuelos():
        if (vuelo.getNumeroVuelo() == numVuelo):
            vuelo.agregarPasajero(nombre,identificacion,edad)
            print("\n\tPasajero agregado correctamente")
            break
    else:
        print("\tEl vuelo al que se va a registrar el pasajero no existe...")
    
def listarVuelos():
    for vuelo in Aerolinea.getListaVuelos():
        numVuelo = vuelo.getNumeroVuelo()
        fechaVuelo = vuelo.getFecha()
        ciudadOrigen = vuelo.getCiudadOrigen()
        ciudadDestino = vuelo.getCiudadDestino()
        print(f"\tNúmero de vuelo: {numVuelo}\n\tFecha del vuelo: {fechaVuelo}\n\tCiudad de origen del vuelo: {ciudadOrigen}\n\tCiudad de destino del vuelo: {ciudadDestino}\n")
            
def listarPasajeros():
    numVuelo = input("\tIngrese el número del vuelo a consultar: ")
    for vuelo in Aerolinea.getListaVuelos():
        if (vuelo.getNumeroVuelo() == numVuelo):
            print(f"\n\tLista de pasajeros del  vuelo número {numVuelo}:")
            for pasajero in vuelo.getListaPasajeros():
                Nombre = pasajero.getNombre()
                Id = pasajero.getIdentificacion()
                edad = pasajero.getEdad()
                print(f"\n\tNombre: {Nombre}\n\tIdentificación: {Id}\n\tEdad del pasajero: {edad}\n")
                break
        else:
            print("\tNo existe un vuelo con ese número!")


def menu():
    print("---------------------------------------------------------------")
    print(f"\t\tGestión de vuelos {Aerolinea.getNombre().upper()}")
    print("---------------------------------------------------------------")
    print("\t1. Registrar vuelo \n\t2. Agregar pasajero \n\t3. Listar vuelos \n\t4. Listar pasajeros \n\t5. Salir")
    print("---------------------------------------------------------------")
    opc = int(input("\t\tIngrese opción: "))
    print("---------------------------------------------------------------")
    return opc

while opcion != 5:
    os.system("cls")
    opcion = menu()
    if (opcion == 1):
        print("\tREGISTRAR VUELO:\n")
        registrarVuelo()
    elif (opcion == 2):
        print("\tAGREGAR PASAJERO:\n")
        numVuelo = input("\tIngrese el númerod del vuelo a agregar el pasajero: ")
        nombre = input("\tIngrese el nombre del pasajero: ")
        identificacion = input("\tIngrese la identificación del pasajero: ")
        edad = int(input("\tIngrese la edad del pasajero: "))
        agregarPasajero(numVuelo,nombre,identificacion,edad)
    elif (opcion == 3):
        print("\tLISTA DE VUELOS DISPONIBLES:\n")
        listarVuelos()
    elif (opcion == 4):
        print("\tLISTA DE PASAJEROS:\n")
        listarPasajeros()
    elif (opcion == 5):
        print("\t\tSaliendo...")
        print("---------------------------------------------------------------")
    else:
        print("\t\tIngresa una opción válida")
        
    input("\n\tPresione ENTER para continuar")

