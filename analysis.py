#The pandas library was imported into the work space for us, as pd(for easy use)
import pandas as pd

#The pandas read_csv command helps to read csv files, 
#There are other commands depending on the file type...
poke = pd.read_csv('pokemon_data.csv')

#This code checks the last 5 rows of the pandas dataframe.
print(poke.tail(5))

