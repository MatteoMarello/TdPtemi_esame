import mysql.connector
from time import time

N = 1000

# NO POOLING
start_time = time()
for i in range(1,N):
    cnx = mysql.connector.connect(host = "127.0.0.1", user = 'root', password = 'Juventus1.',database = 'iscritticorsi')
    cursor = cnx.cursor()
    query = """SELECT * FROM corso"""
    cursor.execute(query)
    row = cursor.fetchall()
    cursor.close()
    cnx.close()

end_time = time()
print(f'Elapsed time without pooling =  {end_time-start_time}')



# POOLING
start_time = time()
cnx_pool = mysql.connector.pooling.MySQLConnectionPool(host = "127.0.0.1", user = 'root', password = "Juventus1.", database = 'iscritticorsi', pool_size=3, pool_name="mypool")
# Aggiungo due parametri aggiuntivi --> pool_size e pool_name.

for i in range(1,N):
    cnx = cnx_pool.get_connection()
    cursor = cnx.cursor()
    query = """SELECT * FROM corso"""
    cursor.execute(query)
    row = cursor.fetchall()
    cursor.close()
    cnx.close()

end_time = time()
print(f'Elapsed time with pooling =  {end_time-start_time}')
