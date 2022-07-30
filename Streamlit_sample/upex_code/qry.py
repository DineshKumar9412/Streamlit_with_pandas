import pandas as pd
from datetime import datetime
from datetime import date, timedelta
import streamlit as st
import datetime as dt

tdy = date.today()
ytd = tdy - timedelta(days = 1)
ytd1 = tdy - timedelta(days = 2)
data1 = pd.read_csv("report1.csv")
# print(data1.dtypes)
# print(data1.head().to_string())
print(data1.columns)
data1["last_login_time"] = pd.to_datetime(data1["last_login_time"])
data1["last_tp_ack_date"] = pd.to_datetime(data1["last_tp_ack_date"])
data1["last_ob_date"] = pd.to_datetime(data1["last_ob_date"])
data1["last_sold_date"] = pd.to_datetime(data1["last_sold_date"])
# print(data1.dtypes)
males = data1[(data1[Gender]=='Male') & (data1[Year]==2014)]

# # print(data1.head().to_string())
#
# df = data1.set_index(['last_login_time'])
# print(df.loc['2022-04-24':'2022-04-26'])




# tdx = "2022-04-25"
# tdx1 = "2022-04-26"
# print(data1[data1["last_login_time"] == "2022-04-25"])
# print(data1[data1['last_login_time'].dt.strftime('%Y-%m-%d')])

# sd  = (data1[data1['last_login_time'].dt.date.astype(str) > tdx])
# print(sd)
# print(data1[data1['last_login_time'].astype(str).str[:10] == tdx].head().to_string())

# coa1, coa2, coa3, coa4 = st.columns(4)
# chan = dict({"Select all":"","Jan": '01',"Feb": '02',"Mar":'03',"Apr":'04',"May":'05',"Jun":'06',"Jul":'07',"Aug":'08',"Sep":'09',"Oct":'10',"Nov":'11',"Dec":'12'})
# month = ["Select all","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sep","Oct","Nov","Dec"]
# days = ["Select all","1", "2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
# with coa1:
#     fmo = st.selectbox("From Month", month)
# with coa2:
#     if len(fmo) == 3:
#         fda = st.selectbox("From Day",days)
#     else:
#         days =[]
#         fda = st.selectbox("From Day",days)
# with coa3:
#     if len(fmo) == 3 and len(fda) <= 2:
#         tmo = st.selectbox("To Month", month)
#     else:
#         month =[]
#         tmo = st.selectbox("To Month", month)
# with coa4:
#     if len(fmo) == 3 and len(fda) <= 2 and len(tmo) == 3:
#         tda = st.selectbox("To Day",days)
#     else:
#         days =[]
#         tda = st.selectbox("To Day",days)
# if len(fmo) == 3 and len(fda) <= 2 and len(tmo) == 3 and len(tda) <= 2:
#     fmth = chan.get(fmo)
#     tmth = chan.get(tmo)
#     fdt = "2022" + "-" + fmth + "-" + fda
#     tdt = "2022" + "-" + tmth + "-" + tda
#     fdy = date(*map(int, fdt.split('-')))
#     tdy = date(*map(int, tdt.split('-')))
#     data1.drop(data1.columns[[5, 6, 7]], axis=1, inplace=True)
#     flt_df = data1.dropna()
#     flt_df["last_login_time"] = pd.to_datetime(flt_df["last_login_time"]).dt.date
#     wwi = flt_df[(flt_df['last_login_time'] <= tdy) & (flt_df['last_login_time'] >= fdy)]
#     w = len(wwi)
# else:
#     data1.drop(data1.columns[[5, 6, 7]], axis=1, inplace=True)
#     flt_df = data1.dropna()
#     w = len(flt_df)
#
#
# print(w)
#     tda = st.selectbox("To Day", days)
#
# if len(fmo) == 3 and len(fda) <= 2 and len(tmo) == 3 and len(tda) <= 2:
#     print("yes")
#     fmth = chan.get(fmo)
#     tmth = chan.get(tmo)
#     # print(fmth)
#     fdt = "2022" + "-" + fmth + "-" + fda
#     tdt = "2022" + "-" + tmth + "-" + tda
#     if fmth != "" and tmth != "" and fda != "" and tda != "":
#         fdy = date(*map(int, fdt.split('-')))
#         tdy = date(*map(int, tdt.split('-')))
#         print(fdy, tdy)
# else:
#     print("All fields should be select all")

