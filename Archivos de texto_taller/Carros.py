try:
    archivo = open("Carros.txt","a",encoding="utf-8")
    placa = input("Ingrese la placa: ")
    marca = input("Ingrese la marca: ")
    color = input("Ingrese el color: ")
    #carro = placa,marca,color
    #archivo.writelines(f"{carro}\n")
    archivo.write(f"{placa},")
    archivo.write(f"{marca},")
    archivo.write(f"{color}\n")
except IOError as error:
    print(error.strerror)