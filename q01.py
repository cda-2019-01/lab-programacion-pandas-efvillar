##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
import pandas as pd

tabla = pd.read_csv('tbl0.tsv', sep='\t')

#print (tabla)

tabla1=tabla['_c1'].value_counts()
#print(type(tabla1))
tabla1 = tabla1.sort_index()
tabla1.index.names = ['_c1']
print(tabla1)