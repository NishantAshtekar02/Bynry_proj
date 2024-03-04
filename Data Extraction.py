import pyodbc

# Define connection parameters
server = 'smart360_server'
database = 'smart360_database'
username = 'smart360_username'
password = 'smart360_password'

# Establish connection to the database
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'
try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Connected to the database successfully!")
except pyodbc.Error as e:
    print(f"Error connecting to the database: {e}")
    exit()

# SQL query to extract consumer data
sql_query = """
    SELECT ConsumerID, Name, Address, ContactNumber, EmailAddress, AccountNumber, MeterNumber, TariffPlan, ConsumptionHistory, PaymentStatus 
    FROM ConsumerTable
"""

try:
    # Execute the query
    cursor.execute(sql_query)
    
    # Fetch all rows
    consumer_data = cursor.fetchall()
    
    # Print the retrieved data
    for row in consumer_data:
        print(row)
except pyodbc.Error as e:
    print(f"Error executing SQL query: {e}")

# Close the cursor and connection
cursor.close()
conn.close()
