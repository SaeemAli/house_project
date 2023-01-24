import pandas as pd

df = pd.read_csv('london.csv')
postcode = pd.read_csv('London_postcodes.csv')

''' 
Price
Postcode
Area name
Number of bedrooms
URL of rightmove listing
Only use records where postcode is given
Use the postcode.csv to find area names 
'''

#Take the columns we need.
cleanDF = df[['price', 'postcode', 'number_bedrooms', 'url', 'address']]

#Take only rows where postcode was given
cleanDF['postcode'] = cleanDF['postcode'].fillna(-1)
cleanDF = cleanDF[cleanDF['postcode'] != -1]

postcodeUnique = cleanDF['postcode'].unique()

# Add the area names to the dataframe
for i in postcodeUnique:
    cleanDF['address'][cleanDF['postcode'] == i] = postcode['town'][postcode['postcode'] == i].iloc[0]


cleanDF.to_csv("cleanData.csv")