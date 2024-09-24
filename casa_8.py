import pandas as pd

# Data frame
df = pd.read_csv('big-mac-full-index.csv' )


print("Given Dataframe :\n", df)

print("\nIterating over rows using iterrows() method :\n")


# Just show the first 10 dont need to see the whole thing
limit = 10 
# naming index and row and using iterrows in the dataframe
for index,row in df.iterrows():
    if index >= limit:
        break
    print(f'row{index} data:')
    print(f"Name: {row['name']}, Currency Code: {row['currency_code']}")

# data = {'Name': ['Argentina','Australia', 'Brazil', 'Canada'],
    #    'currency_code': ['ARS','AUD','BRL','CAD'],
    #     'local_price': [2.5,2.59,2.95,2.85],
    #      'CNY_adjusted': [0.96883,0.01031,0.33548,0.30204]}


