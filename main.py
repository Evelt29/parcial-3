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

grafoTest = grafo()
for origen, destino, peso in aristas:
    grafoTest.addArista(origen, destino, peso)
    
print("\033[33m Grafo:\033[0m")
print(grafoTest)




origenG = 'B'
destinoG = 'H'
path = {}
visitados = []
path[origenG]= {'-':0}
llaves = grafoTest.aristas[origenG].keys()
print(llaves)

for i in llaves:
    path[i]={origenG: grafoTest.aristas[origenG][i]}
    
print("primer iter:")   
print(visitados)
print(path)

verticeAct = 'B'
visitados.append(verticeAct)
llaves = grafoTest.aristas[verticeAct].keys()
print(llaves)
for i in llaves:
    if i not in visitados:
        if i not in path: path[i] = {}
        llave = list(path[verticeAct].keys())
        acumulado = path[verticeAct][llave[0]]
        path[i].update({verticeAct: grafoTest.aristas[verticeAct][i]+ acumulado})
        # reviso si hay más de dos llaves en una llave del path
        if len(path[i])== 2:
            kiss = list(path[i].keys())
            if kiss [0] < kiss[1]:
                del(path[i][kiss [1]])
            pass
    # fin if not in visitados
# fin for i
   
        
print(path)
exit()