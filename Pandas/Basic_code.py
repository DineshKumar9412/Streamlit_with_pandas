Python Pandas
****************
Python Pandas - DataFrame

import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print df

Name Age
0 Alex 10
1 Bob 12
2 Clarke 13

import pandas as pd
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
                      (Or)
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

df = pd.DataFrame(data)
print(df)

Name Age
0 Tom 20
1 nick 21
2 krish 19
3 jack 18

Add DataFrame
*****************
import pandas as pd

df1 = df = pd.DataFrame({"a":[1, 2, 3, 4],
						"b":[5, 6, 7, 8]})
df2 = pd.DataFrame({"a":[1, 2, 3],
					"b":[5, 6, 7]})
df1.append(df2)
df1.append(df2, ignore_index = True

Python Pandas - Merging/Joining
***********************************

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)

import pandas as pd
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame({
	'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})

Merge Two DataFrames on a Key
print pd.merge(left,right,on='id')

Merge Two DataFrames on Multiple Keys
Print pd.merge(left,right,on=['id','subject_id'])

Pandas Basic Functions

Attribute or Method & Description
T
Transposes rows and columns.
axes
Returns a list with the row axis labels and column axis labels as the only members.
dtypes
Returns the dtypes in this object.
empty
True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
ndim
Number of axes / array dimensions.
shape
Returns a tuple representing the dimensionality of the DataFrame.
size
Number of elements in the NDFrame.
values
Numpy representation of NDFrame.
head()
Returns the first n rows.
tail()
Returns last n rows.


Python Joining
****************
https://www.tutorialspoint.com/python_pandas/python_pandas_merging_joining.htm

Merge Method	SQL Equivalent	Description
left	LEFT OUTER JOIN	Use keys from left object
right	RIGHT OUTER JOIN	Use keys from right object
outer	FULL OUTER JOIN	Use union of keys
inner	INNER JOIN	Use intersection of keys

import pandas as pd
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})

Left Join
print pd.merge(left, right, on='subject_id', how='left')
Right Join
print pd.merge(left, right, on='subject_id', how='right')
Outer join
print pd.merge(left, right, how='outer', on='subject_id')
Inner Join
print pd.merge(left, right, on='subject_id', how='inner')


ADD New Column using lamda
********************************
import pandas as pd
values = [['Rohan', 455], ['Elvish', 250], ['Deepak', 495],
		['Sai', 400], ['Radha', 350], ['Vansh', 450]]

df = pd.DataFrame(values, columns=['Name', 'Univ_Marks'])
df = df.assign(Percentage=lambda x: (x['Univ_Marks'] / 500 * 100))
print(df)

Dataframe Slicing
*******************
import pandas as pd
player_list = [['M.S.Dhoni', 36, 75, 5428000], 
               ['A.B.D Villers', 38, 74, 3428000], 
               ['V.Kholi', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000], 
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]
df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
print(df)
new_df = df[“column_name”]
new_df2 = df[[“column_name”,”column_data2”]]

Pandas loc vs iloc slicing
**************************
* loc selects rows and columns with specific labels
* iloc selects rows and columns at specific integer positions

NOTE: Loc vs iloc main thing we need index column 

df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'points': [5, 7, 7, 9, 12, 9, 9, 4],
                   'assists': [11, 8, 10, 6, 6, 5, 9, 12]},
                   index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])    =================> index we need create incase we don’t have index we can’t slicing

 fin = flt_df.set_index(['last_login_time’])     ===============>we need to change column to index
 wd1_val = fin.loc[str(fdy):str(tdy)]

How to Use loc in Pandas
df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'points': [5, 7, 7, 9, 12, 9, 9, 4],
                   'assists': [11, 8, 10, 6, 6, 5, 9, 12]},
                   index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

#select rows with index labels 'E' and 'F'
df.loc[['E', 'F']]
#select 'E' and 'F' rows and 'team' and 'assists' columns
df.loc[['E', 'F'], ['team', 'assists']]
#select 'E' and 'F' rows and 'team' and 'assists' columns
df.loc['E': , :'assists']

How to Use iloc in Pandas
#select rows in index positions 4 through 6 (not including 6)
df.iloc[4:6]
#select rows in range 4 through 6 and columns in range 0 through 2
df.iloc[4:6, 0:2]
#select rows from 4 through end of rows and columns up to third column
df.iloc[4: , :3]

Pandas Statistics
Function	Description
count()	Number of non-null observations
sum()	Sum of values
mean()	Mean of Values
median()	Median of Values
mode()	Mode of values
std()	Standard Deviation of the Values
min()	Minimum Value
max()	Maximum Value
abs()	Absolute Value
prod()	Product of Values
cumsum()	Cumulative Sum
cumprod()	Cumulative Product
Missing Data
	isnull() 
	notnull()
dropna
df.dropna(inplace = True)
new_df = df.dropna()
fillna
df.fillna(130, inplace = True)
df["Calories"].fillna(130, inplace = True)


https://www.dataquest.io/blog/pandas-cheat-sheet/
https://elitedatascience.com/python-cheat-sheet/

Pandas GroupBY
https://sparkbyexamples.com/pandas/pandas-groupby-count-examples


df.groupby(['col2','col4'])['col1'].sum()
df[['col5','col2']].value_counts().sort_index()

Drop column 

df.drop(to_drop, inplace=True, axis=1)


pandas objects to datetime
https://datagy.io/pandas-extract-date-from-datetime/

df[‘date’] = pd.to_datetime(df[‘date’]).dt.date             ===>  dtype == object
df['u'] = pd.to_datetime(df['u']).dt.normalize()            ===>  dtype ==datetime64[ns]

Single

df['Date']= pd.to_datetime(df['Date'])
                              (Or )
df['Date'] = pd.to_datetime(df['DateTime']).dt.normalize()

Multipul type

df[["col1", "col2", "col3"]] = df[["col1", "col2", "col3"]].apply(pd.to_datetime)

ONLY MONTH 
df['Date'] = pd.to_datetime(df['DateTime']).dt.month
df['MonthNum'] = df['DateTime'].dt.month
df['MonthName'] = df['DateTime'].dt.month_name()
df['MonthNameShort'] = df['DateTime'].dt.month_name().str[:3]
print(df)

ONLY DAY

df['Date'] = pd.to_datetime(df['DateTime']).dt.day

ONLY YEAR

df['Date'] = pd.to_datetime(df['DateTime']).dt.year

pandas strftime

https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html

Pandas Filter
https://towardsdatascience.com/8-ways-to-filter-pandas-dataframes-d34ba585c1b8

Single	

print(df[df["District"] == "Tamil Nadu"])

Multiple single filter

The “&” signs stands for “and” , the “|” stands for “or”

df[(df.val > 0.5) & (df.val2 == 1)]	
df[(df.val < 0.5) | (df.val2 == 7)]

Multiple isin()
frame = df[df[a].isin(dh)]

Logical operators
df[df.val > 0.5]
df[df.name > 'Jane']

Str accessor
df[df.name.str.startswith('J')]
df[df.name.str.contains('y')]

Tilde (~)

The tilde operator is used for “not” logic in filtering
df[~df.name.str.startswith('J')]

Query
df.query('ctg == "B" and val > 0.5')

Nlargest or nsmallest
df.nlargest(3, 'val')
df.nsmallest(2, 'val2')

Loc and iloc
The loc and iloc methods are used to select rows or columns based on index or label.
* 		loc: select rows or columns using labels
* 		iloc: select rows or columns using indices

df.iloc[3:5, :] #rows 3 and 4, all columns
df.loc[3:5, :] #rows 3 and 4, all columns
df.loc['b':'d', :]

Date and time Filters 
**********************
import datetime as DT
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)

