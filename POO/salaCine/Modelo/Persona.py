class Persona():
    def __init__(self, identificacion=str, nombre=str, correo=str, genero=str):
        """_summary_
            Constructor con parametros de inicialización.
        Args:
            identificacion (str): documento de identidad.
            nombre (str): nombre completo.
            correo (str): correo electrónico.
            genero (str): masculino - femenino.
        """
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo
        self.__genero = genero
        
    def getIdentificacion(self):
        return self.__identificacion
    
    def getNombre(self):
        return self.__nombre
    
    def getCorreo(self):
        return self.__correo
    
    def getGenero(self):
        return self.__genero