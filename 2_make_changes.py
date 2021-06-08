import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#IN THESE EXAMPLES WE WILL ESSENTIALLY REARRANGE DATA. WE ARE GOING  TO USE A LOT OF INDEXING
#BE CAREFUL---IF YOUR DATA IS CHANGING HARDCODING INDEXING IS BAD-----USE THE NAMES INSTEAD LIKE IN THE FIRST EXAMPLE


#create a new column that totals all the stats
#this way is easiest to read-----and SAFEST
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))

#drop the column we made:
df = df.drop(columns=['Total'])
print(df.head(5))

# add a column in a more succinct way using iloc (integer location)
# : means all rows
# then we add up the 4th through 9th column
# axis=1 sums horizontally, axis=0 sums vertically
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(5))


# lets rearrange a column to move total over to the left of HP
#first get the columns as a list
#Then concantenate them---note the single column is considered a string so you need to make it a list by using the [cols[-1]]
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5))


#########################LETS SAVE OUR DATA################################
#by setting index=False, we remove the left most index column
df.to_csv('modified_pokemon.csv', index=False)

#to save as excel
df.to_excel('modified_poke.xlsx', index=False)

#to save as a tab seperated file
df.to_csv('modified_poke2.txt', index=False, sep='\t')