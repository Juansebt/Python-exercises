from Pasajero import Pasajero

class Vuelo():
    
    def __init__(self,numeroVuelo=None,fecha=None,ciudadOrigen=None,ciudadDestino=None):
        self.__numeroVuelo = numeroVuelo
        self.__fecha = fecha
        self.__ciudadOrigen = ciudadOrigen
        self.__ciudadDestino = ciudadDestino
        self.__listaPasajeros = []
        
    # def agregarPasajero(self, Pasajero):
    #     self.__listaPasajeros.append(Pasajero)
    
    def agregarPasajero(self,nombre=None,identificacion=None,edad=None):
        pasajero = Pasajero(nombre,identificacion,edad)
        self.__listaPasajeros.append(pasajero)
        
    def getNumeroVuelo(self):
        return self.__numeroVuelo
    
    def setNumeroVuelo(self, numeroVuelo):
        self.__listaPasajeros = numeroVuelo
        
    def getFecha(self):
        return self.__fecha
    
    def setFecha(self, fecha):
        self.__fecha = fecha
        
    def getCiudadOrigen(self):
        return self.__ciudadOrigen
    
    def setCiudadOrigen(self, ciudadOrigen):
        self.__ciudadOrigen = ciudadOrigen
        
    def getCiudadDestino(self):
        return self.__ciudadDestino
    
    def setCiudadDestino(self, ciudadDestino):
        self.__ciudadDestino = ciudadDestino
        
    def getListaPasajeros(self):
        return self.__listaPasajeros
    
    