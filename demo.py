import pandas as pd

# Read a CSV file
data = pd.read_csv('sample_data.csv')

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Display summary statistics
print("\nSummary statistics:")
print(data.describe())

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Calculate the average of a specific column
average_value = data['Sales'].mean()
print(f"\nAverage Sales: {average_value}")
