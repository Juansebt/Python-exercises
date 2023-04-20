import os

archivo = input("Ingrese el nombre del archivo a buscar: ")

if os.path.exists(archivo):
    print("\nArchivo encontrado\n")
    arch = open(archivo,"r",encoding="utf-8")
    lineas = arch.readlines()
    i = 0
    for linea in lineas:
        i+=1
        if linea[-1]== "\n":
            linea = linea[:-1]
        print(f"{i} - {linea}")
    print()
        
    arch.close()
else:
    print("El archivo no existe...")