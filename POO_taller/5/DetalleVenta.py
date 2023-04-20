from Producto import Producto

class DetalleVenta():
     
    def __init__(self,producto=Producto,Cantidad=0,Valor=int):
        self.__producto = producto
        self.__Cantidad = Cantidad
        self.__Valor = Valor
        
    def getProducto(self):
        return self.__producto
    
    def getCantidad(self):
        return self.__Cantidad
    
    def getValor(self):
        return self.__Valor
    
    def setCantidad(self,Cantidad):
        self.__Cantidad = Cantidad
    
    def setValor(self,Valor):
        self.__Valor = Valor