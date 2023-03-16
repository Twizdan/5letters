import pandas as pd

data = pd.read_csv("5letters.csv", index_col=0)["0"]
z = data.str.split("", expand=True)
print(z.head())
mas = [0] * 5
for i in range(1, 6):
    mas[i] = (z[i].value_counts(normalize=True))