filtersf = df[(df['date'] >= str(week_ago)) & (df['date'] <= str(today))]
filtersf.groupby(by=filtersf['date'].dt.date).count()

fgh = pd.DataFrame(filtersf.groupby(['district']).size().reset_index(name='counts'))
filtersf.groupby(['count'])['district'].sum()
df2 = filtersf.groupby(['district'])['count'].sum().reset_index()

df['u'] = pd.to_datetime(df['u']).dt.date                     == object
df['u'] = pd.to_datetime(df['u']).dt.normalize()       == timedelta
filtersf = df[(df['u'] >= '2022-07-01') & (df['u'] <= '2022-07-04')]
print(len(filtersf))


mask = (df['date'] > start_date) & (df['date'] <= end_date)
df = df[(df['Date'] > "2018-01-01") & (df['Date'] <= "2019-07-01")]
df = df[(df['date'] > '2000-6-1') & (df['date'] <= '2000-6-10')]

df[(df['date']>datetime.date(2016,1,1)) & (df['date']<datetime.date(2016,3,1))]  

import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.random((200,3)))
df['date'] = pd.date_range('2000-1-1', periods=200, freq='D')
mask = (df['date'] > '2000-6-1') & (df['date'] <= '2000-6-10')
print(df.loc[mask])

import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.random((200,3)))
df['date'] = pd.date_range('2000-1-1', periods=200, freq='D') 
df = df.set_index(['date'])
print(df.loc['2000-6-1':'2000-6-10'])

import pandas as pd
mydata = pd.read_csv('mydata.csv',index_col='date') # or its index number, e.g. index_col=[0]
mydata['2020-01-01':'2020-02-29'] # will pull all the columns
#if just need one column, e.g. Cost, can be done:
mydata['2020-01-01':'2020-02-29','Cost'] 

import numpy as np   
import pandas as pd
# Make a DataFrame with dates and random numbers
df = pd.DataFrame(np.random.random((30, 3)))
df['date'] = pd.date_range('2017-1-1', periods=30, freq='D')
# Select the rows between two dates
in_range_df = df[df["date"].isin(pd.date_range("2017-01-15", "2017-01-20"))]
print(in_range_df)

Data Cleaning 

data.head()
data.tail()
data.isnull()             =======> True  or False


print(data.head())
print(data.tail())

# Rebuild Missing Data
print(data.isnull().to_string())
print(data.isna())
print(data.isna().sum())
print(data.isna().any().sum())

https://www.geeksforgeeks.org/python-pandas-dataframe-fillna-to-replace-null-values-in-dataframe/

print(df.fillna(0))
print(df["College"].fillna("No College", inplace = True))
nba["College"].fillna( method ='ffill', inplace = True)
nba["College"].fillna( method ='ffill', limit = 1, inplace = True)

Pandas - Working with Text Data

s.str.lower()
s.str.upper()
s.str.len()
s.str.strip()      ==> space remover
s.str.split(' ‘)    ==> William Rick           ==>       [William, Rick]
s.str.cat(sep='_')     ===>  Tom _ William Rick_John_Alber@t
s.str.contains(' ')     ===>    find empty space its gives true or false
s.str.replace('@','$')
s.str.repeat(2)
s.str.count('m')
s.str. startswith ('T')
s..str.endswith('t')
s.str.find('e')            =====> Alber@t ======> 3(position )
s.str.findall('e')       ======> Alber@t  ======> [e] 
s.str.swapcase()
s.str.islower()         ====> True or flase
s.str.isupper()        ====> True or flase
s.str.isnumeric()    ====> True or flase
