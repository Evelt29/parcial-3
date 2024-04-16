from lib import *
import pandas as pd

nombre_archivo = input('Nombre del achivo:')
df = pd.read_excel(nombre_archivo,index_col=0)
print('\033[35m Matriz de adyacencia\033[0m')
print(df)

diccRel = {}
grafoTest = grafo(df)
print(grafoTest)


vertices = df.columns.tolist()
aristas = []