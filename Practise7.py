import pyodbc
import pandas as pd

conc_string='driver={sql server}; server=DEVBISQL01\DEVR1;database=dwcore;trusted_connection=yes;' 
query='select * from information_schema.tables' 
conx=pyodbc.connect(conc_string) 
print(conx) 
df = pd.read_sql(query, conx)
print(df)

# Corrected connection string syntax
conn_string = 'DRIVER={SQL Server};SERVER=DEVBISQL01\\DEVR1;DATABASE=dwcore;Trusted_Connection=yes;'

# Corrected query and connection handling
query = 'SELECT * FROM INFORMATION_SCHEMA.TABLES'
try:
    # Establishing connection
    conx = pyodbc.connect(conn_string)
    print("Connection successful:", conx)
    
    # Using pandas to execute the query and fetch data into a DataFrame
    df = pd.read_sql(query, conx)
    print(df)
finally:
    # Ensure the connection is properly closed
    conx.close()