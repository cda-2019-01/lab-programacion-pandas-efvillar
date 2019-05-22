##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 

import pandas as pd

tabla = pd.read_csv('tbl2.tsv', sep='\t')
tabla.sort_values('_c5a', inplace=True)

tabla['lista'] = tabla['_c5a']+":"+tabla['_c5b'].astype(str)
tabla2 = tabla.groupby('_c0')['lista'].apply(lambda x: ','.join(x))
tabla3 = pd.DataFrame({'_c0':tabla2.index, 'lista':tabla2.values})

print(tabla3)