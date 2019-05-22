##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 


import pandas as pd

tabla = pd.read_csv('tbl2.tsv', sep='\t')
tabla.sort_values('_c5a', inplace=True)
tabla1 = tabla.groupby('_c5a')['_c5b'].sum()
print (tabla1)