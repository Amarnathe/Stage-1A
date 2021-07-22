import pandas as pd

data = pd.read_csv("data_copie.csv")
str1 = ''.join(data["Notes"].tolist())
print(str(data["Notes"].tolist()[0])=="nan")
print(str1)