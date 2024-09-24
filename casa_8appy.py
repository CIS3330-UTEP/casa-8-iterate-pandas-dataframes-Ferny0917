import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

s = df['local_price'].squeeze()

# checking whats prices of local price

def fun(curr):
    curr = float (curr)
    if curr < 3:
        return "Low"
    elif  3 <= curr <6:
        return "Normal"
    else:
        return "High"
    
new = s.apply(fun)

#print First 5 element
print(new.head(5))

#print last  5 elemnts
print(new.tail(5))