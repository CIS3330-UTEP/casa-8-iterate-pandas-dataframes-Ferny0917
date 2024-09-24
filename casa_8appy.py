import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

s = df['local_price'].squeeze()

def fun(curr):
    curr = float (curr)
    if curr < 3:
        return "Low"
    elif  3 <= curr <6:
        return "Normal"
    else:
        return "High"
    
new = s.apply(fun)

print(new.head(5))

print(new.tail(3))