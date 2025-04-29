import pandas as pd

df = pd.read_csv("../Csv/temperature.csv")

df.head(3)

print(df)

df.dtypes

df['year']= pd.to_datetime(df['year'])

df = df.set_index('year')
print(df.index)

df.describe()