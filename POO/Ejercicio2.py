class Persona():
    
    def __init__(self,identificacion,nombre,correo):
        """_summary_
            Metodo constructor
        Args:
            identificacion (int): Identificacion de la persona
            nombre (String): nombre de la persona
            correo (String): correo de la persona
        """
        #Atributos privados
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo
        
        #atributo protecte
        #self._correo = correo
        
    #Metodos get and set
    def getIdentificacion(self):
        return self.__identificacion
    
    def setIdentificacion(self, identificacion):
        self.__identificacion = identificacion
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getCorreo(self):
        return self.__correo
    
    def setCorreo(self, correo):
        self.__correo = correo
        
    def saludar(self):
        print(f"Desde la clase persona... Hola soy un objeto de tipo: {type(self).__name__}")
        
#Herencia - Aprendiz hereda de la clase persona

class Aprendiz(Persona):
    
    def __init__(self, identificacion, nombre, correo, puntajeIcfes):
        super().__init__(identificacion, nombre, correo)
        self.__puntajeIcfes = puntajeIcfes
        
    def getPuntajeIcfes(self):
        return self.__puntajeIcfes
    
    def setPuntajeIcfes(self, puntajeIcfes):
        self.__puntajeIcfes = puntajeIcfes
        
    def saludar2(self):
        print(f"Desde la clase aprendiz... Hola soy un objeto de tipo: {type(self).__name__}")
        
        
class Instructor(Persona):
    
    def __init__(self, identificacion, nombre, correo, especialidad):
        super().__init__(identificacion, nombre, correo)
        self.__especialidad = especialidad
        
    def getEspecialidad(self):
        return self.__especialidad
    
    def setEspecialidad(self, especialidad):
        self.__especialidad = especialidad
        
    def saludar(self):
        print(f"Desde la clase instructor... Hola soy un objeto de tipo: {type(self).__name__}")
    

#per = Persona(11,"Juan Sebastián","juansebt.0610@gmail.com")

aprendiz = Aprendiz(18,"Juan Sebastián","juansebt.0610@gmail.com",500)

instructor = Instructor(20,"Carlos Cadena","ccadena@gmail.com","Desarrollo de software")

print(aprendiz.getIdentificacion())
print(aprendiz.getNombre())
print(aprendiz.getCorreo())
print(aprendiz.getPuntajeIcfes())

aprendiz.saludar()

# per.__nombre = "Pablo Emilio"

# print(per.__nombre)

# print(f"Identificación: {per.getIdentificacion()}")



