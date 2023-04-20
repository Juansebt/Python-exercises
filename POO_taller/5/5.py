"""
Representar en Python cada una de las clases de acuerdo al diagrama anexado en el documento del taller.
• Para cada clase crear un archivo en Python
• Crear otro archivo que haga lo siguiente:
    o Crear un objeto de tipo Tienda
    o Crear un producto
    o Agregar el producto a la tienda
    o Crear un producto
    o Agrear el producto a la tienda
    o Crear un objeto de tipo Cliente
    o Crear un objeto e tipo Venta
    o Agregar un detalleVenta a la venta
    o Agregar otro detalleVenta a la Venta
    o Listar todos los datos de la venta aí:
        ▪ Fecha de la venta
        ▪ Nombre del Cliente
        ▪ Productos de la Venta:
            • Nombre producto
            • Precio Unitario
            • Cantidad
            • Valor Total
            • Y así si hay más producto en el detalle
        ▪ Valor total de la venta
"""
from Tienda import Tienda
from Cliente import Cliente
from Producto import Producto
from Venta import Venta
from DetalleVenta import DetalleVenta
import datetime
import os

os.system("cls")

# Objeto tienda
miTienda = Tienda("Tienda ADSO 2023")
print(f"\t\t{miTienda.getNombreTienda().upper()}")
print("-----------------------------------------------------------------------")

# Objeto producto
codigoP1 = int(input("\tIngrese el código del producto 1: "))
nombreP1 = input("\tIngrese el nombre del producto 1: ")
precioP1 = int(input("\tIngrese el precio del producto 1: "))

producto1 = Producto(codigoP1, nombreP1, precioP1)
print("\t\tProducto 1 creado efectivamente...")
print("-----------------------------------------------------------------------")

# Agregar producto a la lista de la tienda
miTienda.agregarProducto(codigoP1, nombreP1, precioP1)
# print("Producto 1 agregado correctamente a la tienda...")
#print("-----------------------------------------------------------------------")

# Objeto 2 de producto
codigoP2 = int(input("\tIngresa el código del producto 2: "))
nombreP2 = input("\tIngresa el nombre del producto 2: ")
precioP2 = int(input("\tIngresa el precio del producto 2: "))

producto2 = Producto(codigoP2, nombreP2, precioP2)
print("\t\tProducto 2 creado efectivamente...")
print("-----------------------------------------------------------------------")

# Agregar producto 2 a la lista de tienda
miTienda.agregarProducto(codigoP2, nombreP2, precioP2)
# print("Producto 2 agregado correctamente a la tienda...")
#print("-----------------------------------------------------------------------")

# Objeto cliente
nombreC1 = input("\tIngrese el nombre del cliente: ")
direccionC1 = input("\tIngrese la direccion del cliente: ")
correoC1 = input("\tIngrese el correo electronico del cliente: ")

cliente1 = Cliente(nombreC1, direccionC1, correoC1)
print("\t\tCliente creado efectivamente...")
print("-----------------------------------------------------------------------")

# Agregar cliente a la lista de clientes de la tienda
miTienda.agregarCliente(nombreC1, direccionC1, correoC1)
#print("-----------------------------------------------------------------------")

# Objeto venta
diaV1 = int(input("\tIngrese el día de la venta: "))
mesV1 = int(input("\tIngrese el mes de la venta (Ene : 01...): "))
añoV1 = int(input("\tIngrese el año de la venta: "))

fechaV1 = datetime.datetime(añoV1, mesV1, diaV1)
#print(fechaV1.strftime("%x"))

venta = Venta(fechaV1, cliente1)
print("\t\tVenta realizada con exito...")
print("-----------------------------------------------------------------------")

# Agregar venta a la lista de ventas de la tienda
miTienda.agregarVenta(fechaV1, cliente1)
#print("-----------------------------------------------------------------------")

# Agregar un detalle de venta al producto 1
cantProduct1 = int(input("\tCuantos productos 1 se adquirieron: "))
venta.agregarDetalle(producto1, cantProduct1)
print("\t\tDetalle del producto 1 agregado...")
print("-----------------------------------------------------------------------")

# Agregar otro detalle de venta al producto 2
cantProduct2 = int(input("\tCuantos productos 2 se adquirieron: "))
venta.agregarDetalle(producto2, cantProduct2)
print("\t\tDetalle del producto 2 agregado...")
print("-----------------------------------------------------------------------")

# Listar datos de la venta

#datos de venta
for venta in miTienda.getListaVentas():
    fechaVenta = venta.getFecha().strftime("%x")
    
#Datos de cliente
for cliente in miTienda.getListaClientes():
    nombreCliente = cliente.getNombreCliente()

print(f"\t\t{miTienda.getNombreTienda().upper()}\n\n\t\tDatos de la venta\n")
print(f"\tFecha de la venta: {fechaVenta}")
print(f"\tNombre del cliente: {nombreCliente}")

valorTotalP1 = precioP1*cantProduct1
valorTotalP2 = precioP2*cantProduct2
###
print("\n\tProducto de la venta")
###
print(f"\n\tNombre del producto 1: {nombreP1}")
print(f"\tPrecio unitario: {precioP1}")
print(f"\tCantidad adquirida: {cantProduct1}")
print(f"\tValor total: {valorTotalP1}")
###
print(f"\n\tNombre del producto 2: {nombreP2}")
print(f"\tPrecio unitario: {precioP2}")
print(f"\tCantidad adquirida: {cantProduct2}")
print(f"\tValor total: {valorTotalP1}")
###
print(f"\n\t\tValor total de la venta: {valorTotalP1+valorTotalP2}")
###
print("-----------------------------------------------------------------------")
