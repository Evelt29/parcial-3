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

"""
origenG = 'B'
destinoG = 'H'
path = {origenG: {'prev': None, '-': 0}}
# 'prev' puse el prev para que devolviera el valor que tenía con el nodo anterior 
visitados = []
while destinoG not in visitados:
    verticeCH = min((t,j) for t, j in path.items() if t not in visitados)[0] # para el nodo con menor distancia, t = vertice y j = el valor o peso
    # vi que el min() ayuda a que te devuelva el valor más bajo de t que sería el vertice, aquí sería el valor con menor peso
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
    """
    
    
origenG = 'B'
destinoG = 'H'
path = {}
visitados = []
path[origenG] = {'-': 0}
llaves = grafoTest.aristas[origenG].keys()

# Crear la estructura de datos inicial del camino más corto
for i in llaves:
    path[i] = {origenG: grafoTest.aristas[origenG][i]}

print("primer iteración:")
print(visitados)
print(path)

# Iniciar el algoritmo para encontrar el camino más corto
verticeAct = origenG
visitados.append(verticeAct)
llaves = grafoTest.aristas[verticeAct].keys()

for i in llaves:
    if i not in visitados:
        if i not in path:
            path[i] = {}
        llave = list(path[verticeAct].keys())
        acumulado = path[verticeAct][llave[0]]
        path[i].update({verticeAct: grafoTest.aristas[verticeAct][i] + acumulado})
        # Revisar si hay más de dos llaves en una llave del path
        if len(path[i]) == 2:
            kiss = list(path[i].keys())
            if kiss[0] < kiss[1]:
                del (path[i][kiss[1]])

# Continuar con el algoritmo hasta que el destino esté en los visitados
while destinoG not in visitados:
    verticeCH = min((t, j) for t, j in path.items() if t not in visitados)[0]
    if '-' not in path[verticeCH]: # para que cada path tenga '-'
        path[verticeCH]['-'] = float('inf') # para un valor determinado
    distanciaCH = path[verticeCH]['-']
    
    visitados.append(verticeCH)

    for vecino, peso in grafoTest.aristas[verticeCH].items():
        nuevo_peso = distanciaCH + peso
        if vecino not in path or nuevo_peso < path[vecino].get('-',float('inf')):
            
            
            
            
            path[vecino] = {'prev': verticeCH, '-': nuevo_peso}

# Reconstruir el camino más corto desde el destino hasta el origen
if destinoG in visitados:
    camino_corto = []
    peso_total = path[destinoG]['-']
    actual = destinoG
    while actual is not None:  # Continuar mientras haya un nodo anterior
        camino_corto.append(actual)
        actual = path[actual].get('prev', None)
    if camino_corto[-1] == origenG:  # Verificar si el último nodo en el camino es el origen
        camino_corto.reverse()  # Revertir el camino para obtener la secuencia correcta
        print("Camino corto:", camino_corto)
        print("Peso total:", peso_total)
    else:
        print("No hay camino desde el origen al destino.")
else:
    print("No hay camino desde el origen al destino.")


