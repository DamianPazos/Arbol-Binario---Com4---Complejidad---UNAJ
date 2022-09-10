from Cola import *

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
        
#    def porNiveles(self):
#        cola = Cola()
#        arbolTemporal = None
#        cola.encolar(self)
#        while not cola.esVacia():
#            arbolTemporal = cola.desencolar()
#            print(arbolTemporal.get_dato())
#            if self.__hijoIzq != None:
#               cola.encolar(self.__hijoIzq)
#            if self.__hijoDer != None:
#                cola.encolar(self.__hijoDer)
                
    def porNiveles(self):
        cola = []
        cola.append(self)
        while len(cola) != 0:
            arbolTemp = cola.pop(0)
            print(arbolTemp.get_dato())
            if arbolTemp.get_HijoIzq() != None:
                cola.append(arbolTemp.get_HijoIzq())
            if arbolTemp.get_HijoDer() != None:
                cola.append(arbolTemp.get_HijoDer())
    
    def contarHojas(self):
        if self.__hijoIzq != None and self.__hijoDer != None:
            return self.__hijoIzq.contarHojas() + self.__hijoDer.contarHojas()
        elif self.__hijoIzq != None:
            return self.__hijoIzq.contarHojas()
        elif self.__hijoDer != None:
            return self.__hijoDer.contarHojas()
        else:
            return 1   
            
    
                
arbol = ArbolBinario(1)
nodo2 = ArbolBinario(2)
nodo3 = ArbolBinario(3)
arbol.agregarHijoIzq(nodo2)
arbol.agregarHijoDer(nodo3)
nodo4 = ArbolBinario(4)
nodo5 = ArbolBinario(5)
nodo2.agregarHijoIzq(nodo4)
nodo2.agregarHijoDer(nodo5)
nodo6 = ArbolBinario(6)
nodo7 = ArbolBinario(7)
nodo3.agregarHijoIzq(nodo6)
nodo3.agregarHijoDer(nodo7)

print(arbol.porNiveles())