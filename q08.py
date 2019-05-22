##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd

tabla = pd.read_csv('tbl0.tsv', sep='\t')
tabla['ano'] = tabla['_c3'].str.split('-').str[0]
print (tabla)
