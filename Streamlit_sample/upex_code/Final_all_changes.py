import mysql.connector
from mysql.connector import Error
import pandas as pd
import streamlit as st
from time import time
from datetime import datetime, date, timedelta
from time import gmtime, strftime
import pytz
import datetime as dt
from functools import reduce
import json
import codecs
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import streamlit_authenticator as stauth
from PIL import Image
st.set_page_config(
    page_title = 'UPEXCISE DASHBOARD',
    layout="wide",
    initial_sidebar_state = 'expanded',
    page_icon = 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Seal_of_Uttar_Pradesh.svg'
)
# names = ['upexcise','upexcise1','upexcise2']
# usernames = ['upexcise_usr1','upexcise_usr2','upexcise_usr3']
# passwords = ['up@usr1$123','up$usr2@22','up%usr3#19']
# hashed_passwords = stauth.Hasher(passwords).generate()
# authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
#     'some_cookie_name','some_signature_key',cookie_expiry_days=30)
# name, authentication_status, username = authenticator.login('Login','main')
# if authentication_status:
#     data1 = pd.read_csv("r1.csv")
#     data2 = pd.read_csv("report2.csv")
#     data3 = pd.read_csv("q3.csv")
#     datan = data1.copy()
#     c1, c2, c3, c4 = st.columns([1, 16, 4, 1])
#     with c1:
#         st.markdown(""" """, unsafe_allow_html=True)
#         image = Image.open('Seal.png')
#         st.image(image)
#     with c2:
#         st.markdown("""
#                 <html>
#                     <head>
#                     </head>
#                     <body>
#                           <h1 style= color:#6554c0;line-height:30px;font-family:verdana;font-weight:bold;>&nbsp UPEXCISE DASHBOARD </h1>
#                     </body>
#                 </html>
#                 """, unsafe_allow_html=True)
#     with c3:
#         IST = pytz.timezone('Asia/Kolkata')
#         datetime_ist = datetime.now(IST)
#         q = datetime_ist.strftime('%d:%m:%Y / %H:%M:%S')
#         date, time = q[:10], q[11:]
#         st.markdown("""
#             <html>
#                 <head>
#                 </head>
#                 <body>
#                 <div>
#                       <h3 style=color:#6554c0;font-size:25px;font-weight:bold;>Date  &  Time</h3>
#                 </div>
#                  <div style=color:#6554c0;font-size:20px;font-weight:bold;line-height:0.8;>%s %s
#                  </div>
#                 </body>
#             </html>
#             """ % (date, time), unsafe_allow_html=True)
#     with c4:
#         authenticator.logout('Logout', 'main')
#     with st.container():
#         one, two, thr = data1["District"].unique().tolist(), data2["District"].unique().tolist(), data3[
#             "District"].unique().tolist()
#         new = one + two + thr
#         xd = list(dict.fromkeys(new))
#         xd.sort()
#         xdr = ["Select All"] + xd
#         f = st.selectbox("District:", xdr)
#         coa1, coa2 = st.columns(2)
#         with coa1:
#             fdy = st.date_input("Pick a date")
#         with coa2:
#             tdy = st.date_input("Pick a date", key="dshb")
#         if f == "Select All":
#             # weight 1
#             data1.drop(data1.columns[[5, 6, 7]], axis=1, inplace=True)
#             flt_df = data1.dropna()
#             print(flt_df.dtypes)
#             flt_df['last_login_time'] = pd.to_datetime(flt_df['last_login_time'])
#             fin = flt_df.set_index(['last_login_time'])
#             wd1_val = fin.loc[str(fdy):str(tdy)]
#             w1_val = len(wd1_val)
#             # weight 2
#             print(data2.dtypes)
#             data2["date"] = pd.to_datetime(data2["date"])
#             ww3 = data2.set_index(['date'])
#             wwd3 = ww3.loc[str(fdy):str(tdy)]
#             w2_val = len(pd.unique(wwd3["gate_pass_number"]))
#             # weight 3
#             print(data3.dtypes)
#             data3["created_date"] = pd.to_datetime(data3["created_date"])
#             wwd4 = data3.set_index(['created_date'])
#             wwi4 = wwd4.loc[str(fdy):str(tdy)]
#             wd4_val = wwi4['item_scanned'].sum()
#             w3_val = round(wd4_val)
#         else:
#             # weight 1
#             r1 = data1[data1["District"] == f]
#             r1.drop(r1.columns[[5, 6, 7]], axis=1, inplace=True)
#             flt_df = r1.dropna()
#             flt_df['last_login_time'] = pd.to_datetime(flt_df['last_login_time'])
#             fin = flt_df.set_index(['last_login_time'])
#             wd1_val = fin.loc[str(fdy):str(tdy)]
#             w1_val = len(wd1_val)
#             # weight 2
#             r2 = data2[data2["District"] == f]
#             r2["date"] = pd.to_datetime(r2["date"])
#             ww3 = r2.set_index(['date'])
#             wwd3 = ww3.loc[str(fdy):str(tdy)]
#             w2_val = len(pd.unique(wwd3["gate_pass_number"]))
#             # weight 3
#             r3 = data3[data3["District"] == f]
#             r3["created_date"] = pd.to_datetime(r3["created_date"])
#             wwd4 = r3.set_index(['created_date'])
#             wwi4 = wwd4.loc[str(fdy):str(tdy)]
#             wd4_val = wwi4['item_scanned'].sum()
#             w3_val = round(wd4_val)
#         # # weight 2
#         # if f == "Select All":
#         #     data2["date"] = pd.to_datetime(data2["date"])
#         #     ww3 = data2.set_index(['date'])
#         #     wwd3 = ww3.loc[str(fdy):str(tdy)]
#         #     wd3_val = len(pd.unique(wwd3["gate_pass_number"]))
#         # else:
#         #     r2 = data2[data2["District"] == f]
#         #     r2["date"] = pd.to_datetime(r2["date"])
#         #     ww3 = r2.set_index(['date'])
#         #     wwd3 = ww3.loc[str(fdy):str(tdy)]
#         #     wd3_val = len(pd.unique(wwd3["gate_pass_number"]))
#         # # weight 3
#         # if f == "Select All":
#         #     data3["created_date"] = pd.to_datetime(data3["created_date"])
#         #     wwd4 = data3.set_index(['created_date'])
#         #     wwi4 = wwd4.loc[str(fdy):str(tdy)]
#         #     wd4_val = wwi4['item_scanned'].sum()
#         # else:
#         #     r3 = data3[data3["District"] == f]
#         #     r3["created_date"] = pd.to_datetime(r3["created_date"])
#         #     wwd4 = r3.set_index(['created_date'])
#         #     wwi4 = wwd4.loc[str(fdy):str(tdy)]
#         #     wd4_val = wwi4['item_scanned'].sum()
#         # print(round(wd4_val))
#     st.markdown("<br>", unsafe_allow_html=True)
#     cl1, cl2, cl3 = st.columns(3)
#     with cl1:
#         q = "Total Retail Users logged"
#         st.markdown("""
#                  <html>
#                     <head>
#                  <style>
#                     .one{
#                             background: #4680ff;
#                             border-radius: 14px;
#                             padding: 30px 50px 110px 35px;
#                             width: 350px;
#                             height: 20px;
#                             font-size: 20px;
#                             color:white;
#                             line-height: 1;
#                             text-align: center;
#                             font-weight:bold;
#                             transition: transform 1s;
#                      }
#                     .one:hover {
#                             transform: scale(1.1); / Animation /
#                             box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#                         }
#                     .oneplus{
#                     fond-weight:bold;
#                     line-height: 2.5;
#                     margin-left:18px;
#                     font-size: 30px;
#                     }
#                     </style>
#                     </head>
#                         <body>
#                             <div class= "one">%s
#                             <div class= "oneplus">%i / %i
#                             </div>
#                             </div>
#                         </body>
#                     </html>
#                     """ % (q, w1_val, len(data1)), unsafe_allow_html=True)
#     with cl2:
#         q = "Total Retail Stock-In"
#         st.markdown("""
#                 <html>
#                 <head>
#                 <style>
#                 .oneq{
#                         background: #11c15b;;
#                         border-radius: 14px;
#                         padding: 30px 50px 110px 35px;
#                         width: 350px;
#                         height: 20px;
#                         font-size: 28px;
#                         color:white;
#                         line-height: 1;
#                         text-align: center;
#                         font-weight:bold;
#                         transition: transform 1s;
#                     }
#                 .oneq:hover {
#                         transform: scale(1.1); / Animation /
#                         box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#                  }
#                 .oneplusq{
#                 fond-weight:bold;
#                 line-height: 2.5;
#                 margin-left:10px;
#                 font-size: 30px;
#                 }
#                 </style>
#                 </head>
#                  <body>
#                       <div class="oneq">%s
#                            <div class= "oneplusq">%i
#                         </div>
#                         </div>
#                 </body>
#                 </html>
#                 """ % (q, w2_val), unsafe_allow_html=True)
#     with cl3:
#         q = "Total Retail Sales"
#         st.markdown("""
#                 <html>
#                 <head>
#                 <style>
#                 .onew{
#                         background: #6644da;
#                         border-radius: 14px;
#                         padding: 30px 50px 110px 35px;
#                         width: 350px;
#                         height: 20px;
#                         font-size: 28px;
#                         color:white;
#                         line-height: 1;
#                         text-align: center;
#                         font-weight:bold;
#                         transition: transform 1s;
#                  }
#                 .onew:hover {
#                         transform: scale(1.1); / Animation /
#                         box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#                     }
#                 .oneplusw{
#                 fond-weight:bold;
#                 line-height: 2.5;
#                 margin-left:10px;
#                 font-size: 30px;
#                 }
#                 </style>
#                 </head>
#                     <body>
#                         <div class="onew">%s
#                         <div class= "oneplusw">%i
#                         </div>
#                         </div>
#                     </body>
#                 </html>
#                 """ % (q, w3_val), unsafe_allow_html=True)
#     st.markdown("<br>", unsafe_allow_html=True)
#     coll1, coll2 = st.columns([15, 2])
#     with coll1:
#         dfg = st.selectbox("Please select the report", ["Retail Active Users", "Retail Stock In", "Retail Sales"])
#     with coll2:
#         if dfg == "Retail Active Users":
#             if f == "Select All":
#                 datan['last_login_time'] = pd.to_datetime(datan['last_login_time'])
#                 rau = datan.set_index(['last_login_time'])
#                 tab = rau.loc[str(fdy):str(tdy)]
#                 tab.reset_index(inplace=True)
#                 lld = tab.pop('last_login_time')
#                 tab.insert(4, 'last_login_time', lld)
#                 tab["last_login_time"] = pd.to_datetime(tab["last_login_time"]).dt.date
#                 tab1 = tab
#             else:
#                 ra1 = datan[datan["District"] == f]
#                 ra1['last_login_time'] = pd.to_datetime(ra1['last_login_time'])
#                 rau = ra1.set_index(['last_login_time'])
#                 tab = rau.loc[str(fdy):str(tdy)]
#                 tab.reset_index(inplace=True)
#                 lld = tab.pop('last_login_time')
#                 tab.insert(4, 'last_login_time', lld)
#                 tab["last_login_time"] = pd.to_datetime(tab["last_login_time"]).dt.date
#                 tab1 = tab
#         elif dfg == "Retail Stock In":
#             if f == "Select All":
#                 data2["date"] = pd.to_datetime(data2["date"])
#                 rsi = data2.set_index(['date'])
#                 rsi1 = rsi.loc[str(fdy):str(tdy)]
#                 rsi1.reset_index(inplace=True)
#                 rld = rsi1.pop('date')
#                 rsi1.insert(4, 'date', rld)
#                 rsi1["date"] = pd.to_datetime(rsi1["date"]).dt.date
#                 tab1 = rsi1
#             else:
#                 ra2 = data2[data2["District"] == f]
#                 ra2["date"] = pd.to_datetime(ra2["date"])
#                 rsi = ra2.set_index(['date'])
#                 rsi1 = rsi.loc[str(fdy):str(tdy)]
#                 rsi1.reset_index(inplace=True)
#                 rld = rsi1.pop('date')
#                 rsi1.insert(4, 'date', rld)
#                 rsi1["date"] = pd.to_datetime(rsi1["date"]).dt.date
#                 tab1 = rsi1
#         else:
#             if f == "Select All":
#                 data3["created_date"] = pd.to_datetime(data3["created_date"])
#                 rst = data3.set_index(['created_date'])
#                 rst1 = rst.loc[str(fdy):str(tdy)]
#                 rst1.reset_index(inplace=True)
#                 rlt = rst1.pop('created_date')
#                 rst1.insert(3, 'created_date', rlt)
#                 rst1["created_date"] = pd.to_datetime(rst1["created_date"]).dt.date
#                 tab1 = rst1
#             else:
#                 ra3 = data3[data3["District"] == f]
#                 ra3["created_date"] = pd.to_datetime(ra3["created_date"])
#                 rst = ra3.set_index(['created_date'])
#                 rst1 = rst.loc[str(fdy):str(tdy)]
#                 rst1.reset_index(inplace=True)
#                 rlt = rst1.pop('created_date')
#                 rst1.insert(3, 'created_date', rlt)
#                 rst1["created_date"] = pd.to_datetime(rst1["created_date"]).dt.date
#                 tab1 = rst1
#         csv = tab1.to_csv().encode('utf-8')
#         st.markdown("")
#         st.download_button(
#             label="Download data as CSV",
#             data=csv,
#             file_name='large_df.csv',
#             mime='text/csv',
#         )
#     st.markdown("<br>", unsafe_allow_html=True)
#     place = st.empty()
#     with place.container():
#         gb = GridOptionsBuilder.from_dataframe(tab1)
#         gb.configure_pagination()
#         gridOptions = gb.build()
#         data = AgGrid(tab1,
#                       gridOptions=gridOptions,
#                       enable_enterprise_modules=True,
#                       allow_unsafe_jscode=True,
#                       height=1440, fit_columns_on_grid_load=True)
#     st.markdown(
#         """
#            <style>
#            .main {
#            background-color: #FFFFFF;
#            }
#            </style>
#            """,
#         unsafe_allow_html=True
#     )
# elif authentication_status == False:
#     st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')

