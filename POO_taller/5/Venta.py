from DetalleVenta import DetalleVenta
from Cliente import Cliente
from Producto import Producto
from datetime import datetime

class Venta():
    
    def __init__(self,Fecha=datetime,cliente=Cliente):
        self.__Fecha = Fecha
        self.__cliente = cliente
        self.__listaDetalle = []
        
    def agregarDetalle(self,producto=Producto, cantidad=int):
        valor = producto.getPrecioProducto()*cantidad
        detalleVenta = DetalleVenta(producto,cantidad,valor)
        self.__listaDetalle.append(detalleVenta)
        
    def getFecha(self):
        return self.__Fecha
    
    def setFecha(self,Fecha):
        self.__Fecha = Fecha
        
    def getCliente(self):
        return self.__cliente
    
    def getListaDetalle(self):
        return self.__listaDetalle