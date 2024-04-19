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




"""origenG = 'B'
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
   
        
#print(path)
print("path:")
for t in path.keys():
    print(f"{t}: {path[t]}")
    
#camino más corto
camino_corto = []
peso_total = 0
actual = destinoG
while actual != origenG:
    anterior = path[actual].get('prev',None)
    if path[actual]:
        anterior = list(path[actual].keys())[0] # marca error en path
    #anterior = list(path[actual].keys())[0]
    peso_total += path[actual][anterior]
    camino_corto.append(actual)
    actual = anterior
camino_corto.reverse()
print(f"Camino corto: {camino_corto}")
print(f"Peso total: {peso_total}")
"""


origenG = 'B'
destinoG = 'H'
path = {origenG: {'prev': None, '-': 0}}
# 'prev' puse el prev para que devolviera el valor que tenía con el nodo anterior 
visitados = []
while destinoG not in visitados:
    verticeCH = min((t,j) for t, j in path.items() if t not in visitados)[0] # para el nodo con menor distancia, t = vertice y j = el valor o peso
    # vi que el min() ayuda a que te devuelva el valor más bajo, aquí sería el valor con menor peso
    distanciaCH = path[verticeCH]['-']# distanciaCH = distancia más pequeña 
    
    visitados.append(verticeCH)
    
    for vecino, peso in grafoTest.aristas[verticeCH].items():
        if vecino not in visitados:
            newPeso = distanciaCH + peso
            if vecino not in path or newPeso < path[vecino]['-']:
                path[vecino] = {'prev': verticeCH, '-': newPeso}
                
if destinoG in visitados:
    camino = []
    Pesot = path[destinoG]['-']
    actual = destinoG
    while actual != origenG:
        camino.append(actual)
        actual = path[actual]['prev']
    camino.append(origenG)
    camino.reverse()
    print(f"\033[33m camino corto:\033[0m {camino} ")
    print(f"Peso total: {Pesot}")
else:
    print("NO HAY :( )")
    