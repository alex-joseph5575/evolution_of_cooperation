print("importing...")
import axelrod as axl
from src.functions import *
import pandas as pd
print("Done.")

df = pd.read_csv("outputs/results_0.csv")
print(df.head(2))
print()

outputToCsv(df)