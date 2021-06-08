import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')

#filter where a column equals a value
print(df.loc[df['Type 1'] == 'Grass'])

#multiple text location conditions
# & sign for both x and y conditions
# | sign for x and/or y conditions
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

#can also set parameters with values and not just locations
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])


#can also create new data frames and save them#################################################################
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

# WHEN YOU FILTER DATA IT KEEPS THE OLD INDEX NUMBERS---but you can reset them---
# by default it saves the old index as a new column but you can get rid of the old indicies with drop=True
print(new_df)
new_df = new_df.reset_index(drop=True)
print(new_df)
#new_df.to_csv('filtered.csv')


# RegEx Filtering###############################################################################
# Example1: Filter out all names that contain mega
contains_df = df.loc[df['Name'].str.contains('Mega')]
print(contains_df)

# Example2: Filter out all names that DO NOT contain mega
contains_df2 = df.loc[~df['Name'].str.contains('Mega')]
print(contains_df2)

# Example3: Filter out if type 1 is grass or fire using regEx
# regex=True means to use regular expressions
# flags=re.I means to ignore case
# 'fire|grass means fire or grass

regex_df = df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
print(regex_df)

#Example 4: All pokemon names that start with Pi
#'^pi[a-z]*' 
# ######## ^ means the start of the word
# ####### [a-z] means it contains letters a-z
# ####### * means any number of letters (i.e. the name may be 3 or 100 characters long)
regex_df2 = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(regex_df2)


#####################################CONDITIONAL CHANGES#################################################
#Example 1: Under type 1----change the fire type to flamer
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(df)
#change it back
df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'
print(df)

#Example 2: Change all fire pokemon to legendary----use one codnition to change another columns value
df.loc[df['Type 1']== 'Fire', 'Legendary'] = True
print(df.loc[df['Type 1'] == "Fire"])


####reload dataframe to get rid of making all the legendary true
df = pd.read_csv('modified_pokemon.csv')
print(df)

#Example 3: Change two columns based on a condition by using lists
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = [88, 'Yeah']
print(df)