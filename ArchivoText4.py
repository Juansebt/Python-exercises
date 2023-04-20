try:
    archivo = open("Ejemplo.txt","a",encoding="utf-8")
    
    archivo.write("Campaña SENA\n")
    
    archivo.write("Comunicación empresarial\n")
    
    archivo.close
    
except IOError as error:
    print(error.strerror)