# import mysql.connector
# import pandas as pd
# import streamlit as st
# from time import time
#
# mydb = mysql.connector.connect(
#   host="103.249.97.108",port="3306",
#   user="ashoktroondx",
#   password="@#ooKtroonDX22",
#   database="pds_17sep16"
# )
#
# mycursor = mydb.cursor()
#
# query1 = "SELECT * FROM district;"
# query2 = "SELECT * FROM district;"
# query3 = "SELECT * FROM district;"
#
# df = pd.read_sql_query(query, mydb)
# df1 = pd.read_sql_query(query, mydb)
# df2 = pd.read_sql_query(query, mydb)
#
#
# end_time = time()
# seconds_elapsed = end_time - start_time
# hoursd, rests = divmod(seconds_elapsed, 3600)
# minutess, secondss = divmod(rests, 60)
# print(secondss)

import mysql.connector
import pandas as pd
import streamlit as st
from time import time
from streamlit_autorefresh import st_autorefresh

mydb = mysql.connector.connect(
  host="103.249.97.108",port="3306",
  user="ashoktroondx",
  password="@#ooKtroonDX22",
  database="pds_17sep16"
)

mycursor = mydb.cursor()

query1 = "SELECT * FROM district;"
# query2 = "SELECT * FROM district;"
# query3 = "SELECT * FROM district;"
# df = pd.read_sql_query(query1, mydb)
# df.to_csv('dist.csv')
#

# update every 15 mins
st_autorefresh(interval= 5 * 60 * 1000, key="dataframerefresh")
def get_data():
    # Perform some request to get a dataframe
    df = pd.read_sql_query(query1, mydb)
    df.to_csv('dishss.csv')
    # df1 = pd.read_sql_query(query2, mydb)
    # df1.to_csv('/location/file2')
    # df2 = pd.read_sql_query(query3, mydb)
    # df2.to_csv('/location/file3')
    return df
st.dataframe(get_data())