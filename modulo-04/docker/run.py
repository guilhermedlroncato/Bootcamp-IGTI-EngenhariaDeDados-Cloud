import pandas as pd

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv'

df =  pd.read_csv(url, header = None)

df['nova_coluna'] = df[5] * 2

print(df.columns)

print(df.head())

print(df.shape)