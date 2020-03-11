import pandas as pd

data = pd.read_csv('./6153237444115dat.csv', na_values=['*', '**', '***', '****', '*****', '******'])

selected = data[['USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN']]

selected = selected.dropna(subset=['TEMP'])

kumpula = selected.ix[selected['USAF'] == 29980]
rovaniemi = selected.ix[selected['USAF'] == 28450]