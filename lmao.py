import pyodbc
# Establecer la cadena de conexión
server = 'pc-11'
database = 'matricula'
username = 'sa'
password = 'S@123456'
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
# Conectar a la base de datos

nuevo_valor_col1 = '55555555'
nuevo_valor_col2 = 'Arena para gatos'
nuevo_valor_col3 = '$25.5'
nuevo_valor_col4 = '2024-06-25'

nuevo_valor = '$2.5'
condicion = 'cod_produc=22222222'

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    sql_query = f"UPDATE Productos SET precio_produc = '{nuevo_valor}' WHERE {condicion}"

    sql_query = f"INSERT INTO Productos (cod_produc, nom_produc, precio_produc, fech_nac_produc) VALUES ('{nuevo_valor_col1}', '{nuevo_valor_col2}', '{nuevo_valor_col3}', '{nuevo_valor_col4}')"
    cursor.execute(sql_query)

    cod_produc=22222222
    cursor.execute(sql_query)

    conn.commit()
    print("Actualización exitosa")

except Exception as e:
    print(f'Error de conexión: {str(e)}')


finally:
# Cerrar la conexión
    if conn:
        conn.close()