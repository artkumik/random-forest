import pandas as pd

#importing the data as a csv and printing the first few results
data = pd.read_csv('UltraMarathon.csv')
print(data.head())

data.info()

fastest_athlete = data.sort_values(by="Athlete ID")
print(fastest_athlete.head())