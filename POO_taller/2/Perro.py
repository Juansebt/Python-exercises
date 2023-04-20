from Animal import Animal

class Perro(Animal):
    
    def __init__(self, peso):
        super().__init__(peso)
        
    def Respirar(self):
        print(f"El {type(self).__name__} esta respirando...")
        
    def Ladrar(self):
        print(f"El {type(self).__name__} esta ladrando...")