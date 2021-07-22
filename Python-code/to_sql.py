import pandas as pd

data = pd.read_csv("data_copie.csv")

# dropping null value columns to avoid errors
data.dropna(inplace=True)

# substring to be searched
word = 'vivre'

# start var
start = 2

# creating and passing series to new column
data["vivre"] = data["Citations"].str.find(word, start)

# display
print(data)
