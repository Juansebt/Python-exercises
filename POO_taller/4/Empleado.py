class Empleado():
    
    def __init__(self,Cedula,Nombres,Apellidos,Correo,Genero,fechaIngreso,Cargo):
        self.__Cedula = Cedula
        self.__Nombres = Nombres
        self.__Apellidos = Apellidos
        self.__Correo = Correo
        self.__Genero = Genero
        self.__fechaIngreso = fechaIngreso
        self.__Cargo = Cargo
        
    def getCedula(self):
        return self.__Cedula
    
    def getNombres(self):
        return self.__Nombres
    
    def getApellidos(self):
        return self.__Apellidos
    
    def getCorreo(self):
        return self.__Correo
    
    def getGenero(self):
        return self.__Genero
    
    def getFechaIngreso(self):
        return self.__fechaIngreso
    
    def getCargo(self):
        return self.__Cargo