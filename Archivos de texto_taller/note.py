import os

archivo = None
contactos = []

def crearArchivo():
    """_summary_:Crea el archivo note.txt sino existe
    """
    if(not os.path.exists("note.txt")):
        archivo = open("note.txt","w",encoding="utf-8")
        
def existeContacto(identificacion, correo):
    """_summary_:Función que verifica si ya existe un contacto de acuerdo
                a la identificación o correo

    Args:
        identificacion (_type_): número de documento de identidad
        correo (_type_): correo electronico del contacto

    Returns:
        _type_: verdadero o falso
    """
    existe = False
    for contacto in contactos:
        if (contacto[0] == identificacion or contacto[3] == correo):
            existe = True
            break
    return existe

def obtenerContacto():
    archivo = open("note.txt","r",encoding="utf-8")
    filas = archivo.readlines()
    contactos.clear()
    for fila in filas:
        contacto = fila.strip("\n").split(",")
        contactos.append(contacto)
       
def listarContactos(): 
    print("LISTAR")
    obtenerContacto()
    contador = 0
    for contacto in contactos:
        contador += 1
        print(f"\nDatos del contacto {contador}")
        print(f"Identificación: {contacto[0]}")
        print(f"Nombre: {contacto[1]}")
        print(f"Apellido: {contacto[2]}")
        print(f"Correo: {contacto[3]}")
        print(f"Genero: {contacto[4]}")
    
def consultarPorIdentificacion(identificacion):
    print("CONSULTAR POR IDENTIFICACIÓN")
    
    obtenerContacto()
    for contacto in contactos:
        if (contacto[0] == identificacion):
            print(f"Nombre: {contacto[1]}")
            print(f"Apellido: {contacto[2]}")
            print(f"Correo: {contacto[3]}")
            print(f"Genero: {contacto[4]}")
            break
    else:
        print("No existe un contacto con esa identificación!")

def agregar():
    print("AGREGAR CONTACTO")
    archivo = open("note.txt","a",encoding="utf-8")
    identificacion = input("ingrese identificación: ")
    nombre = input("ingrese nombre(s): ")
    apellido = input("ingrese apellido(s): ")
    correo = input("ingrese correo electrónico: ")
    while(True):
        genero = input("ingrese genero (Femenino/Masculino): ").upper()
        if (genero == "FEMENINO" or genero == "MASCULINO"):
            break
        else:
            print("Debe volver a ingresar el genero!")
            
    existe = existeContacto(identificacion,correo)
    if (existe):
        print("Ya existe una persona con esa identificación o correo!")
    else:
        contacto = f"{identificacion},{nombre},{apellido},{correo},{genero}\n"
        archivo.write(contacto)
        archivo.close()
        print("Contacto agregado correctamente")
    
def menu():
    while(True):
        print("\t\tGESTIÓN CONTACTOS:")
        print("\t1. Agregar\n\t2. Consultar\n\t3. Listar\n\t4. Salir")
        opcion = int(input("\tIngrese opción: "))
        if(opcion == 1):
            agregar()
        elif(opcion == 2):
            identificacion = input("Ingrese identificación: ")
            consultarPorIdentificacion(identificacion)
        elif (opcion == 3):
            listarContactos()
        elif(opcion == 4):
            print("\n\tSe va a salir de la aplicación!")
            break
        else:
            print("\n\tOpción NO valida...")
            
        input("\n\tPresione ENTER para continuar")
        
crearArchivo()
menu()