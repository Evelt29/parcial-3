from lib import *
import pandas as pd

"""nombre_archivo = input('Nombre del achivo:')
df = pd.read_excel(nombre_archivo,index_col=0)
print('\033[35m Matriz de adyacencia\033[0m')"""
print('\033[35m Matriz de adyacencia\033[0m')
print(df)
print('\033[32m Lista de relaciones:\033[0m')
for arista in aristas:
    print(f"{arista[0]} -> Destino: {arista[1]} : Peso {arista[2]}")

grafo_test = grafo()
for origen, destino, peso in aristas:
    grafo_test.addArista(origen, destino, peso)
    
print("\033[33m Grafo:\033[0m")
print(grafo_test)