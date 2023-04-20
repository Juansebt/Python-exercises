from Modelo.Silla import Silla
from Modelo.Persona import Persona
from Modelo.ingresoSala import IngresoSala

class Sala():
    def __init__(self, nombre=str, cantidadSillas=int):
        """_summary_
            Constructor con parametros de inicialización.
        Args:
            nombre (str): nombre de la sala de cine.
            cantidadSillas (int): cantidad de sillas que tiene la sala.
        """
        self.__nombre = nombre
        self.__cantidadSillas = cantidadSillas
        self.__estado = "DISPONIBLE"
        self.__listaSillas = []
        self.__listaIngresos = []
        self.__inicializarSillas()
        
    def __inicializarSillas(self):
        for i in range(self.__cantidadSillas):
            silla = Silla(i+1)
            self.__listaSillas.append(silla)
            
    def registrarIngreso(self, identificacion=str, nombre=str, correo=str, genero=str):
        persona = Persona(identificacion, nombre, correo, genero)
        sillaDisponible = self.__obtenerSillaDisponible()
        if(sillaDisponible is not None): #is not None
            ingresoSala = IngresoSala(persona, sillaDisponible)
            self.__listaIngresos.append(ingresoSala)
            sillaDisponible.setPersona(persona)
            sillaDisponible.setEstado()
            return True, "\n\tSe ha realizado el registro de ingreso"
        else:
            return False, "\n\tNo hay silla disponible en la sala"
        
    def __obtenerSillaDisponible(self):
        for silla in self.__listaSillas:
            if(silla.getEstado() == "DISPONIBLE"):
                return silla
            
        return None
    
    def obtenerDatosPersonaSilla(self, numero=int):
        for silla in self.__listaSillas:
            if (silla.getNumeroSilla() == numero):
                if (silla.getEstado() == "OCUPADO"):
                    return silla.getPersona()
                else:
                    return "\n\tNo hay persona sentada en esa silla!"
                
        return "\n\tNo existe silla con ese número!"
    
    def obtenerCantidadMujeresHombres(self):
        mujeres, hombres = 0,0
        for ingreso in self.__listaIngresos:
            if(ingreso.getPersona().getGenero() == "FEMENINO"):
                mujeres+=1
            else:
                hombres+=1
                
        return mujeres, hombres
    
    def getNombre(self):
        return self.__nombre
    
    def getListaSillas(self):
        return self.__listaSillas
    
    def getListaIngresos(self):
        return self.__listaIngresos
    
    def getCantidadSillas(self):
        return self.__cantidadSillas