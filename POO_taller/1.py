"""
De acuerdo al diagrama anexo representar en Python las clases Carro y libro. 
En el mismo archivo crear un objeto de tipo carro y un objeto de tipo Libro.
"""
class Carro():
    
    def __init__(self, placa,marca,modelo,color):
        self.__placa = placa #Atributo privado
        self.marca = marca #Atributo publico
        self.__modelo = modelo #Atributo privado
        self.color = color #Atributo publico
        
    #Metodos GET
    def getPlaca(self):
        return self.__placa
    
    def getModelo(self):
        return self.__modelo
    
    #Metodos SET
    def setPlaca(self, placa):
        self.__placa = placa
        
    def setModelo(self, modelo):
        self.__modelo = modelo

class Libro():
    
    def __init__(self,titulo,autor,numeroPaginas):
        self.__titulo = titulo #Atributo privado
        self.__autor = autor #Atributo privado
        self.__numeroPaginas = numeroPaginas #Atributo privado
        
    #Metodos GET
    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getNumeroPaginas(self):
        return self.__numeroPaginas
    
    #Metodos SET
    def setTitulo(self, titulo):
        self.__titulo = titulo
        
    def setAutor(self, autor):
        self.__autor = autor
        
    def setNumeroPaginas(self, numeroPaginas):
        self.__numeroPaginas = numeroPaginas
        
print("--------------------------------------")

#Objeto de tipo Carro
miCarro = Carro("XYZ123","Tesla",2023,"Gris")
print(f"\tMi carro:\n\tPlaca: {miCarro.getPlaca()}\n\tMarca: {miCarro.marca}\n\tModelo: {miCarro.getModelo()}\n\tColor: {miCarro.color}")

print("--------------------------------------")

#Objeto de tipo Libro
miLibro = Libro("Verde fue mi selva","",312)
print(f"\tMi libro:\n\tTitulo: {miLibro.getTitulo()}\n\tAutor: {miLibro.getAutor()}\n\tNúmero de páginas: {miLibro.getNumeroPaginas()}")

print("--------------------------------------")
