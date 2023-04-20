from Empleado import Empleado

class Contraista(Empleado):
    
    def __init__(self, Cedula, Nombres, Apellidos, Correo, Genero, fechaIngreso, Cargo, valorHora):
        super().__init__(Cedula, Nombres, Apellidos, Correo, Genero, fechaIngreso, Cargo)
        self.__valorHora = valorHora
        self.__Salario = 0
        
    def getValorHora(self):
        return self.__valorHora
    
    def setValorHora(self,valorHora):
        self.__valorHora = valorHora
    
    def calcuarSalarioMensual(self,horasTrabajadas):
        self.__Salario = self.__valorHora * horasTrabajadas
        return self.__Salario