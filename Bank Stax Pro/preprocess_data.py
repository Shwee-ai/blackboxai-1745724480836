import pandas as pd
import numpy as np

def calculate_ratios(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate financial ratios from raw data."""
    df_with_ratios = df.copy()
    
    # Calculate Core Deposits to Total Deposits ratio
    if 'Core Deposits' in df.columns and 'Total Deposits' in df.columns:
        df_with_ratios['Core Deposits to Total Deposits'] = df['Core Deposits'] / df['Total Deposits']
    
    # Calculate NPAs to Total Loans ratio
    if 'Non performing assets' in df.columns and 'Loans' in df.columns:
        df_with_ratios['NPAs to Total Loans'] = df['Non performing assets'] / df['Loans']
    
    # Calculate Loans to Deposit ratio
    if 'Loans' in df.columns and 'Total Deposits' in df.columns:
        df_with_ratios['Loans to Deposit Ratio'] = df['Loans'] / df['Total Deposits']
    
    # Calculate Solvency Ratio
    if 'Total Assets' in df.columns and 'Total Liabilities (excluding equity)' in df.columns:
        df_with_ratios['Solvency Ratio'] = df['Total Assets'] / df['Total Liabilities (excluding equity)']
    
    return df_with_ratios

# Read the original data
print("Reading original data...")
df = pd.read_excel('data/bank_data.xlsx')
print("\nOriginal columns:", df.columns.tolist())

# Calculate ratios
print("\nCalculating ratios...")
df_processed = calculate_ratios(df)
print("\nProcessed columns:", df_processed.columns.tolist())

# Save processed data
print("\nSaving processed data...")
df_processed.to_excel('data/bank_data_processed.xlsx', index=False)
print("Done!")

# Print first few rows of processed data
print("\nFirst few rows of processed data:")
print(df_processed.head())
