from Vuelo import Vuelo

class Empresa():
    
    def __init__(self,nombre=None):
        self.__nombre = nombre
        self.__listaVuelos = []
        
    def registrarVuelo(self,numeroVuelo=None,fecha=None,ciudadOrigen=None,ciudadDestino=None):
        if (numeroVuelo and fecha and  ciudadOrigen and ciudadDestino):
            vuelo = Vuelo(numeroVuelo,fecha,ciudadOrigen,ciudadDestino)
            self.__listaVuelos.append(vuelo)
        else:
            return False
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getListaVuelos(self):
        return self.__listaVuelos