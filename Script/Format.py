import pandas as pd

# Read the file
file_path = '/Users/akhilarekatika/Work/Projects/Power Bi Project/DataCoSupplyChainDataset_Cleaned.csv'
df = pd.read_csv(file_path, encoding='latin1')

# Define your columns
columns_to_clean = ["Order City", "Order State", "Order Country"]

# Define common replacements
replace_map = {
    'Ã¡': 'á', 'Ã¢': 'â', 'Ã¤': 'ä', 'Ã£': 'ã', 'Ã': 'Á', 'Ã‚': 'Â', 'Ã„': 'Ä', 'Ãƒ': 'Ã',
    'Ã©': 'é', 'Ãª': 'ê', 'Ã«': 'ë', 'Ã‰': 'É', 'ÃŠ': 'Ê', 'Ã‹': 'Ë',
    'Ã­': 'í', 'Ã®': 'î', 'Ã¯': 'ï', 'Ã': 'Í', 'ÃŽ': 'Î', 'Ã': 'Ï',
    'Ã³': 'ó', 'Ã´': 'ô', 'Ã¶': 'ö', 'Ãµ': 'õ', 'Ã“': 'Ó', 'Ã”': 'Ô', 'Ã–': 'Ö', 'Ã•': 'Õ',
    'Ãº': 'ú', 'Ã»': 'û', 'Ã¼': 'ü', 'Ãš': 'Ú', 'Ã›': 'Û', 'Ãœ': 'Ü',
    'Ã±': 'ñ', 'Ã‘': 'Ñ',
    'Ã§': 'ç', 'Ã‡': 'Ç',
    'Ã ': 'à', 'Ã€': 'À',
    'Ã¨': 'è', 'Ã‰': 'É', 'Ã€': 'À',
}

# Function to clean a single value
def clean_text(text):
    for bad, good in replace_map.items():
        text = text.replace(bad, good)
    return text

# Apply cleaning
for col in columns_to_clean:
    if col in df.columns:
        df[col] = df[col].astype(str).apply(clean_text)

# Save cleaned file
df.to_csv("cleaned.csv", index=False)
print("✅ Dataset cleaned and saved as 'your_dataset_cleaned.csv'")
