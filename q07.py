##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd

tabla = pd.read_csv('tbl0.tsv', sep='\t')
tabla['suma'] = tabla['_c0']  + tabla['_c2'] 
print (tabla)