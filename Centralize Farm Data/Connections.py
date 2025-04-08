import pyodbc


def get_connection_strings(database):
    """
    Returns the connection strings for Access and SQL Express databases.
    """
    # Path to your Access database
    access_db_path = r"C:\Users\Jason\Desktop\Farm Ventra Databases\?.accdb", format(database)

    # Define connection string for Access database
    access_conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        rf"DBQ={access_db_path};"
    )

    # Define connection string for SQL Express database
    sql_server_conn_str = (
        r"DRIVER={SQL Server};"
        r"SERVER=CMF-IT-LAP-2\SQLEXPRESS;"
        r"DATABASE=FarmData;"
        r"Trusted_Connection=yes;"
    )

    return access_conn_str, sql_server_conn_str


def connect_to_databases(database):
    """
    Connects to the Access and SQL Express databases and returns the connection objects.
    """
    access_conn_str, sql_server_conn_str = get_connection_strings(database)

    # Connect to the Access database
    access_conn = pyodbc.connect(access_conn_str)
    access_cursor = access_conn.cursor()

    # Connect to the SQL Express database
    sql_server_conn = pyodbc.connect(sql_server_conn_str)
    sql_server_cursor = sql_server_conn.cursor()

    return access_conn, access_cursor, sql_server_conn, sql_server_cursor


def close_connections(access_conn, access_cursor, sql_server_conn, sql_server_cursor):
    """
    Closes the database connections.
    """
    access_cursor.close()
    access_conn.close()
    sql_server_cursor.close()
    sql_server_conn.close()


