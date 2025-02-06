import pyodbc
import  pandas as pd

conc_string='driver={sql server}; server=DEVBISQL01\DEVR1;database=dwcore;trusted_connection=yes;'
query='select * from information_schema.tables'
conx=pyodbc.connect(conc_string)

query="select * from information_schema.tables"
print(query)
df = pd.read_sql(query, conc_string)
print(df)