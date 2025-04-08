import pyodbc

# Path to your Access database
access_db_path = r"/\Oldbury11525.accdb"

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

# Fetch data from Access database
zone_info = []
access_data = access_cursor.execute("SELECT * FROM GetInfoZones")
for row in access_data:
    zone_info.append(row)

# Insert data into SQL Express database
insert_query = ("INSERT INTO OldburyZoneInfo (ControllerID, ZoneID, ZoneName, ZoneNum, SetpointTemp,"
                "TodayAnimalAge, WeightToday, ZoneState, EETTemp, AvgRH, HeatStress, WorkTemp, StaticPressure,"
                "OutsideTemp, LastDownloaded) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
for row in zone_info:
    print(f"Inserting: {row.ControllerID}, {row.ZoneID}, {row.ZoneName}, {row.ZoneNum}, {row.SetpointTemp}, "
          f"{row.TodayAnimalAge}, {row.WeightToday}, {row.ZoneState}, {row.EETTemp}, {row.AvgRH},"
          f" {row.HeatStress}, {row.WorkTemp}, {row.StaticPressure}, {row.OutsideTemp}, {row.LastDownloaded}")

    sql_server_cursor.execute(insert_query, row.ControllerID, row.ZoneID, row.ZoneName, row.ZoneNum,
                              row.SetpointTemp, row.TodayAnimalAge, row.WeightToday, row.ZoneState,
                              row.EETTemp, row.AvgRH, row.HeatStress, row.WorkTemp, row.StaticPressure,
                              row.OutsideTemp, row.LastDownloaded)

# Commit the transaction
sql_server_conn.commit()

# Close all connections
access_cursor.close()
access_conn.close()
sql_server_cursor.close()
sql_server_conn.close()