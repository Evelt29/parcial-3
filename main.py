from lib import *
import pandas as pd

"""nombre_archivo = input('Nombre del achivo:')
df = pd.read_excel(nombre_archivo,index_col=0)
print('\033[35m Matriz de adyacencia\033[0m')"""
print('\033[35m Matriz de adyacencia\033[0m')
print(df)



grafoTest = grafo()
for origen, destino, peso in aristas:
    grafoTest.addArista(origen, destino, peso)
    
print("\033[33m Grafo:\033[0m")
print(grafoTest)



# dejé el código pero no lo da, marca error en una línea donde no hay texto y no supe :((
origenG = 'B'
destinoG = 'H'
path = {origenG: {'prev': None, '-': 0}}
# 'prev' puse el prev para que devolviera el valor que tenía con el nodo anterior 
visitados = []
while destinoG not in visitados:
    verticeCH = min((t,j) for t, j in path.items() if t not in visitados)[0] # para el nodo con menor distancia, t = vertice y j = el valor o peso
    # el min() ayuda a que te devuelva el valor más bajo de t que sería el vertice, aquí sería el valor con menor peso
    distanciaCH = path[verticeCH]['-']# distanciaCH = distancia más pequeña 
    
    visitados.append(verticeCH)
    
    for vecino, peso in grafoTest.aristas[verticeCH].items():
        if vecino not in visitados:
            pesoN = distanciaCH + peso
            if vecino not in path or pesoN < path[vecino]['-']:
                path[vecino] = {'prev': verticeCH, '-': pesoN}
                
if destinoG in visitados:
    camino = []
    Pesot = path[destinoG]['-']
    actual = destinoG
    while actual != origenG:
        camino.append(actual)
        actual = path[actual]['prev']
    camino.append(origenG)
    camino.reverse()
    print(f"\033[36m camino corto:\033[0m {camino} ")
    print(f"Peso total: {Pesot}")


 