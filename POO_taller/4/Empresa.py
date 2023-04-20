from Contratista import Contraista
from Planta import Planta
class Empresa():
    
    def __init__(self,nombreEmpresa):
        self.__nombreEmpresa = nombreEmpresa
        self.__listaEmpleadosContratistas = []
        self.__listaEmpleadosPlanta = []
        
    def agregarEmpleadoContratista(self,contratista=Contraista):
        self.__listaEmpleadosContratistas.append(contratista)
        
    # def agregarEmpleadoPlanta(self,Cedula,Nombres,Apellidos,Correo,Genero,fechaIngreso,Cargo,sueldoBasico):
    #     empleadoPlanta = Planta(Cedula,Nombres,Apellidos,Correo,Genero,fechaIngreso,Cargo,sueldoBasico)
    #     self.__listaEmpleadosPlanta.append(empleadoPlanta)
        
    def agregarEmpleadoPlanta(self,planta=Planta):
        self.__listaEmpleadosPlanta.append(planta)
        
    def getNombre(self):
        return self.__nombreEmpresa
    
    def setNombre(self,nombreEmpresa):
        self.__nombreEmpresa = nombreEmpresa
        
    def getListaEmpleadosContratistas(self):
        return self.__listaEmpleadosContratistas
    
    def getListaEmpleadosPlanta(self):
        return self.__listaEmpleadosPlanta