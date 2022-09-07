import Cola

class ArbolBinario:
    
    def __init__(self, dato):
        
        self.__raiz = dato
        self.__hijoIzq = None
        self.__hijoDer = None
        
    def get_dato(self):
        return self.__raiz
     
    def get_HijoIzq(self):
        return self.__hijoIzq
    
    def get_HijoDer(self):
        return self.__hijoDer
    
    def agregarHijoIzq(self, arbol):
        self.__hijoIzq = arbol
    
    def agregarHijoDer(self, arbol):
        self.__hijoDer = arbol
        
    def eliminarHijoIzq(self):
        self.__hijoIzq = None
    
    def eliminarHijoDer(self):
        self.__hijoDer = None
    
    def preorden(self):
        print(self.__raiz)
        if self.__hijoIzq != None:
            self.__hijoIzq.preorden()
        if self.__hijoDer != None:
            self.__hijoDer.preorden()
            
    def inorden(self):
        if self.__hijoIzq != None:
            self.__hijoIzq.inorden()
        print(self.__raiz)
        if self.__hijoDer != None:
            self.__hijoDer.inorden()
            
    def postorden(self):
        if self.__hijoIzq != None:
            self.__hijoIzq.postorden()
        if self.__hijoDer != None:
            self.__hijoDer.postorden()
        print(self.__raiz)
        
    def porNiveles(self):
        cola = Cola()
        cola.encolar(self.__raiz)
        while not cola.esVacia():
            print(cola.desncolar())
            if self.__hijoIzq != None:
               cola.encolar(self.__hijoIzq)
            if self.__hijoDer != None:
                cola.encolar(self.__hijoDer)
        
            
    

        
            
        
arbol1 = ArbolBinario(1)
arbol2 = ArbolBinario(2)
arbol3 = ArbolBinario(3)
arbol4 = ArbolBinario(4)
arbol5 = ArbolBinario(5)

print(arbol1.get_dato())