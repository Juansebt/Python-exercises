class Animal():
    
    def __init__(self,peso,):
        self.__peso = peso
        
    def getPeso(self):
        return self.__peso
    
    def setPeso(self, peso):
        self.__peso = peso
    
    def Respirar(self):
        print(f"Un {type(self).__name__} esta respirando...")