import pandas as pd
import csv

df = pd.read_csv("final.csv")

df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)

file_data = df.dropna()
file_data.reset_index(drop=True,inplace = True)

file_data.to_csv("main.csv")
