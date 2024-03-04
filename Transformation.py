import pandas as pd
import pyodbc

# Sample mapped consumer data (replace this with the actual mapped data)
mapped_data = [
    (1, 'John', 'Doe', '123 Main St', '', 'City', 'State', '12345', '555-123-4567', 'john.doe@email.com'),
    # Add more sample rows as needed
]

# Convert mapped data to a pandas DataFrame
df_mapped = pd.DataFrame(mapped_data, columns=['ConsumerID', 'First Name', 'Last Name', 'Address Line 1', 'Address Line 2', 'City', 'State', 'Zip Code', 'Phone Number', 'Email Address'])

# Establish connection to SMART360 database
server = 'smart360_server'
database = 'smart360_database'
username = 'smart360_username'
password = 'smart360_password'
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Connected to SMART360 database successfully!")
except pyodbc.Error as e:
    print(f"Error connecting to SMART360 database: {e}")
    exit()

# Define SQL query to insert data into SMART360 consumer table
sql_insert_query = """
    INSERT INTO ConsumerTable (ConsumerID, FirstName, LastName, AddressLine1, AddressLine2, City, State, ZipCode, PhoneNumber, EmailAddress)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

try:
    # Loop through each row of the DataFrame and insert data into the SMART360 consumer table
    for index, row in df_mapped.iterrows():
        cursor.execute(sql_insert_query, tuple(row))
        conn.commit()
    
    print("Data loaded into SMART360 consumer table successfully!")
except pyodbc.Error as e:
    print(f"Error inserting data into SMART360 consumer table: {e}")

# Close the cursor and connection
cursor.close()
conn.close()
