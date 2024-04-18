from .funciones import *
class grafo():
    def __init__(self) -> None:
        self.aristas = {}
        pass
    
    def addVertice(self,vertice):
        #self.aristas[vertice]={}
        if vertice not in self.aristas:
            self.aristas[vertice]= {}
        #pass
    
    
    #                   a       b       5
    def addArista(self,origen,destino,peso):
        """if origen not in self.aristas:
            self.addVertice(origen)
        if destino not in self.aristas:
            self.addVertice(destino)"""
        self.addVertice(origen)
        self.addVertice(destino)
        self.aristas[origen][destino] = peso
            
        # self.aristas[origen][destino] = peso
        self.aristas[origen].update({destino:peso})
        
    def printDicc(dicc):
        for i in dicc:
            print(f'Vertice: {i}')
            for j in dicc[i]:
                print(f'\tRel: {j}, peso: {dicc[i][j]}')
        return '' 

    def __str__(self) -> str:
        return printDicc(self.aristas)
    pass

    
