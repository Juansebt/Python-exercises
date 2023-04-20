#Agregación curso - alumno

class Curso():
    
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__alumnos = []
        
    def  matricularAlumno(self, alumno):
        self.__alumnos.append(alumno)
        
    def getNombre(self):
        return self.__nombre
    
    def getAlumnos(self):
        return self.__alumnos
    
    #Metodo to string
    def __str__(self):
        return self.__nombre
    
    #Metodo para eliminar la clase
    def __del__(self):
        print("Curso Eliminado")
    
class Alumno():
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad = edad
        
    def __str__(self):
        return self.__nombre
        
        
unCurso = Curso("Python Avanzdo")

alumno1 = Alumno("Juan",18)
alumno2 = Alumno("María",17)
alumno3 = Alumno("Andrés",19)

unCurso.matricularAlumno(alumno1)
unCurso.matricularAlumno(alumno3)

#print(unCurso.getAlumnos())
for alumno in unCurso.getAlumnos():
    print(alumno)
    
unCurso.__del__()
print(unCurso.getNombre())
