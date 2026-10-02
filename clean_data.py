import pandas as pd
df = pd.read_csv('train.csv')
df['Postal Code'] = df['Postal Code'].fillna(df['Postal Code'].median())
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
df['State'] = df['State'].str.strip().str.title()
df.to_csv('cleaned_train.csv', index=False)