# if tda == "Select all":
#     data1.drop(data1.columns[[5, 6, 7]], axis=1, inplace=True)
#     flt_df = data1.dropna()
#     w = len(flt_df)
#     print(flt_df.head().to_string())
#     print(w)
#     # w = data1[(data1['last_login_time'] != "NaT")]
# else:
#     data1.drop(data1.columns[[5, 6, 7]], axis=1, inplace=True)
#     flt_df = data1.dropna()
#     flt_df['last_login_time'] == flt_df['last_login_time'].str.slice(0,9)
#     flt_df["last_login_time"] = pd.to_datetime(flt_df["last_login_time"]).dt.date
#     w = flt_df[(flt_df['last_login_time'] <= tdy) & (flt_df['last_login_time'] >= fdy)]
#
# val = w.count()
# #     # print(w.head().to_string())
# print("Total users login today",val[0])

# # wdt = pd.read_csv("report2.csv")
# # wdt1 = pd.read_csv("report3.csv")
# uni = data1.count()
# print(uni[0])
# df.drop(df.columns[[5,6,7]],axis = 1, inplace=True)
# flt_df = df.dropna()
# # flt_df['last_login_time_sli'] == flt_df['last_login_time'].str.slice(0,9)
# flt_df["last_login_time"] = pd.to_datetime(flt_df["last_login_time"]).dt.date
#
# w = flt_df[(flt_df['last_login_time'] == tdy) | (flt_df['last_login_time'] == ytd)]
# val = w.count()
# # print(w.head().to_string())
# print("Total users login today",val[0])
#
# # widget 3 Total stock in today
# print(wdt.dtypes)
# wdt["date"] = pd.to_datetime(wdt["date"]).dt.date
# wdt = wdt[(wdt['date'] == tdy) | (wdt['date'] == ytd)]
# wd2_val = wdt['gate_pass_number'].count()
# print("Total Stock in Today",wd2_val)
#
# widget 4 Total sales for today
# wdt1["date(created_date)"] = pd.to_datetime(wdt1["date(created_date)"],format="%Y/%m/%d")
# # wdt1 = wdt1[(wdt1['date(created_date)'] == str(tdy)) | (wdt1['date(created_date)'] == str(ytd))]
# wdt1 = wdt1[(wdt1['date(created_date)'] == str(ytd)) ]
# wd3_val = wdt1['item_scanned'].sum()
# print(wdt1.head().to_string())
# print("Total Sales in Today",round(wd3_val))

# #widget 2 Total user transactions

# print(data1.dtypes)
# data1["last_login_time"] = pd.to_datetime(data1["last_login_time"]).dt.date
# print(data1.dtypes)
# data1["last_tp_ack_date"] = pd.to_datetime(data1["last_tp_ack_date"]).dt.date
# data1["last_ob_date"] = pd.to_datetime(data1["last_ob_date"]).dt.date
# data1["last_sold_date"] = pd.to_datetime(data1["last_sold_date"]).dt.date
#
# wdt2 = data1[(data1['last_login_time'] == tdy) | (data1['last_login_time'] == ytd) | (data1['last_tp_ack_date'] == tdy) | (data1['last_tp_ack_date'] == ytd) | (data1['last_ob_date'] == tdy) | (data1['last_ob_date'] == ytd) | (data1['last_sold_date'] == tdy) | (data1['last_sold_date'] == ytd) ]
# wdt2_val = len(wdt2)
# print(wdt2_val)

