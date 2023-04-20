from Modelo.Silla import Silla
from Modelo.Persona import Persona
from datetime import datetime

class IngresoSala():
    def __init__(self, persona=Persona, silla=Silla):
        """_summary_
            Constructor con parametros de inicialización.
            Crea el objeto que representa el ingreso a la sala.
        Args:
            persona (Persona): objeto de tipo Persona.
            silla (Silla): objeto de tipo Silla.
        """
        self.__persona = persona
        self.__silla = silla
        self.__fechaHora = datetime.now()
        
    def getPersona(self):
        return self.__persona
    
    def getSilla(self):
        return self.__silla
    
    def getFechaHora(self):
        return self.__fechaHora