class Cliente():
    
    def __init__(self,Nombre,Direccion,Correo):
        self.__Nombre = Nombre
        self.__Direccion = Direccion
        self.__Correo = Correo
        
    def getNombreCliente(self):
        return self.__Nombre
    
    def setNombreCliente(self,Nombre):
        self.__Nombre = Nombre
        
    def getDireccion(self):
        return self.__Direccion
    
    def setDireccion(self,Direccion):
        self.__Direccion = Direccion
        
    def getCorreo(self):
        return self.__Correo
    
    def setCorreo(self,Correo):
        self.__Correo = Correo