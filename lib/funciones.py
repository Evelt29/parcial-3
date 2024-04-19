from .clases import *
import pandas as pd
def printDicc(dicc):
    for i in dicc:
        print(f'Vertice: {i}')
        for j in dicc[i]:
            print(f'\tRel: {j}, peso: {dicc[i][j]}')
    return ''

nombre_archivo = input('Nombre del achivo:')
df = pd.read_excel(nombre_archivo,index_col=0)


aristas = [
    (origen, destino, peso)
    for origen in df.index
    for destino, peso in df.loc[origen].items()
    if pd.notna(peso) and peso != 0
]

print('\033[32m Lista de relaciones:\033[0m')
for arista in aristas:
    print(f"{arista[0]} -> Destino: {arista[1]} : Peso {arista[2]}")







"""def printMat(df):
    nombre_archivo = input('Nombre del achivo:')
    df = pd.read_excel(nombre_archivo,index_col=0)
    print('\033[35m Matriz de adyacencia\033[0m')
    print(df)
    
vertices = df.columns.tolist()      
vertices = []
for index, row in df.iterrows():
    vertices.append(row.name)"""    
"""def lis(df):
    array =[]
    for origen, row in df.iterrows():
        for destino, peso in row.items():
            if pd.notna(peso):
                array.append((origen, destino, peso))
    return array
    """
    