import pandas as pd

file_path = '/Users/akhilarekatika/Work/Projects/Power Bi Project/DataCoSupplyChainDataset.csv'
df = pd.read_csv(file_path, encoding='latin1')

print(f"Original shape: {df.shape}")

columns_to_remove = [
    'Customer Email', 'Customer Fname', 'Customer Lname', 'Customer Password',
    'Customer Street', 'Customer Zipcode', 'Order Zipcode',
    'Product Description', 'Product Image', 'Product Status'
]

df_cleaned = df.drop(columns=columns_to_remove)
print(f"After cleaning: {df_cleaned.shape}")

output_path = '/Users/akhilarekatika/Work/Projects/Power Bi Project/DataCoSupplyChainDataset_Cleaned.csv'
df_cleaned.to_csv(output_path, index=False)

print(f"Cleaned dataset saved as CSV at: {output_path}")
print(df['Order State'].unique())
print(df['Order City'].unique())
print(df['Order Country'].unique())
