from Cliente import Cliente
from Producto import Producto
from Venta import Venta
from datetime import datetime

class Tienda():
    
    def __init__(self,NombreTienda):
        self.__NombreTienda = NombreTienda
        self.__listaClientes = []
        self.__listaProductos = []
        self.__listaVentas = []
        
    def getNombreTienda(self):
        return self.__NombreTienda
    
    def setNombreTienda(self,NombreTienda):
        self.__NombreTienda = NombreTienda
        
    def agregarCliente(self,Nombre,Direccion,Correo):
        cliente = Cliente(Nombre,Direccion,Correo)
        self.__listaClientes.append(cliente)
        
    def agregarProducto(self,Codigo,Nombre,Precio):
        producto = Producto(Codigo,Nombre,Precio)
        self.__listaProductos.append(producto)
        
    def agregarVenta(self,Fecha=datetime,cliente=Cliente):
        venta = Venta(Fecha,cliente)
        self.__listaVentas.append(venta)
        
    def getListaClientes(self):
        return self.__listaClientes

    def getListaProductos(self):
        return self.__listaProductos
    
    def getListaVentas(self):
        return self.__listaVentas
        