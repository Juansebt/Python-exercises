try:
    archivo = open("frutas.txt","a") #agregar al archivo
    fruta = input("Ingrese una fruta: ")
    archivo.write(f"{fruta}\n")
    archivo.close()
except IOError as error:
    print(error.strerror)