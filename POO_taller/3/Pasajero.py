class Pasajero():
    
    def __init__(self,nombre=None,identificacion=None,edad=None):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__edad = edad
        
    def getNombre(self):
        return self.__nombre
    
    def getIdentificacion(self):
        return self.__identificacion
    
    def getEdad(self):
        return self.__edad
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setIdentificacion(self, identificacion):
        self.__identificacion = identificacion
        
    def setEdad(self, edad):
        self.__edad = edad
        