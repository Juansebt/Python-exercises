#Archivos de texto

#Crear archivo de texto
try:
    archivo = open("frutas.txt","a") #x(crea el archivo y si existe no lo reemplaza) - w(archivo si existe es reemplazado por uno vacio) - a(Abrirlo para agregar) - r(leer)

    print("Archivo creado")

    print(type(archivo))
    
    archivo.write("Banano\n")

    archivo.close()
except IOError as error:
    print(error.strerror)