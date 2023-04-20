class Producto():
    
    def __init__(self,Codigo,Nombre,Precio):
        self.__Codigo = Codigo
        self.__Nombre = Nombre
        self.__Precio = Precio
        
    def getCodigo(self):
        return self.__Codigo
    
    def setCodigo(self,Codigo):
        self.__Codigo = Codigo
        
    def getNombreProducto(self):
        return self.__Nombre
    
    def setNombreProducto(self,Nombre):
        self.__Nombre = Nombre
        
    def getPrecioProducto(self):
        return self.__Precio
    
    def setPrecioProducto(self,Precio):
        self.__Precio = Precio