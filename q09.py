##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 

import pandas as pd

tabla = pd.read_csv('tbl0.tsv', sep='\t')
tabla.sort_values('_c2', inplace=True)
tabla['_c2'] = tabla['_c2'].apply(str)

tabla2 = tabla.groupby('_c1')['_c2'].apply(lambda x: ':'.join(x))
tabla3 = pd.DataFrame({'_c0':tabla2.index, 'lista':tabla2.values})
print (tabla3)