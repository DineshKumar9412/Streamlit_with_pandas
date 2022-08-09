Different between cursor-fetchall-and-pandas-dataframe
*******************************************************

https://stackoverflow.com/questions/71072838/difference-between-cursor-fetchall-and-pandas-dataframe
  
import mysql.connector
import pandas as pd
from time import time

mydb = mysql.connector.connect(
  host="localhost",port="3306",
  user="root",
  password="root@123",
  database="face"
)
mycursor = mydb.cursor()
if mydb.is_connected():
    start_time = time()
    # query = "SELECT * FROM test;"
    # query = "select * from test where id='1717';"
    mycursor.execute("select * from test where id='1717';")
    df = pd.DataFrame(mycursor.fetchall())                               =============>> Method 1               best
    # df = pd.read_sql(query, mydb)                                      ============>>> Method 2
    mydb.close()
    end_time = time()
    seconds_elapsed = end_time - start_time
    hours, rest = divmod(seconds_elapsed, 3600)
    minutes, seconds = divmod(rest, 60)
    print(minutes, seconds)
else:
    print("no")
    

How to mycursor.close and mydb.close  how to reconnect
*******************************************************

import mysql.connector
import pandas as pd
from time import time

mydb = mysql.connector.connect(
  host="localhost",port="3306",
  user="root",
  password="root@123",
  database="face"
)
mycursor = mydb.cursor()
if mydb.is_connected():
    # query = "SELECT * FROM test;"
    # df = pd.read_sql(query, mydb)
    mycursor.execute("SELECT * FROM test;")
    df = pd.DataFrame(mycursor.fetchall())
    jsonfiles = json.loads(df.to_json(orient='records'))
    mycursor.close()
    mydb.close()
    return jsonify(jsonfiles)
else:
    return jsonify({'data': "no"})

mydb.connect()                                                          =========>>> reconnected   mydb
if mydb.is_connected():
    mycursor = mydb.cursor()                                            =========>>> reconnected  mycursor
    # query = f"select * from test where id='{num}';"
    # df = pd.read_sql(query, mydb)
    mycursor.execute(f"select * from test where id='{num}';")
    df = pd.DataFrame(mycursor.fetchall())
    jsonfiles = json.loads(df.to_json(orient='records'))
    mycursor.close()
    return jsonify(jsonfiles)
else:
    return jsonify({'data': "no"})
