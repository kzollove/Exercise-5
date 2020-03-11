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

# In this problem the aim is to understand how different the summer temperatures has been in Helsinki Kumpula and Rovaniemi.
# #Using the data from Problem 3 in kumpula and rovaniemi DataFrames answer to following questions:

# Part 1
# What was the median temperature in:
# Helsinki Kumpula?
# Rovaniemi?
print('Median Temp K:', kumpula[["TEMP"]].median(), '\nMedian Temp R:', rovaniemi[["TEMP"]].median())


# Part 2
# Part 1 considers data from quite long period of time (May-Aug), hence the differences might not be so clear.
# Let's find out what were the mean temperatures in May and June in Kumpula and Rovaniemi:
mayK = kumpula.ix[kumpula['YR--MODAHRMN'] < 201706010000]
junK = kumpula.ix[(kumpula['YR--MODAHRMN'] >= 201706010000) & (kumpula['YR--MODAHRMN'] < 201707010000)]
mayR = rovaniemi.ix[rovaniemi['YR--MODAHRMN'] < 201706010000]
junR = rovaniemi.ix[(rovaniemi['YR--MODAHRMN'] >= 201706010000) & (rovaniemi['YR--MODAHRMN'] < 201707010000)]

print('Mean Temperatures in May and June of Kumpula and Rovaniemi')
print('Kumpula, May: ',mayK['TEMP'].mean())
print('Kumpula, Jun: ',junK['TEMP'].mean())
print('Rovaniemi, May: ',mayR['TEMP'].mean())
print('Rovaniemi, Jun: ',junR['TEMP'].mean())

print('Min Temperatures in May and June of Kumpula and Rovaniemi')
print('Kumpula, May: ',mayK['TEMP'].min())
print('Kumpula, Jun: ',junK['TEMP'].min())
print('Rovaniemi, May: ',mayR['TEMP'].min())
print('Rovaniemi, Jun: ',junR['TEMP'].min())

print('Max Temperatures in May and June of Kumpula and Rovaniemi')
print('Kumpula, May: ',mayK['TEMP'].max())
print('Kumpula, Jun: ',junK['TEMP'].max())
print('Rovaniemi, May: ',mayR['TEMP'].max())
print('Rovaniemi, Jun: ',junR['TEMP'].max())

# Select from rovaniemi and kumpula DataFrames such rows from the DataFrames where YR--MODAHRMN values are from May 2017 (see hints for help) and assign them into variables rovaniemi_may and kumpula_may
# Do similar procedure for June and assign those values into variables rovaniemi_june and kumpula_june
# Using those new subsets print the mean, min and max temperatures for both places in May and June.
# You can add your codes into a data_exploration.py file.

# Upload the script to your GitHub repository for Exercise-5
# Remember to comment well your code! (add docstring, and comments explaining what your code does)
# Interpreting the results after the data analysis is one of the most important steps in a process called knowledge discovery. Hence, use the information above to discuss shortly about following questions (justify your answers with the data analysis results):

# Does there seem to be large difference in temperatures between the months?
# Is Rovaniemi much colder place than Kumpula?