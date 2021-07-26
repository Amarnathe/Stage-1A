import pandas as pd

data = pd.read_csv("data_copie.csv")

print(len(data["Notes"].tolist()))
a = ["a", "b"]
if "a" in a:
    print("yes")