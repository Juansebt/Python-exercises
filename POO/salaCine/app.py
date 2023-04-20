from Modelo.Sala import Sala
from Modelo.Persona import Persona
import datetime
import os

miSala = Sala("SENA", 2)

def ingresoSala():
    print("\n\tRegistrar ingreso a la sala\n")
    id = input("\tIngrese la identificación de la persona : ")
    nombre = input("\tIngrese el nombre de la persona : ")
    correo = input("\tIngrese el correo electronico de la persona : ")
    genero = input("\tIngrese el genero de la persona (Femenino / Masculino) : ").upper()
    estado,mensaje=miSala.registrarIngreso(id, nombre, correo, genero)
    print(mensaje)
    
def consultarSilla():
    print("\n\tConsultar silla\n")
    num = int(input(f"\tIngrese el número de silla a consultar de 1 a {miSala.getCantidadSillas()} : "))
    persona = miSala.obtenerDatosPersonaSilla(num)
    
    if(type(persona) == Persona):
        print(f"\tDatos de la persona ubicada en la silla número: {num}")
        print(f"\tIdentificación: {persona.getIdentificacion()}")
        print(f"\tNombre: {persona.getNombre()}")
        print(f"\tCorreo: {persona.getCorreo()}")
        print(f"\tGenero: {persona.getGenero()}")
    else:
        print(persona)
    
def cantidadPersonasGenero():
    print("\n\tCantidad de mujeres y hombres en la sala\n")
    mujeres, hombres = miSala.obtenerCantidadMujeresHombres()
    print(f"\tCantidad mujeres: {mujeres}")
    print(f"\tCantidad hombres: {hombres}")

def datosPersonaSala():
    print("\n\tDatos de las personas que estan en la sala\n")
    for ingreso in miSala.getListaIngresos():
        print(f"\tNombre: {ingreso.getPersona().getNombre()}")
        print(f"\tSilla: {ingreso.getSilla().getNumeroSilla()}")
        print(f"\tFecha ingreso: {ingreso.getFechaHora().strftime('%x')}")
        print(f"\tHora ingreso: {ingreso.getFechaHora().strftime('%X')}")
        print("-"*50)
    
def menu():
    while(True):
        os.system("cls")
        print(f"\t\tGESTIÓN SALA {miSala.getNombre()}")
        print("\t1. Registrar ingreso sala")
        print("\t2. Consultar silla")
        print("\t3. Cantidad personas genero")
        print("\t4. Datos personas en sala")
        print("\t5. Salir")
        opcion = int(input("\tIngrese opcion: "))
        if(opcion == 1):
            ingresoSala()
        elif(opcion == 2):
            consultarSilla()
        elif(opcion == 3):
            cantidadPersonasGenero()
        elif(opcion == 4):
            datosPersonaSala()
        elif(opcion == 5):
            print("\n\tSaliendo...")
            break
        else:
            print("\n\tOpción no valida...")
            
        input("\n\tPresiones ENTER para continuar")
        
menu()