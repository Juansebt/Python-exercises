try:
    archivoLinea = open("Lineas.txt","w",encoding="utf-8")
    cantidadLineas = int(input("Cuantas lineas de texto deseas agregar: "))
    
    for i in range(cantidadLineas):
        archivoLinea.write(f"Linea de texto {i+1}\n")
        
    archivoLinea.close()
except IOError as error:
    print(error.strerror)