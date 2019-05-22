##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd

tabla = pd.read_csv('tbl1.tsv', sep='\t')
#print (tabla)
tabla['_c4'] = tabla['_c4'].apply(lambda x:x.upper())
unicos = tabla['_c4'].unique()
unicos.sort(axis=0)
unicos = list(unicos)

print (unicos)
#print (type(unicos))
