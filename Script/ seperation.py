import pandas as pd


# Read the file
file_path = '/Users/akhilarekatika/Work/Projects/Power Bi Project/DHL Project/Shipping.csv'
# Load dataset
df = pd.read_csv(file_path, encoding='latin1')
# Inspect the column name
col = "shipping date (DateOrders)"

# Convert to datetime (if not already), then extract date part
df[col] = pd.to_datetime(df[col], errors='coerce').dt.date

# Optional: save back to CSV
df.to_csv("shipping_cleaned_dates.csv", index=False)

print("✅ Order date converted to date-only and saved as 'your_dataset_cleaned_dates.csv'")

