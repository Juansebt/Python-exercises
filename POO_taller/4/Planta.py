from Empleado import Empleado

class Planta(Empleado):
    
    def __init__(self, Cedula, Nombres, Apellidos, Correo, Genero, fechaIngreso, Cargo, sueldoBase):
        super().__init__(Cedula, Nombres, Apellidos, Correo, Genero, fechaIngreso, Cargo)
        self.__sueldoBase = sueldoBase
        self.__Salario = 0
        
    def getSueloBase(self):
        return self.__sueldoBase
    
    def setSueldoBase(self,sueldoBase):
        self.__sueldoBase = sueldoBase
    
    def calcularSalarioMensual(self,diasTrabajados):
        self.__Salario = (self.__sueldoBase * diasTrabajados) / 30
        return self.__Salario