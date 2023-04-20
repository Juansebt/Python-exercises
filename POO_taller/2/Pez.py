from Animal import Animal #Llamar a un clase de otro archivo

class Pez(Animal):
    
    def __init__(self, peso):
        super().__init__(peso)
        
    def Respirar(self):
        print(f"El {type(self).__name__} esta respirando...")
        
    def Nadar(self):
        print(f"El {type(self).__name__} esta nadando...")