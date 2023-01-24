import pandas as pd

df = pd.read_csv('postcodes.csv')
df['town'] = df['town'].fillna(-1)
df = df[df['town'] != -1]
df = df[df['region'] == "Greater London"]
df.to_csv("London_postcodes.csv")
