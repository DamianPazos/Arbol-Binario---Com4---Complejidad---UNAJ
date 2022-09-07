class Cola:
    
    def __init__(self):
        self.__items = []
    
    def encolar(self, dato):
        self.__items.append(dato)
    
    def desencolar(self):
        try:
            return self.__items.pop(0)
        except:
            return ValueError('La cola se encuentra vacia')
    
    def esVacia(self):
        if self.__items.count == 0:
            return True
        else:
            return False