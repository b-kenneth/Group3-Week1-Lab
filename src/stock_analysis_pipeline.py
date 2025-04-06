"""
data_analysis_pipeline.py

This script performs stock price analysis as a data analysis pipeline.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load stock price data from a CSV file."""
    return pd.read_csv(file_path)

def main():
    """Main execution pipeline."""
    # Add your file path and function calls here

if __name__ == "__main__":
    main()


import pandas as pd
import numpy as np
from datetime import datetime
import os

# Specify the directory containing your CSV files
directory = '../data/stocks'

# Create an empty list to store individual DataFrames
dataframes = []

# Loop through all CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Extract symbol from filename (remove .csv extension)
        symbol = filename.replace('.csv', '')
        
        # Load the CSV file
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        
        # Add a symbol column to identify the source
        df['symbol'] = symbol
        
        # Append to our list of dataframes
        dataframes.append(df)

# Concatenate all DataFrames in the list
df = pd.concat(dataframes, ignore_index=True)

# Display the first few rows of the merged DataFrame
df.head()


df.tail()

#checking the columns information(names & Data Types)
df.info()

df.shape

df.describe()

# Missing values in each column
missing_values = df.isnull().sum()
print("Missing Values by Column:")
print(missing_values)

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])


df.head()

df.info()

# The top 10 highest stocks 
top_10_stocks = df.sort_values(by='Close', ascending=False).head(10)

top_10_stocks

top_5_stocks = df.sort_values(by='Close', ascending=False).head(5)

print(top_5_stocks)

top5_by_company = df.groupby('symbol').apply(lambda x: x.nlargest(5, 'Close')).reset_index(drop=True)
top5_by_company

lowest5_by_company = df.groupby('symbol').apply(lambda x: x.nsmallest(5, 'Close')).reset_index(drop=True)
lowest5_by_company

# Check if High is always >= Low, Open, and Close
inconsistent_high = df[
    (df['High'] < df['Low']) | 
    (df['High'] < df['Open']) | 
    (df['High'] < df['Close'])
]

print(f"Number of rows where High is not the highest price: {len(inconsistent_high)}")
if len(inconsistent_high) > 0:
    print("Sample inconsistent rows:")
    print(inconsistent_high.head())

# Check if Low is always <= High, Open, and Close
inconsistent_low = df[
    (df['Low'] > df['High']) | 
    (df['Low'] > df['Open']) | 
    (df['Low'] > df['Close'])
]

print(f"Number of rows where Low is not the lowest price: {len(inconsistent_low)}")
if len(inconsistent_low) > 0:
    print("Sample inconsistent rows:")
    print(inconsistent_low.head())


duplicates = df.duplicated()


print(f"Number of duplicate rows: {duplicates.sum()}")

# Get the duplicate rows
duplicate_rows = df[duplicates]


print("\nDuplicate rows:")
print(duplicate_rows)

df.describe()

print("Original Column Names:")
print(df.columns.tolist())


# Convert to lowercase and replace spaces with underscores
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# Check the standardized column names
print("\nStandardized Column Names:")
print(df.columns.tolist())


# Save the cleaned dataset
df.to_csv('../data/cleaned_data.csv')

file_path = "../data/cleaned_data.csv"  # Update with your actual file path
df = pd.read_csv(file_path)

filtered = df[df['symbol'] == "YUMC"]


filtered

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Ensure 'date' column is datetime
filtered['date'] = pd.to_datetime(filtered['date'])

# Extract unique years from the date column
years = sorted(filtered['date'].dt.year.unique())

# Create list of dates corresponding to Jan 1st of each year (or approximate)
year_ticks = [pd.Timestamp(f'{year}-01-01') for year in years]

# Time series plot
plt.figure(figsize=(12,6))
plt.plot(filtered['date'], filtered['close'], label='Closing price', color='red')

# Set x-ticks to only those specific years
plt.xticks(ticks=year_ticks, labels=years)

plt.xlabel('Year')
plt.ylabel('Price')
plt.title('Yum China Holdings, Inc. Common Stock Closing Price Trend 2017-2020')
plt.legend()
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load stock data from local Parquet file
file_path = "../data/cleaned_data.csv"
df = pd.read_csv(file_path)

# Check the column names and data types
print(df.dtypes)

# Filter only the numeric columns for correlation matrix
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Compute correlation matrix
correlation_matrix = numeric_df.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Stock Price Correlation Heatmap")
plt.show()


