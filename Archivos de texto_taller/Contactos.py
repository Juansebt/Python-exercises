import os

opcion = 0

def menu():
    print("\t\tGESTIÓN DE CONTACTOS")
    print("\t1. Agregar \n\t2. Consultar por identificación \n\t3. Listar contactos \n\t4. Salir")
    opc = int(input("\t\tIngrese opción: "))
    return opc

def agregarContacto(ID, nombres, apellidos, correo, genero):
    try:
        archivo = open("Contactos.txt","a",encoding="utf-8")
        archivo.write(f"{ID} - ")
        archivo.write(f"{nombres} - ")
        archivo.write(f"{apellidos} - ")
        archivo.write(f"{correo} - ")
        archivo.write(f"{genero}\n")
        print("\n\tContacto agregado\n")
        archivo.close()
    except IOError as error:
        print(error.strerror)

def consultarPorID(ID):
    #archivo = open("Contactos.txt","r",encoding="utf-8")
    with open("Contactos.txt","r",encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        existe = False
        for linea in lineas:
            palabras = linea.strip("\n").split(" - ")
            for palabra in palabras:
                if (palabra == ID):
                    nombres = palabras[1]
                    apellidos = palabras[2]
                    correo = palabras[3]
                    genero = palabras[4]
                    print(f"\n\tNombres: {nombres}\n\tApellidos: {apellidos}\n\tCorreo: {correo}\n\tGenero: {genero}\n")
                    existe = True
                    break
            if (existe):
                break
        if (not existe):
            print("\tNo hay ningún contacto con esa identificación\n")
    
def listarContactos():
    archivo = open("Contactos.txt","r",encoding="utf-8")
    lineas = archivo.readlines()
    i = 0
    for linea in lineas:
        #print(linea)
        palabras = linea.strip("\n").split(" - ")
        i += 1
        identificacion = palabras[0]
        nombres = palabras[1]
        apellidos = palabras[2]
        correo = palabras[3]
        genero = palabras[4]
        print(f"\tContacto {i}:")
        print(f"\n\tIdentifición: {identificacion}\n\tNombres: {nombres}\n\tApellidos: {apellidos}\n\tCorreo: {correo}\n\tGenero: {genero}\n")
                    
while opcion != 4:
    opcion = menu()
    if (opcion == 1):
        print("\n\tAGREGAR CONTACTO:\n")
        nombres = input("\tIngrese los nombres del contacto: ")
        apellidos = input("\tIngrese los apellidos de contacto: ")
        Id = input(f"\tIngrese la identificación de {nombres} {apellidos}: ")
        correo = input(f"\tIngrese el correo electrónico de {nombres} {apellidos}: ")
        genero = input(f"\tIngrese el genero (Masculino-Femenino): ")
        agregarContacto(Id,nombres,apellidos,correo,genero)
        
    elif (opcion == 2):
        print("\n\tCONSULTAR POR IDENTIFICACIÓN:\n")
        Id = input("\tIngrese la identificación del contacto: ")
        consultarPorID(Id)
        
    elif (opcion == 3):
        print("\n\tLISTAR CONTACTOS:\n")
        listarContactos()

    elif (opcion == 4):
        print("\n\t\tSaliendo...\t\n")
        
    else:
        print("\n\t\tIngresa una opción válida")