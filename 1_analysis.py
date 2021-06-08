import pandas as pd

#load csv in as a data frame###############################################################################
df = pd.read_csv('pokemon_data.csv')
print(df.head(3))
print(df.tail(5))


# #load excel in as a data frame
# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print("EXCEL________________________________________________________________________")
# print(df_xlsx.head(3))


# #load in a tab seperated file as data frame
# df_tab = pd.read_csv('pokemon_data.txt', delimiter='\t')
# print("TAB SEPERATED________________________________________________________________")
# print(df_tab.head(5))

##########################################################################################################
#read the headers
print(df.columns)

#read a specific column
print(df['Name'][0:5])

#read mulitple columns
#read a specific column
print(df[['Name', 'HP', 'Type 1']][5:10])

#read a specific row(s)
print(df.iloc[1:3])

#read a specific location (R,C)
#second row, first column
print(df.iloc[2,1])

####Iteration VERY USEFUL########################################################################################
#iterate through each row
for index, row in df.iterrows():
    print (index, row['Name'])

######df.loc----userful for text type searching (as opposed to index, row integers)############################
print(df.loc[df['Type 1'] == "Fire"])

############sorting#####################################################################################
#pass in the column you want to sort by
print(df.sort_values('Name'))

#sort in reverse order,
print(df.sort_values('Name', ascending=False))

#sort by main and secondary coolumn
#we can choose the first as ascedning and the second as descending
print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))



