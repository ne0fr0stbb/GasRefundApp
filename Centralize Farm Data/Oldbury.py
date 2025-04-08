import pyodbc

# Path to your Access database
db_path = r"/\Oldbury11525.accdb"

# Define connection string
conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={db_path};"
)

# Connect to the database
conn = pyodbc.connect(conn_str)

# Create a cursor object
cursor = conn.cursor()

zone_info = []
history_temp = []

# Execute a query (e.g., fetch all rows from a table named 'HistoryUsed')
data = cursor.execute("SELECT * FROM GetInfoZones")

# Fetch and print results
for row in data:
    zone_info.append(row)

'''
data = cursor.execute("SELECT * FROM HistoryTemp")
for row in data:
    history_temp.append(row)
'''

#print(history_temp)
print("------------------------------------------------")
print(zone_info[0])

cursor.close()
conn.close()
