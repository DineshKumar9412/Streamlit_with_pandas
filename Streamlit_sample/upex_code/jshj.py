import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
from time import gmtime, strftime
import pytz
from functools import reduce
import json
import codecs
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

st.set_page_config(
    page_title = 'LIMS DASHBOARD',
    layout="wide",
    initial_sidebar_state = 'expanded'
)

def re_data():
    # mydb = mysql.connector.connect(
    # host="10.2.1.140",port="3306",
    # user="ashoktroondx",
    # password="@#ooKtroonDX22",
    # database="trackandtrace_10_04_2022")
    #
    # if mydb.is_connected():
    #     query2 = "select em.entity_code as ShopID,em.name_of_shop as ShopName,em.district as District, mtp.gatepass_number as gate_pass_number, date(st.created_date)as date,em2.name_of_licensee as wholesaler_name, count(distinct stc.box_bar_code) as No_Of_Cases, sum(sti.received_qty) as No_Of_Bottles from stock_transfer st join mentor_entity_master em on em.entity_code=st.to_entity_code join mentor_entity_master em2 on em2.entity_code=st.from_entity_code join transport_pass tp on st.transport_pass_id=tp.id join mentor_transport_pass mtp on mtp.tp_reference_number=tp.tp_reference_number join stock_transfer_case stc on st.id=stc.stock_transfer_id join stock_transfer_items sti on sti.stock_transfer_id=st.id where transfer_type in ('RETAIL_INWARD') group by em.entity_code,em.name_of_shop,em2.name_of_licensee,em.district,mtp.gatepass_number,date(st.created_date);"
    #     data2 = pd.read_sql_query(query2, mydb)
    # else:
    #     data2 = "no"
    df
    return data2



# c1, c2, c3, c4 = st.columns([1, 16, 4, 1])
# with c1:
#     st.write("dnf")
# with c2:
#     st.markdown("""
#         <html>
#             <head>
#             </head>
#             <body>
#                   <h1 style= color:red;line-height:30px;font-family:verdana;font-weight:bold;>&nbsp UPEXCISE DASHBOARD </h1>
#             </body>
#         </html>
#         """, unsafe_allow_html=True)
# with c3:
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
# with c4:
#     st.button("one")
#     refresh = st.button("two")
# st.markdown("<br><br>", unsafe_allow_html=True)
if refresh :
    data_out = re_data()
@st.cache
def load_data1():
    da = data_out[0]
    da1 = data_out[1]
    da2 = data_out[2]
    return da, da1, da2



# with st.container():
#     one, two, thr  = df["District"].unique().tolist(), df1["District"].unique().tolist(),df2["District"].unique().tolist()
#     # one, two, thr  = data["District"].unique().tolist(), data1["District"].unique().tolist(),data2["District"].unique().tolist()
#
#     new = ["Select All"] + one + two + thr
#     xd = list(dict.fromkeys(new))
#     f = st.selectbox("District:", xd)
#     if f == "Select All":
#         selected_option_2 = df["District"].unique()
#         r1 = df[df["District"].isin(selected_option_2)]
#     else:
#         r1 = df[df["District"] == f]

