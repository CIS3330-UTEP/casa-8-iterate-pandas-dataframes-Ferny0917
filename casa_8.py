import pandas as pd

df = pd.read_csv('big-mac-full-index.csv' )

s = pd.read_csv('big-mac-full-index.csv', squeeze=True)

print("Given Dataframe :\n", df)

print("\nIterating over rows using iterrows() method :\n")

limit = 10 
for index,row in df.iterrows():
    if index >= limit:
        break
    print(f'row{index} data:')
    print(f"Name: {row['name']}, Currency Code: {row['currency_code']}")

# data = {'Name': ['Argentina','Australia', 'Brazil', 'Canada'],
    #    'currency_code': ['ARS','AUD','BRL','CAD'],
    #     'local_price': [2.5,2.59,2.95,2.85],
    #      'CNY_adjusted': [0.96883,0.01031,0.33548,0.30204]}


def fun(curr):
    if curr < 1:
        return "Low"
    elif curr >= 2 and curr <3:
        return "Normal"
    else:
        return "High"
    
new = s.apply(fun)

print(new.head(5))

print(new[1], new[2],new[3])

print(new.tail(3))