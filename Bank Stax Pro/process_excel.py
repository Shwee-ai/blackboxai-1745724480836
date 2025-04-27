import pandas as pd

# Read the Excel file
df = pd.read_excel('Line items latest (1).xlsx')

# Get the column names from the first row
columns = df.iloc[0].tolist()
columns[0] = 'Bank Name'  # Fix the first column name

# Create new dataframe with proper column names
df_clean = df.iloc[1:].copy()
df_clean.columns = columns

# Save to Excel
df_clean.to_excel('financial-dashboard/data/bank_data.xlsx', index=False)

print("Processed columns:", df_clean.columns.tolist())
print("\nFirst few rows:")
print(df_clean.head())
