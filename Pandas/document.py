Python Cheat Sheet for Data Science 
https://elitedatascience.com/python-cheat-sheet

https://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf

Scikit-Learn Cheat Sheet: Python Machine Learning 
https://www.datacamp.com/community/blog/scikit-learn-cheat-sheet

Top 28 Cheat Sheets for Machine Learning, Data Science and Big Data
https://www.analyticsvidhya.com/blog/2017/02/top-28-cheat-sheets-for-machine-learning-data-science-probability-sql-big-data/

Pandas Cheat Sheet — Python for Data Science 
https://www.dataquest.io/blog/pandas-cheat-sheet/

Pandas 101 - Python and R Tips 
https://cmdlinetips.com/pandas-tutorial/

Mean Function in Python pandas (Dataframe, Row and column wise mean) - DataScience Made Simple 
https://www.datasciencemadesimple.com/mean-function-python-pandas-dataframe-row-column-wise-mean/

Pandas Fliters
https://towardsdatascience.com/8-ways-to-filter-pandas-dataframes-d34ba585c1b8

pandas: filter rows of DataFrame with operator chaining 
https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining

How to filter data without using pandas package
https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining

Python : 10 Ways to Filter Pandas DataFrame 
https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html

Python Pandas : Select Rows in DataFrame by conditions on multiple columns 
https://thispointer.com/python-pandas-select-rows-in-dataframe-by-conditions-on-multiple-columns

Read csv file


import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("train.csv")
print(df.head().to_string())
 

Get value


df1 = df[df['City'] == "Henderson"]
print(df1.head().to_string())
 

Contains mean “like” in mysql


