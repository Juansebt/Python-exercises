"""
La Empresa X cuenta con dos tipos de empleados así:
• Contratista: empleados cuyo salario mensual se basa en el número de horas trabajadas en
el mes y según el valor de la hora.
• Planta: empleados que tienen un sueldo mensual independientemente de las horas
trabajadas.
Los datos de los empleados son los siguientes:
• Cédula, nombres, apellidos, correo, genero, fecha de ingreso a la empresa, cargo
"""
from Contratista import Contraista
from Planta import Planta
from Empresa import Empresa
import datetime as dt

miEmpresa = Empresa("Berkshire Hathaway")
print(f"\n{miEmpresa.getNombre().upper()}")

print("-----------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\nEmpleado contratista 1\n")
cedulaC1 = int(input("Ingrese la cédula: "))
nombresC1 = input("Ingresa los nombres: ")
apellidosC1 = input("Ingresa los apellidos: ")
correoC1 = input("Ingresa el correo electrónico: ")
generoC1 = input("Ingresa el genero (Masculino-Femenino): ").upper()
fechaIngresoC1 = input("Ingresa la fecha de ingreso (dd/mm/yyyy): ")
cargoC1 = input("Ingresa el cargo: ")
valorHoraC1 = 32000

contratista1 = Contraista(cedulaC1,nombresC1,apellidosC1,correoC1,generoC1,fechaIngresoC1,cargoC1,valorHoraC1)

miEmpresa.agregarEmpleadoContratista(contratista1)

horasTrabajadasC1 = int(input("Cuantás horas trabajó: "))
salarioMensualC1 = float(contratista1.calcuarSalarioMensual(horasTrabajadasC1))
print(f"\nEl salario mensual de {contratista1.getNombres()} es: {salarioMensualC1}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\n\nEmpleado contratista 2\n")
cedulaC2 = int(input("Ingrese la cédula: "))
nombresC2 = input("Ingresa los nombres: ")
apellidosC2 = input("Ingresa los apellidos: ")
correoC2 = input("Ingresa el correo electrónico: ")
generoC2 = input("Ingresa el genero (Masculino-Femenino): ").upper()
fechaIngresoC2 = input("Ingresa la fecha de ingreso (dd/mm/yyyy): ")
cargoC2 = input("Ingresa el cargo: ")
valorHoraC2 = 25000

contratista2 = Contraista(cedulaC2,nombresC2,apellidosC2,correoC2,generoC2,fechaIngresoC2,cargoC2,valorHoraC2)

miEmpresa.agregarEmpleadoContratista(contratista2)

horasTrabajadasC2 = int(input("Cuantás horas trabajó: "))
salarioMensualC2 = float(contratista2.calcuarSalarioMensual(horasTrabajadasC2))
print(f"\nEl salario mensual de {contratista2.getNombres()} es: {salarioMensualC2}")

print("-----------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\nEmpleado de planta 1\n")
cedulaP1 = int(input("Ingrese la cédula: "))
nombresP1 = input("Ingresa los nombres: ")
apellidosP1 = input("Ingresa los apellidos: ")
correoP1 = input("Ingresa el correo electrónico: ")
generoP1 = input("Ingresa el genero (Masculino-Femenino): ").upper()
fechaIngresoP1 = input("Ingresa la fecha de ingreso (dd/mm/yyyy): ")
cargoP1 = input("Ingresa el cargo: ")
sueloBaseP1 = 2500000

planta1 = Planta(cedulaP1,nombresP1,apellidosP1,correoP1,generoP1,fechaIngresoP1,cargoP1,sueloBaseP1)

miEmpresa.agregarEmpleadoPlanta(planta1)

diasTrabajadosP1 = int(input("Ingrese los días trabajados: "))
salarioMensualP1 = planta1.calcularSalarioMensual(diasTrabajadosP1)
print(f"\nEl salario mensual de {planta1.getNombres()} es: {salarioMensualP1}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\n\nEmpleado de planta 2\n")
cedulaP2 = int(input("Ingrese la cédula: "))
nombresP2 = input("Ingresa los nombres: ")
apellidosP2 = input("Ingresa los apellidos: ")
correoP2 = input("Ingresa el correo electrónico: ")
generoP2 = input("Ingresa el genero (Masculino-Femenino): ").upper()
fechaIngresoP2 = input("Ingresa la fecha de ingreso (dd/mm/yyyy): ")
cargoP2 = input("Ingresa el cargo: ")
sueloBaseP2 = 3000000

planta2 = Planta(cedulaP2,nombresP2,apellidosP2,correoP2,generoP2,fechaIngresoP2,cargoP2,sueloBaseP2)

miEmpresa.agregarEmpleadoPlanta(planta2)

diasTrabajadosP2 = int(input("Ingrese los días trabajados: "))
salarioMensualP2 = planta2.calcularSalarioMensual(diasTrabajadosP2)
print(f"\nEl salario mensual de {planta2.getNombres()} es: {salarioMensualP2}")

print("-----------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\nLista de empledaos contratistas: \n")

i = 0

for contratistas in miEmpresa.getListaEmpleadosContratistas():
    i+=1
    CedulaC = contratistas.getCedula()
    NombresC = contratistas.getNombres()
    ApellidosC = contratistas.getApellidos()
    CorreoC = contratistas.getCorreo()
    GeneroC = contratistas.getGenero()
    fechaIngresoC = contratistas.getFechaIngreso()
    CargoC = contratistas.getCargo()
    valorHoraC = contratistas.getValorHora()
    
    print(f"\nContratista {i}: \n")
    print(f"Cédula: {CedulaC}\nNombres: {NombresC}\nApellidos: {ApellidosC}\nCorreo electrónico: {CorreoC}\nGenero: {GeneroC}\nFecha de ingreso: {fechaIngresoC}\nCargo: {CargoC}\nValor por hora: {valorHoraC}\n\n")
    
print("-----------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\nLista de empleados de planta: \n")

c = 0

for plantas in miEmpresa.getListaEmpleadosPlanta():
    c+=1
    CedulaP = plantas.getCedula()
    NombresP = plantas.getNombres()
    ApellidosP = plantas.getApellidos()
    CorreoP = plantas.getCorreo()
    GeneroP = plantas.getGenero()
    fechaIngresoP = plantas.getFechaIngreso()
    CargoP = plantas.getCargo()
    sueldoBaseP = plantas.getSueloBase()

    print(f"\nEmpleado de planta {c}: \n")
    print(f"Cédula: {CedulaP}\nNombres: {NombresP}\nApellidos: {ApellidosP}\nCorreo electrónico: {CorreoP}\nGenero: {GeneroP}\nFecha de ingreso: {fechaIngresoP}\nCargo: {CargoP}\nSueldo base: {sueldoBaseP}\n\n")
    