# data4 = pd.read_csv("q4.csv")
# s = st.selectbox("hsdg", data4["District"].unique())
# df = data4[data4["District"] == "azamgarh"]
# print(df)
# a = data4["District"].unique()
# # one, two, thr = data1["District"].unique().tolist(), data2["District"].unique().tolist(), data3["District"].unique().tolist()
# # new = one + two + thr
# xd = list(dict.fromkeys(a))
# xd.sort()
# xdr = ["Select All"] + xd
# f = st.selectbox("District:", xdr)

# coa1, coa2 = st.columns(2)
# with coa1:
#     fdy = st.date_input("Pick a date")
# with coa2:
#     tdy = st.date_input("Pick a date", key="dshb")
# if f == "Select All":
#     data4['DATE'] = pd.to_datetime(data4['DATE'])
#     fin = data4.set_index(['DATE'])
#     wd4 = fin.loc[str(fdy):str(tdy)]
#     wd4_val = ["OB_INWARD"].sum()
# else:
#     data4['DATE'] = pd.to_datetime(data4['DATE'])
#     r4 = data4[data4["District"] == f]
#     fin = r4.set_index(['DATE'])
#     wd4 = fin.loc[str(fdy):str(tdy)]
#     wd4_val = wd4["OB_INWARD"].sum()
# col5, col6,col8, col9= st.columns(4)
#
# with col5:
#     q = "Total Retail Users logged"
#     st.markdown("""
#              <html>
#                 <head>
#              <style>
#                 .one{
#                         background: #4680ff;
#                         border-radius: 14px;
#                         padding: 30px 50px 110px 35px;
#                         width: 350px;
#                         height: 20px;
#                         font-size: 20px;
#                         color:white;
#                         line-height: 1;
#                         text-align: center;
#                         font-weight:bold;
#                         transition: transform 1s;
#                  }
#                 .one:hover {
#                         transform: scale(1.1); / Animation /
#                         box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#                     }
#                 .oneplus{
#                 fond-weight:bold;
#                 line-height: 2.5;
#                 margin-left:18px;
#                 font-size: 30px;
#                 }
#                 </style>
#                 <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#                 </head>
#                     <body>
#                         <div class= "container-fluid one">%s
#                         <div class= "container-fluid oneplus">%i
#                         </div>
#                         </div>
#                     </body>
#                 </html>
#                 """ % (q, wd4_val, ), unsafe_allow_html=True)
#
# with col8:
#     st.markdown("""
#     """,unsafe_allow_html=True)
#
# with col6:
#     q = "Total Retail Users logged"
#     st.markdown("""
#              <html>
#                 <head>
#              <style>
#                 .oness{
#                         background: #4680ff;
#                         border-radius: 14px;
#                         padding: 30px 50px 110px 35px;
#                         width: 100px;
#                         height: 20px;
#                         font-size: 20px;
#                         color:white;
#                         line-height: 1;
#                         text-align: center;
#                         font-weight:bold;
#                  }
#                 .oneplusss{
#                 fond-weight:bold;
#                 line-height: 2.5;
#                 margin-left:18px;
#                 font-size: 30px;
#                 }
#                 </style>
#                 <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#                 </head>
#                     <body>
#                         <div class= "container-fluid oness">%s
#                         <div class= "container-fluid oneplusss">%i
#                         </div>
#                         </div>
#                     </body>
#                 </html>
#                 """ % (q, wd4_val ), unsafe_allow_html=True)
# cl1, cl2, cl3, cl4 = st.columns(4)
# with cl1:
#     q = "Total Retail Users logged"
#     st.markdown("""
#                <html>
#                   <head>
#                <style>
#                   .one{
#                           background: #4680ff;
#                           border-radius: 14px;
#                           padding: 30px 50px 110px 35px;
#                           width: 350px;
#                           height: 20px;
#                           font-size: 20px;
#                           color:white;
#                           line-height: 1;
#                           text-align: center;
#                           font-weight:bold;
#                    }
#                   .oneplus{
#                   fond-weight:bold;
#                   line-height: 2.5;
#                   margin-left:18px;
#                   font-size: 30px;
#                   }
#                   </style>
#                   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#                   </head>
#                       <body>
#                           <div class= "container-fluid one">%s
#                           <div class= "container-fluid oneplus">%i / %i
#                           </div>
#                           </div>
#                       </body>
#                   </html>
#                   """ % (q, 43435, 98989), unsafe_allow_html=True)
#
# with cl2:
#     q = "Stock in through TP"
#     st.markdown("""
#               <html>
#               <head>
#               <style>
#               .oneq{
#                       background: #11c15b;;
#                       border-radius: 14px;
#                       padding: 30px 50px 110px 35px;
#                       width: 350px;
#                       height: 20px;
#                       font-size: 20px;
#                       color:white;
#                       line-height: 1;
#                       text-align: center;
#                       font-weight:bold;
#                   }
#               .oneplusq{
#               fond-weight:bold;
#               line-height: 2.5;
#               margin-left:10px;
#               font-size: 30px;
#               }
#               </style>
#               <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#               </head>
#                <body>
#                     <div class="container-fluid oneq">%s
#                          <div class= "container-fluid oneplusq">%i
#                       </div>
#                       </div>
#               </body>
#               </html>
#               """ % (q, 32344), unsafe_allow_html=True)
# with cl3:
#     q = "Stock in through opening balance"
#     st.markdown("""
#               <html>
#               <head>
#               <style>
#               .oaneq{
#                       background: #FF5370;
#                       border-radius: 14px;
#                       padding: 30px 50px 110px 35px;
#                       width: 350px;
#                       height: 20px;
#                       font-size: 20px;
#                       color:white;
#                       line-height: 0.8;
#                       text-align: center;
#                       font-weight:bold;
#                }
#               .oaneplusq{
#               fond-weight:bold;
#               line-height: 2.9;
#               margin-left:10px;
#               font-size: 30px;
#               }
#               </style>
#               <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#               </head>
#                   <body>
#                       <div class="container-fluid oaneq">%s
#                       <div class= "container-fluid oaneplusq">%i
#                       </div>
#                       </div>
#                   </body>
#               </html>
#               """ % (q, 34355), unsafe_allow_html=True)
#
# with cl4:
#     q = "Total Retail Sales"
#     st.markdown("""
#               <html>
#               <head>
#               <style>
#               .onew{
#                       background: #6644da;
#                       border-radius: 14px;
#                       padding: 30px 50px 110px 35px;
#                       width: 350px;
#                       height: 20px;
#                       font-size: 20px;
#                       color:white;
#                       line-height: 1;
#                       text-align: center;
#                       font-weight:bold;
#                }
#               .oneplusw{
#               fond-weight:bold;
#               line-height: 2.9;
#               margin-left:10px;
#               font-size: 30px;
#               }
#               </style>
#               <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#               </head>
#                   <body>
#                       <div class="container-fluid onew">%s
#                       <div class= "container-fluid oneplusw">%i
#                       </div>
#                       </div>
#                   </body>
#               </html>
#               """ % (q, 23422), unsafe_allow_html=True)
#
# with col8:
#     st.markdown("""
#     """,unsafe_allow_html=True)
#     st.markdown("<br>", unsafe_allow_html=True)