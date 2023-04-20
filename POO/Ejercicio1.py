class Perro():
    
    #Metodo constructor |
    def __init__(self,nombre=None, raza=None):
        self.nombre = nombre
        self.raza = raza
        
    #Metodo sin parametros
    def ladrar(self):
        print(f"{self.nombre} está ladrando ¡Guau!")
        
    #Metodo con parametros
    def caminar(self, pasos):
        print(f"{self.nombre} ha caminado {pasos} pasos")
    
miJuanito = Perro("Juanito","Chandoso")

otroPerro = Perro()

print(f"El nombre del perro: {miJuanito.nombre}")
print(f"La raza del perro: {miJuanito.raza}")
miJuanito.ladrar()
miJuanito.caminar(6)

print(otroPerro.nombre)