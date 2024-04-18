from .funciones import *
class grafo:
    def __init__(self):
        self.aristas = {}

    def addVertice(self, vertice):
        self.aristas[vertice] = {}

    def addArista(self, origen, destino, peso):
        if origen not in self.aristas:
            self.addVertice(origen)
        if destino not in self.aristas:
            self.addVertice(destino)
        self.aristas[origen].update({destino: peso})


    def __str__(self):
        return printDicc(self.aristas)