import pandas as pd
from sqlalchemy import create_engine

#extrat
url =  "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
df = pd.read_csv (url)
#print (df.head())

#tranform
df = df[df['Country'] == 'Brazil'].dropna()
df['Total Cases'] = df['Confirmed'].cumsum()
print(df.head())

#load
engine = create_engine('sqlite:///covid_data.bd')
df.to_sql('brasil_covid', engine, if_exists='replace', index=False)