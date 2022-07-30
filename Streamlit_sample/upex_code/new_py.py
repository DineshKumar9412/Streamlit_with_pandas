# import streamlit as st
# import numpy as np
# import pandas as pd
# from datetime import datetime
# from time import gmtime, strftime
# import pytz
# from functools import reduce
# import json
# import codecs
# from st_aggrid import AgGrid
# from st_aggrid.grid_options_builder import GridOptionsBuilder
# from st_aggrid.shared import GridUpdateMode
#
# st.set_page_config(
#     page_title = 'LIMS DASHBOARD',
#     layout="wide",
#     initial_sidebar_state = 'expanded',
#     page_icon = 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Seal_of_Uttar_Pradesh.svg'
# )
#
# c1, c2, c3 = st.columns([8,2,1])
# with c1:
#     st.markdown("""
#         <html>
#             <head>
#             </head>
#             <body>
#                   <h1 style= color:red;line-height:30px;font-family:verdana;font-weight:bold;>&nbsp UPEXCISE DASHBOARD </h1>
#             </body>
#         </html>
#         """, unsafe_allow_html=True)
# with c2:
#     IST = pytz.timezone('Asia/Kolkata')
#     datetime_ist = datetime.now(IST)
#     q = datetime_ist.strftime('%d:%m:%Y / %H:%M:%S')
#     date,time = q[:10], q[11:]
#     st.markdown("""
#     <html>
#         <head>
#         </head>
#         <body>
#            <div>
#               <h3 style=color:red;font-size:32px;font-weight:bold;>Data  &  Time</h3>
#            </div>
#            <div style=color:black;font-size:28px;font-weight:bold;line-height:0.5;>%s %s
#            </div>
#         </body>
#     </html>
#     """%(date, time),unsafe_allow_html=True)
#
# with c3:
#     if st.button("please"):
#         st.write("jfdbdj")
#
# st.markdown("<br><br>", unsafe_allow_html=True)
#
# cl1, cl2, cl3 = st.columns(3)
# with cl1:
#     q = "Total Retail User's"
#     w = 1234
#     st.markdown("""
#             <html>
#             <head>
#             <style>
#             .ones{
#                     background: #11c15b;
#                     border-radius: 14px;
#                     padding: 30px 50px 110px 35px;
#                     width: 350px;
#                     height: 20px;
#                     font-size: 28px;
#                     color:white;
#                     line-height: 0.7;
#                     text-align: center;
#                     font-weight:bold;
#                     transition: transform 1s;
#              }
#             .ones:hover {
#                     transform: scale(1.1); / Animation /
#                     box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#              }
#             .oneplusy{
#             fond-weight:bold;
#             line-height: 3.0;
#             margin-left:10px;
#             font-size: 30px;
#          }
#             </style>
#             </head>
#                 <body>
#                     <div class="ones">%s
#                     <div class= "oneplusy">%i / %i
#                     </div>
#                     </div>
#                 </body>
#             </html>
#             """ % (q, w, 46), unsafe_allow_html=True)
# with cl2:
#     q = "Total Retail User's"
#     w = 234
#     st.markdown("""
#             <html>
#             <head>
#             <style>
#             .oness{
#                     background: #11c15b;
#                     border-radius: 14px;
#                     padding: 30px 50px 110px 35px;
#                     width: 350px;
#                     height: 20px;
#                     font-size: 28px;
#                     color:white;
#                     line-height: .7;
#                     text-align: center;
#                     font-weight:bold;
#                     transition: transform 1s;
#              }
#             .oness:hover {
#                     transform: scale(1.1); / Animation /
#                     box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#              }
#             .oneplusi{
#             fond-weight:bold;
#             line-height: 3.0;
#             margin-left:10px;
#             font-size: 30px;
#          }
#             </style>
#             </head>
#                 <body>
#                     <div class="oness">%s
#                     <div class= "oneplusi">%i / %i
#                     </div>
#                     </div>
#                 </body>
#             </html>
#             """ % (q, w, 45), unsafe_allow_html=True)
# with cl3:
#     q = "Total Retail User's"
#     w = 1324
#     st.markdown("""
#             <html>
#             <head>
#             <style>
#             .onqs{
#                     background: #11c15b;
#                     border-radius: 14px;
#                     padding: 30px 50px 110px 35px;
#                     width: 350px;
#                     height: 20px;
#                     font-size: 28px;
#                     color:white;
#                     line-height: 1;
#                     text-align: center;
#                     font-weight:bold;
#                     transition: transform 1s;
#              }
#             .onqs:hover {
#                     transform: scale(1.1); / Animation /
#                     box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#              }
#             .oneplusa{
#             fond-weight:bold;
#             line-height: 0.2;
#             margin-left:10px;
#             font-size: 30px;
#          }
#             </style>
#             </head>
#                 <body>
#                     <div class="container-fluid onqs">%s
#                            <div class= "container-fluid threeplus">%i / %i
#                     </div>
#                     </div>
#                 </body>
#             </html>
#             """ % (q, w, 67), unsafe_allow_html=True)
#
from datetime import date
import streamlit as st
# dates = st.date_input("Pick a date")
# print(type(dates))


# chan = dict({"Select all":"","Jan": '01',"Feb": '02',"Mar":'03',"Apr":'04',"May":'05',"Jun":'06',"Jul":'07',"Aug":'08',"Sep":'09',"Oct":'10',"Nov":'11',"Dec":'12'})
# month = ["Select all","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sep","Oct","Nov","Dec"]
# days = ["Select all","1", "2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
#
# with coa1:
#     fmo = st.selectbox("From Month", month)
# with coa2:
#     if len(fmo) == 3:
#         fda = st.selectbox("From Day", days)
#     else:
#         days = []
#         fda = st.selectbox("From Day", days)
# with coa3:
#     if len(fmo) == 3 and len(fda) <= 2:
#         tmo = st.selectbox("To Month", month)
#     else:
#         month = []
#         tmo = st.selectbox("To Month", month)
# with coa4:
#     if len(fmo) == 3 and len(fda) <= 2 and len(tmo) == 3:
#         tda = st.selectbox("To Day", days)
#     else:
#         days = []
#         tda = st.selectbox("To Day", days)

# coa1, coa2 = st.columns(2)
# with coa1:
#     fdy = st.date_input("Pick a date")
# with coa2:
#     tdy = st.date_input("Pick a date", key="dshb")

one,two,thr = ["obe","ome"], ["obe","ome","hdjch"],["obe","ome","shucs"]
new = ["Select All"] + one + two + thr
xd = list(dict.fromkeys(new))
xd.sort()
print(xd)
# f = st.selectbox("District:", xd)
#
# print(xd)
#
# data1.drop(data1.columns[[5, 6, 7]], axis=1, inplace=True)
# flt_df = data1.dropna()
# fin = flt_df.set_index(['last_login_time'])
# wwi = fin.loc[fdt:tdt]
# w = len(wwi)