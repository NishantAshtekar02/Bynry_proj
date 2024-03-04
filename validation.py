import pandas as pd
import pyodbc

# Define connection parameters for SMART360 database
server = 'smart360_server'
database = 'smart360_database'
username = 'smart360_username'
password = 'smart360_password'
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Function to perform validation and testing
def validate_and_test():
    try:
        # Establish connection to SMART360 database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        print("Connected to SMART360 database successfully!")

        # Query to fetch integrated consumer data from SMART360
        sql_query = """
            SELECT ConsumerID, FirstName, LastName, AddressLine1, AddressLine2, City, State, ZipCode, PhoneNumber, EmailAddress
            FROM ConsumerTable
        """

        # Fetch data from SMART360
        cursor.execute(sql_query)
        integrated_data = cursor.fetchall()

        # Convert fetched data into a DataFrame for easier validation
        df_integrated = pd.DataFrame(integrated_data, columns=['ConsumerID', 'FirstName', 'LastName', 'AddressLine1', 'AddressLine2', 'City', 'State', 'ZipCode', 'PhoneNumber', 'EmailAddress'])

        # Perform validation and testing
        # Example: Check for completeness by ensuring all columns have non-null values
        completeness_check = df_integrated.notnull().all().all()

        if completeness_check:
            print("Validation and testing passed: Integrated consumer data is complete.")
        else:
            print("Validation and testing failed: Integrated consumer data is incomplete.")

    except pyodbc.Error as e:
        print(f"Error connecting to SMART360 database: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Execute validation and testing function
validate_and_test()
