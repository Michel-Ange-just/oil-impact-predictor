import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, 'data', 'raw', 'consumption_worldbank.csv')

print("BASE_DIR =", BASE_DIR)
print("file_path =", file_path)
print("exists?   =", os.path.exists(file_path))

df = pd.read_csv(file_path)
df = df[df["Country Code"] == "DEU"]
df = df.loc[:, "1960":"2024"]

df = df.T
df.columns = ["consumption"]
df.index.name = "year"
df.reset_index(inplace=True)



