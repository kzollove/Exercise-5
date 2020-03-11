import pandas as pd

###### Problem 1 #######

data = pd.read_csv('./6153237444115dat.csv', na_values=['*', '**', '***', '****', '*****', '******'])

#How many rows are in this data? 
print('Number rows: ', data.index)

#What are the column names?
print('Column names: ',data.columns)

#Datatypes of columns? 
print(data.dtypes)

#Mean F temp of Data?
print('Mean F Temp: ',data['TEMP'].mean())

#Std dev of max temp?
print('Std dev of Max temp: ', data['MAX'].describe())

#Number unique stations? 
print('Number of unique station: ', len(data['USAF'].unique()))




###### Problem 2 #######

#Select from the data columns USAF, YR--MODAHRMN, TEMP, MAX, MIN and assign them into a new variable called selected

selected = data[['USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN']]

#Remove all rows from selected that has NoData in column TEMP using dropna() -function
selected = selected.dropna(subset=['TEMP'])

#Convert the Fahrenheit temperatures from TEMP into a new column Celsius
selected['Celsius'] = (selected['TEMP'] -32)/1.8

#round celsius column to no decimals
selected['Celsius'] = selected['Celsius'].round(0)

#convert celsius to integers
selected['Celsius'] = selected['Celsius'].astype(int)




###### Problem 3 #######

# Divide the selection into two separate datasets:
# Select all rows from selected DataFrame into variable called kumpula where the USAF code is 29980
# Select all rows from selected DataFrame into variable called rovaniemi where the USAF code is 28450
kumpula = selected.ix[selected['USAF'] == 29980]
rovaniemi = selected.ix[selected['USAF'] == 28450]

print(kumpula.head(), rovaniemi.head())

# Save kumpula DataFrame into Kumpula_temps_May_Aug_2017.csv file (CSV format)
# separate the columns with ,
# use only 2 decimals in the floating point numbers
output_kumpula = "Kumpula_temps_May_Aug_2017.csv"
kumpula.to_csv(output_kumpula, sep=',', index=False, float_format="%.2f")

# Save rovaniemi DataFrame into Rovaniemi_temps_May_Aug_2017.csv file (CSV format)
# separate the columns with ,
# use only 2 decimals in the floating point numbers
output_rovaniemi = "Rovaniemi_temps_May_Aug_2017.csv"
rovaniemi.to_csv(output_rovaniemi, sep=',', index=False, float_format="%.2f")




###### Problem 4 #######