df1 = df[df['Position'].str.contains("PG”)]
Ex:  You have Chennai  …. Give .str.contains(“che”) its show chennai
 

Show Multiple Column


df = dfs[["gid", "District Name", "Interface SAA"]]
print(dh.head().to_string())
 

Search Multiple list in single column


frame = df[df[a].isin(dh)]

Example:
fr = df[df["State"].isin(["fgft","hggf"])]
 

Dictionary  to filter in pandas


dict = {}
for a,g in enumerate(range(ss)):
    gh = st.sidebar.selectbox("Filter {} value".format(a), df.columns, key=a)
    gg = st.multiselect('Which one you want to choose?', df[gh].unique(), key=a)
    dict.update({gh : gg})
# print(dict.keys())
cols = list(dict.keys())
res = df[df[cols].isin(dict).all(1)]


fg = df1.loc[df1[filter_v.keys()].isin(filter_v.values()).all(axis=1), :]
fg = df1.loc[(df1[list(filter_v)] == pd.Series(filter_v)).all(axis=1)]
DATE AND Month

Extract month and year to a new column in Pandas | Data Interview Questions 
https://www.interviewqs.com/ddi-code-snippets/extract-month-year-pandas

DuckDB - Efficient SQL on Pandas with DuckDB 
https://duckdb.org/2021/05/14/sql-on-pandas.html 

Pandas Pivot table | Create Pivot Table Using Pandas in Python 
https://www.analyticsvidhya.com/blog/2020/03/pivot-table-pandas-python/

Data Preprocessing 

df = pd.read_csv("train.csv")

print(df.describe())

print(df.dtypes)

print(df.info())           ###good

prrint(df.select_dtypes(include = np.object)

covert to object / int32 to datatime formet in pandas
https://www.marsja.se/pandas-convert-column-to-datetime/

Pandas Convert Column to datetime - object/string, integer, CSV & Excel
https://www.marsja.se/pandas-convert-column-to-datetime/

Convert the column type from string to datetime format in Pandas dataframe - GeeksforGeeks 
https://www.geeksforgeeks.org/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe/


How to get First Value in your dataframe


df = pd.read_csv("train.csv")
df['year'] = pd.DatetimeIndex(df['Ship Date']).year
dff = df[df["year"] == 2017]
fin = dff.groupby(["Product Name", "City"])['Sales'].sum().sort_values(ascending=False).reset_index()
# fin.iloc[0].tolist()
#fin.iloc[0]
print(fin.iloc[0].tolist()[2])
 

What Is Pandas in Python? Everything You Need to Know 
https://www.activestate.com/resources/quick-reads/what-is-pandas-in-python-everything-you-need-to-know/#:~:text=Pandas%20is%20an%20open%20source,support%20for%20multi%2Ddimensional%20arrays.

Change datatype (object to datetime)
https://pythonexamples.org/pandas-dataframe-add-append-row/

df["Order_test_date"] = pd.to_datetime(df["Order_test_date"])

#How to get last five days data
print(df[df["Order_test_date"] >= (pd.to_datetime('8/5/21') - pd.Timedelta(days=4))])
 

How to Add or Insert Row to Pandas DataFrame? - Python Examples 
https://pythonexamples.org/pandas-dataframe-add-append-row/

Date and time filter

How to Filter DataFrame by Date in Pandas 
https://datascientyst.com/filter-by-date-pandas-dataframe/

Date and time


import pandas as pd

df = pd.read_csv("file.csv")
df['Date'] = pd.DatetimeIndex(df['Date'])
df['month'] = pd.DatetimeIndex(df['Date']).month
df['month'] = df['Date'].dt.strftime('%b')
#df['month'] = df['Date'].dt.strftime('%B')
fu = df[df["month"] == "Jan"]
print(fu)


Date and time filter

How to Filter DataFrame by Date in Pandas
https://datascientyst.com/filter-by-date-pandas-dataframe/


import pandas as pd

df = pd.read_csv("file.csv")
df['Date'] = pd.DatetimeIndex(df['Date'])
df['month'] = pd.DatetimeIndex(df['Date']).month
df['year'] = pd.DatetimeIndex(df['Date']).year
df['day'] = pd.DatetimeIndex(df['Date']).day

df['month'] = df['Date'].dt.strftime('%b')
#df['month'] = df['Date'].dt.strftime('%B')
fu = df[df["month"] == "Jan"]
print(fu)
Date and time filter Methods


import pandas as pd
import streamlit as st

df = pd.read_csv("Supermarket.csv")
df["Date"] = pd.DatetimeIndex(df["Date"])

## https://datascientyst.com/filter-by-date-pandas-dataframe/
#####  Method 1  #####
#set as index column
df = df.set_index('Date')
sf = df.loc['2019-01-05':'2019-01-15']
#We need to set index first
sf.reset_index(inplace=True)
#cut the date columns
sfm = sf.pop('Date')
#past the column
sf.insert(10, 'Date', sfm)
# if you need to show only date use this
sf["Date"] = sf["Date"].dt.date
print(sf.head().to_string())

#### Method 2 ########
filtersf = df[(df['Date'] >= '2019-01-01') & (df['Date'] <= '2019-01-15')]
sf["Date"] = sf["Date"].dt.date
print(sf.head().to_string())

# filter by single day
df_filtered = df[df['date'].dt.strftime('%Y-%m-%d') == '2014-01-01']

# filter by single month
df_filtered = df[df['date'].dt.strftime('%Y-%m') == '2014-01']

# filter by single year
df_filtered = df[df['date'].dt.strftime('%Y') == '2014']
Last 7 Day 


import datetime as DT
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)
Day wise count 


filtersf = df[(df['date'] >= str(week_ago)) & (df['date'] <= str(today))]
filtersf.groupby(by=filtersf['date'].dt.date).count()

fgh = pd.DataFrame(filtersf.groupby(['district']).size().reset_index(name='counts'))
filtersf.groupby(['count'])['district'].sum()
df2 = filtersf.groupby(['district'])['count'].sum().reset_index()

df['u'] = pd.to_datetime(df['u']).dt.date 
df['u'] = pd.to_datetime(df['u']).dt.normalize()
filtersf = df[(df['u'] >= '2022-07-01') & (df['u'] <= '2022-07-04')]
print(len(filtersf))