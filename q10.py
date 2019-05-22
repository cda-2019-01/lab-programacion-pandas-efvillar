##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

import pandas as pd

tabla = pd.read_csv('tbl1.tsv', sep='\t')
tabla.sort_values('_c4', inplace=True)
tabla2 = tabla.groupby('_c0')['_c4'].apply(lambda x: ','.join(x))
tabla3 = pd.DataFrame({'_c0':tabla2.index, 'lista':tabla2.values})
print (tabla3)
