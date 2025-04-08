import pyodbc
from datetime import datetime, timedelta

# Path to your Access database
access_db_path = r"C:\Users\Jason\Desktop\Farm Ventra Databases\Guinea071223.accdb"

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

# Connect to the Access database
access_conn = pyodbc.connect(access_conn_str)
access_cursor = access_conn.cursor()

# Connect to the SQL Express database
sql_server_conn = pyodbc.connect(sql_server_conn_str)
sql_server_cursor = sql_server_conn.cursor()

# Calculate the date one week ago
one_day_ago = datetime.now() - timedelta(days=1)
one_day_ago_str = one_day_ago.strftime('%m-%d-%Y')

# Fetch data from Access database that is less than one week old
zone_info = []
access_data = access_cursor.execute("SELECT * FROM HistoryRuntime WHERE DeviceName = 'Feed Sensor Run Time' "
                                    "and TheDate >= ?", one_day_ago_str)
for row in access_data:
    zone_info.append(row)

# Prepare queries
insert_query = ("INSERT INTO RuntimeHistory (Farm, ControllerID, ZoneNum, DayTime, TheDate, TheHour,"
                "RecType, DeviceName, Device1Run, Device2Run, Device3Run, Device4Run, Device5Run)"
                " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
update_query = ("UPDATE RuntimeHistory SET ZoneNum = ?, DayTime = ?, TheDate = ?, TheHour = ?, "
                "RecType = ?, DeviceName = ?, Device1Run = ?, Device2Run = ?, Device3Run = ?, "
                "Device4Run = ?, Device5Run = ? WHERE ControllerID = ? AND ZoneNum = ?")
select_query = "SELECT COUNT(*) FROM RuntimeHistory WHERE TheDate >= ? and DeviceName = 'Feed Sensor Run Time'"

# Start a transaction
sql_server_conn.autocommit = False

server_data = []
selected_data = sql_server_cursor.execute("SELECT * FROM RuntimeHistory WHERE TheDate >= ?", one_day_ago_str)
for data_row in selected_data:
    server_data.append(data_row)

try:
    for row in zone_info:
        for data in server_data:
            if row.DayTime == data.DayTime and row.TheHour == data.TheHour and data.Farm == "Guinea":
                break
        else:
            # Record does not exist, insert it
            sql_server_cursor.execute(insert_query, "Guinea", row.ControllerID, row.ZoneNum, row.DayTime, row.TheDate,
                                      row.TheHour, row.RecType, row.DeviceName, row.Device1Run, row.Device2Run,
                                      row.Device3Run, row.Device4Run, row.Device5Run)

    sql_server_conn.commit()

except Exception as e:
    # Rollback the transaction in case of error
    sql_server_conn.rollback()
    raise e
finally:
    # Close all connections
    access_cursor.close()
    access_conn.close()
    sql_server_cursor.close()
    sql_server_conn.close()