# coa1, coa2, coa3, coa4 = st.columns(4)
# chan = dict({"Jan": '01',"Feb": '02',"Mar":'03',"Apr":'04',"May":'05',"Jun":'06',"Jul":'07',"Aug":'08',"Sep":'09',"Oct":'10',"Nov":'11',"Dec":'12'})
# month = ["Select all","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sep","Oct","Nov","Dec"]
# days = ["Select all","1", "2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
# with coa1:
#     fmo = st.selectbox("From Month", month)
# with coa2:
#     fda = st.selectbox("From Day",days)
# with coa3:
#     tmo = st.selectbox("To Month", month)
# with coa4:
#     tda = st.selectbox("To Day", days)
# if fmo == "Select all":
#     print("stesting")
# else:
#     fmth = chan.get(fmo)
#     tmth = chan.get(tmo)
#     fdt = "2022" + "-"+ fmth +"-"+ fda
#     tdt = "2022" + "-"+ tmth +"-"+ tda
#
# st.markdown("<br>", unsafe_allow_html=True)
#
# cl1, cl2, cl3, cl4 = st.columns(4)
# with cl1:
#     q = "Total Users logged in Today"
#     w = df[df["last_login_time"] == ""]
#     # w = sf["Total Cases Sold (Nos) "].sum()
#     w = 23
#     v = 1025
#     st.markdown("""
#             <html>
#             <head>
#             <style>
#             .one{
#                     background: #4680ff;
#                     border-radius: 14px;
#                     padding: 25px 20px 65px 25px;
#                     width: 300px;
#                     height: 20px;
#                     font-size: 18px;
#                     color:white;
#                     line-height: 0.1;
#                     text-align: center;
#                     font-weight:bold;
#                     transition: transform 1s;
#                 }
#             .one:hover {
#                     transform: scale(1.1); / Animation /
#                     box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#                 }
#             .oneplus{
#             fond-weight:bold;
#             line-height: 2.3;
#             margin-left:18px;
#             font-size: 30px;
#             }
#             </style>
#             </head>
#                 <body>
#                     <div class="one">%s
#                        <div class= "oneplus">%i / %i
#                        </div>
#                     </div>
#                 </body>
#             </html>
#             """ % (q, w,v), unsafe_allow_html=True)
# with cl2:
#     q = "Total Users transaction today"
#     # w = sf["Total Bottles Sold (Nos) "].sum()
#     w = 1234
#     st.markdown("""
#             <html>
#             <head>
#             <style>
#             .ones{
#                     background: #11c15b;
#                     border-radius: 14px;
#                     padding: 25px 20px 65px 25px;
#                     width: 300px;
#                     height: 20px;
#                     font-size: 18px;
#                     color:white;
#                     line-height: 0.1;
#                     text-align: center;
#                     font-weight:bold;
#                     transition: transform 1s;
#                 }
#             .ones:hover {
#                     transform: scale(1.1); / Animation /
#                     box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#                 }
#             .oneplusy{
#             fond-weight:bold;
#             line-height: 2.3;
#             margin-left:10px;
#             font-size: 30px;
#             }
#             </style>
#             </head>
#                 <body>
#                     <div class="ones">%s
#                        <div class= "oneplusy">%i
#                        </div>
#                     </div>
#                 </body>
#             </html>
#             """ % (q, w), unsafe_allow_html=True)
# with cl3:
#     q = "Total Stock in today"
#     # w = sf["Total Stock In - Cases "].sum()
#     w = 6536
#     st.markdown("""
#             <html>
#             <head>
#             <style>
#             .oneq{
#                     background: #ffa21d;
#                     border-radius: 14px;
#                     padding: 25px 20px 65px 25px;
#                     width: 300px;
#                     height: 20px;
#                     font-size: 18px;
#                     color:white;
#                     line-height: 0.1;
#                     text-align: center;
#                     font-weight:bold;
#                     transition: transform 1s;
#                 }
#             .oneq:hover {
#                     transform: scale(1.1); / Animation /
#                     box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#                 }
#             .oneplusq{
#             fond-weight:bold;
#             line-height: 2.3;
#             margin-left:10px;
#             font-size: 30px;
#             }
#             </style>
#             </head>
#                 <body>
#                     <div class="oneq">%s
#                        <div class= "oneplusq">%i
#                        </div>
#                     </div>
#                 </body>
#             </html>
#             """ % (q, w), unsafe_allow_html=True)
# with cl4:
#     q = "Total Sales for today"
#     # w = sf["Total Stock In - Bottles "].sum()
#     w = 3565
#     st.markdown("""
#             <html>
#             <head>
#             <style>
#             .onew{
#                     background: #6644da;
#                     border-radius: 14px;
#                     padding: 25px 20px 65px 25px;
#                     width: 300px;
#                     height: 20px;
#                     font-size: 18px;
#                     color:white;
#                     line-height: 0.1;
#                     text-align: center;
#                     font-weight:bold;
#                     transition: transform 1s;
#                 }
#             .onew:hover {
#                     transform: scale(1.1); / Animation /
#                     box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
#                 }
#             .oneplusw{
#             fond-weight:bold;
#             line-height: 2.3;
#             margin-left:10px;
#             font-size: 30px;
#             }
#             </style>
#             </head>
#                 <body>
#                     <div class="onew">%s
#                        <div class= "oneplusw">%i
#                        </div>
#                     </div>
#                 </body>
#             </html>
#             """ % (q, w), unsafe_allow_html=True)
#
# st.markdown("<br><br>", unsafe_allow_html=True)
#
# coll1, coll2 = st.columns([15,2])
# with coll1:
#     dfg = st.selectbox("Please select the report", ["Active Users","Stock In","Sales"])
# with coll2:
#     if dfg == "Active Users":
#         fin = r1
#     elif dfg == "Stock In":
#         fin = df1[df1["District"] == f]
#     else:
#         fin = df2[df2["District"] == f]
#     csv = fin.to_csv().encode('utf-8')
#     st.markdown("")
#     st.download_button(
#         label="Download data as CSV",
#         data=csv,
#         file_name='large_df.csv',
#         mime='text/csv',
#     )
# st.markdown("<br><br>", unsafe_allow_html=True)
#
# if dfg == "Active Users":
#     fin  = r1
# elif dfg == "Stock In":
#     if f == "Select All":
#         fin = df1
#     else:
#         fin = df1[df1["District"] == f]
# else:
#     if f == "Select All":
#         fin = df2
#     else:
#         fin = df2[df2["District"] == f]
#
# place = st.empty()
# with place.container():
#     gb = GridOptionsBuilder.from_dataframe(fin)
#     gb.configure_pagination()
#
#     gridOptions = gb.build()
#     data = AgGrid(fin,
#                   gridOptions=gridOptions,
#                   enable_enterprise_modules=True,
#                   allow_unsafe_jscode=True,
#                   height=1440,fit_columns_on_grid_load=True)