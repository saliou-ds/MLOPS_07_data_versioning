import pandas as pd

# Read the dataset
df = pd.read_csv('data/wine_original.csv')

# Delete the first 200 lines
df = df.iloc[200:]

# Save the modified dataset
df.to_csv('data/wine_original.csv', index=False)