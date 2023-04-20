from Animal import Animal

class Gato(Animal):
    
    def __init__(self, peso):
        super().__init__(peso)
        
    def Respirar(self):
        print(f"El {type(self).__name__} esta respirando...")
        
    def Maullar(self):
        print(f"El {type(self).__name__} esta maullando...")