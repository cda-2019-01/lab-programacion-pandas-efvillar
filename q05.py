##
## Imprima la suma de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd

tabla = pd.read_csv('tbl0.tsv', sep='\t')
tabla1 = tabla.groupby('_c1')['_c2'].sum()
print (tabla1)
