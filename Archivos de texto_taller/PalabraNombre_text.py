import os

busqueda = input("Ingrese el nombre del archivo a buscar: ")
if os.path.exists (busqueda):
    print("Archivo encontrado...")
    archivo = open(busqueda,"r",encoding="utf-8")
    palabra = input("Ingrese la palabra a buscar: ")
    cont = archivo.read()
    if palabra in cont:
        print(f"La palabra {palabra}, SI existe en el archivo {archivo}")
    else:
        print(f"La palabra {palabra}, NO existe en el archivo {archivo}")
        
    archivo.close()
else:
    print("El archivo no existe")

# nombreArchivo = input("Ingrese el nombre del archivo con la extesión: ")

# if os.path.exists(nombreArchivo):
#     palabraBuscar = input(f"Ingrese la palabra a buscar en el archivo {nombreArchivo}: ")
#     archivo = open(nombreArchivo,"r",encoding="utf-8")
#     lineas = archivo.readlines()
#     #print(lineas)
#     existe = False
#     for linea in lineas:
#         #print(linea)
#         palabras = linea.strip("\n").split(" ")
#         # print(palabras)
        
#         for palabra in palabras:
#             if palabra == palabraBuscar :
#                 print("Si existe")
#                 existe = True
#                 break
                
#         if (existe):
#             break
        
#     if (not existe):
#         print("La palabra no existe...")
    
# else:
#     print("El archico no existe..")