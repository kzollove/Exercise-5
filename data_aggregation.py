import pandas as pd
import dateutil

# create a new DataFrame where you have calculated mean, max and min temperatures
# for each day separately using the hourly values from Rovaniemi and Helsinki Kumpula.
# this problem is a classical data aggregation problem

data = pd.read_csv('./6153237444115dat.csv', na_values=['*', '**', '***', '****', '*****', '******'])

selected = data[['USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN']]

selected = selected.dropna(subset=['TEMP'])

selected['datetime'] = pd.to_datetime(selected['YR--MODAHRMN'], format="%Y%m%d%H%M")

selected = selected.set_index('datetime')

kumpula = selected.ix[selected['USAF'] == 29980]
rovaniemi = selected.ix[selected['USAF'] == 28450]

kumpula = kumpula.resample('D').mean()
rovaniemi = rovaniemi.resample('D').mean()


print(kumpula.head())