try:
    
    archivo = open("frutas.txt","r")
    frutas = archivo.readlines() #Leer todas las lineas del archivo de texto - list
    #frutas = archivo.readline() #Leer linea por linea el archivo - str
    archivo.close()
    print(type(frutas))
    print(frutas)
    otrasFrutas = []
    
    
    for fruta in frutas:
        print(fruta)
        f = fruta.strip("\n")
        otrasFrutas.append(f)
    
except IOError as error:
    print(error.strerror)
    
print(fruta)
print(otrasFrutas)