import pandas as pd

# Sample extracted consumer data (replace this with the actual extracted data)
extracted_data = [
    (1, 'John Doe', '123 Main St', '555-123-4567', 'john.doe@email.com', 'ACCT123', 'MTR123', 'Tariff A', '2019-2023', 'Paid'),
    # Add more sample rows as needed
]

# Convert extracted data to a pandas DataFrame
df = pd.DataFrame(extracted_data, columns=['ConsumerID', 'Name', 'Address', 'ContactNumber', 'EmailAddress', 'AccountNumber', 'MeterNumber', 'TariffPlan', 'ConsumptionHistory', 'PaymentStatus'])

# Perform data mapping and transformation
df['First Name'] = df['Name'].apply(lambda x: x.split()[0])
df['Last Name'] = df['Name'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else '')
df['Address Line 1'] = df['Address']
df['Address Line 2'] = ''
# Add more mapping transformations as needed

# Drop redundant columns
df.drop(['Name', 'Address'], axis=1, inplace=True)

# Print the mapped data
print(df)
