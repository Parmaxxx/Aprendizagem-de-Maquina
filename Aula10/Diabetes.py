import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('../Csv/pima-data.csv', sep=',')

print(df.head())

print(df.describe())

