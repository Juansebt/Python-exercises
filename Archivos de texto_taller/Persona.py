try:
    ArchivoPersona = open("Persona.txt","w",encoding="utf-8")
    # person = input("Ingrese el nombre de una persona: ")
    # ArchivoPersona.write(f"{person}\n")
    ArchivoPersona.write("Pedro Rojas\n")
    ArchivoPersona.write("María Dolores\n")
    ArchivoPersona.write("José Luna\n")
    ArchivoPersona.write("Martha Restrepo")
    print("Archivo creado...")
    ArchivoPersona.close()
except IOError as error:
    print(error.strerror)