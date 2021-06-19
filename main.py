import pandas as pd
import csv

df = pd.read_csv("final.csv")

del df["Luminosity"]

df.dropna()

df.to_csv("main.csv")
