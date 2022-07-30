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
import plotly.express as px


st.set_page_config(
    page_title = 'UPEXCISE DASHBOARD',
    layout="wide",
    initial_sidebar_state = 'expanded',
    page_icon = 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Seal_of_Uttar_Pradesh.svg'
)

names = ['upexcise3','upexcise4']
usernames = ['upexcise_usr3','upexcise_usr4']
passwords = ['up%usr3#19','up%usr4#20']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login','main')

if authentication_status:
    def mysql_all():
        mydb = mysql.connector.connect(
                host="10.2.2.111",port="3306",
        user="misuser",
        password="MiSUsER@2022",
        database="trackandtrace_10_04_2022")
        mycursor = mydb.cursor()


        query6 = "select em.district_name,cast(fbd.bill_time as date) as date,count(fbd.id) as total_transactions from flat_bill_details fbd join entity_master em on em.entity_code=fbd.entity_code where em.entity_type_code='RETAIL_SHOP' group by em.district_name,cast(fbd.bill_time as date)"

        if mydb.is_connected():
            query1 = "select em.district as District, em.entity_code as shopId, u.username as user_name, em.name_of_shop as shop_name, max(lh.login_time) as last_login_time, max(stx.created_date) as last_tp_ack_date, max(st.created_date) as last_ob_date, max(fbd.created_date) as last_sold_date from mentor_entity_master em join user_managment_service_10_04_2022.user u on u.username =em.entity_code left join user_managment_service_10_04_2022.login_history lh on lh.user_id =u.id left join stock_transfer st on st.to_entity_code =em.entity_code and st.transfer_type ='RETAIL_INWARD'left join stock_transfer stx on stx.to_entity_code =em.entity_code and stx.transfer_type ='OB_INWARD'left join flat_bill_details fbd on fbd.entity_code =em.entity_code group by em.entity_code, u.username, em.name_of_shop;"
            query3 = "select em.entity_code as ShopID,em.name_of_shop as ShopName,em.district as District, date(created_date) as created_date, sum(fbid.qty) as item_scanned from flat_bill_item_details fbid join mentor_entity_master em on em.entity_code=fbid.entity_code group by em.entity_code, em.name_of_shop, em.district, date(created_date);"
            query2 = "select em.entity_code as ShopID,em.name_of_shop as ShopName,em.district as District, mtp.gatepass_number as gate_pass_number, date(st.created_date)as date,em2.name_of_licensee as wholesaler_name, count(distinct stc.box_bar_code) as No_Of_Cases, sum(sti.received_qty) as No_Of_Bottles from stock_transfer st join mentor_entity_master em on em.entity_code=st.to_entity_code join mentor_entity_master em2 on em2.entity_code=st.from_entity_code join transport_pass tp on st.transport_pass_id=tp.id join mentor_transport_pass mtp on mtp.tp_reference_number=tp.tp_reference_number join stock_transfer_case stc on st.id=stc.stock_transfer_id join stock_transfer_items sti on sti.stock_transfer_id=st.id where transfer_type in ('RETAIL_INWARD') group by em.entity_code,em.name_of_shop,em2.name_of_licensee,em.district,mtp.gatepass_number,date(st.created_date);"
            query4 = "SELECT em.district AS District,DATE(sti.created_date) AS DATE,COUNT(*) AS 'OB_INWARD'FROM `trackandtrace_10_04_2022`.stock_transfer st JOIN `trackandtrace_10_04_2022`.stock_transfer_items sti ON sti.`stock_transfer_id`=st.id JOIN `trackandtrace_10_04_2022`.mentor_entity_master em ON em.`entity_code` =st.to_entity_code WHERE st.`transfer_type`='OB_INWARD'GROUP BY District,DATE(sti.created_date);"


            data1 = pd.read_sql_query(query1, mydb)
            data2 = pd.read_sql_query(query2, mydb)
            data3 = pd.read_sql_query(query3, mydb)
            data4 = pd.read_sql_query(query4, mydb)
            mydb.close()
            return data1, data2, data3, data4
    def mysql_limt(dis, st_da, en_da):
        mydb = mysql.connector.connect(
        host="10.2.2.111",port="3306",
        user="misuser",
        password="MiSUsER@2022",
        database="trackandtrace_10_04_2022")
        mycursor = mydb.cursor()
        if mydb.is_connected():
            query1 = f"select em.district as District, em.entity_code as shopId, u.username as user_name, em.name_of_shop as shop_name, max(lh.login_time) as last_login_time, max(stx.created_date) as last_tp_ack_date, max(st.created_date) as last_ob_date, max(fbd.created_date) as last_sold_date from mentor_entity_master em join user_managment_service_10_04_2022.user u on u.username =em.entity_code left join user_managment_service_10_04_2022.login_history lh on lh.user_id =u.id left join stock_transfer st on st.to_entity_code =em.entity_code and st.transfer_type ='RETAIL_INWARD'left join stock_transfer stx on stx.to_entity_code =em.entity_code and stx.transfer_type ='OB_INWARD'left join flat_bill_details fbd on fbd.entity_code =em.entity_code where em.district = '{dis}' and lh.login_time BETWEEN '{st_da} 00:00:00' and '{en_da} 23:59:59' group by em.entity_code, u.username, em.name_of_shop;"
            query2 = f"select em.entity_code as ShopID,em.name_of_shop as ShopName,em.district as District, mtp.gatepass_number as gate_pass_number, date(st.created_date)as date,em2.name_of_licensee as wholesaler_name, count(distinct stc.box_bar_code) as No_Of_Cases, sum(sti.received_qty) as No_Of_Bottles from stock_transfer st join mentor_entity_master em on em.entity_code=st.to_entity_code join mentor_entity_master em2 on em2.entity_code=st.from_entity_code join transport_pass tp on st.transport_pass_id=tp.id join mentor_transport_pass mtp on mtp.tp_reference_number=tp.tp_reference_number join stock_transfer_case stc on st.id=stc.stock_transfer_id join stock_transfer_items sti on sti.stock_transfer_id=st.id where transfer_type in ('RETAIL_INWARD') and em.district = '{dis}' and st.created_date BETWEEN '{st_da} 00:00:00' and '{en_da} 23:59:59' group by em.entity_code,em.name_of_shop,em2.name_of_licensee,em.district,mtp.gatepass_number,date(st.created_date);"
            query3 = f"select em.entity_code as ShopID,em.name_of_shop as ShopName,em.district as District, date(created_date) as created_date, sum(fbid.qty) as item_scanned from flat_bill_item_details fbid join mentor_entity_master em on em.entity_code=fbid.entity_code where em.district = '{dis}' and created_date BETWEEN '{st_da} 00:00:00' and '{en_da} 23:59:59' group by em.entity_code, em.name_of_shop, em.district, date(created_date);"
            query4 = f"SELECT em.district AS District,DATE(sti.created_date) AS DATE,COUNT(*) AS 'OB_INWARD'FROM `trackandtrace_10_04_2022`.stock_transfer st JOIN `trackandtrace_10_04_2022`.stock_transfer_items sti ON sti.`stock_transfer_id`=st.id JOIN `trackandtrace_10_04_2022`.mentor_entity_master em ON em.`entity_code` =st.to_entity_code WHERE st.`transfer_type`='OB_INWARD' and em.district = '{dis}' and sti.created_date BETWEEN '{st_da} 00:00:00' and '{en_da} 23:59:59' GROUP BY District,DATE(sti.created_date);"


            data1 = pd.read_sql_query(query1, mydb)
            data2 = pd.read_sql_query(query2, mydb)
            data3 = pd.read_sql_query(query3, mydb)
            data4 = pd.read_sql_query(query4, mydb)
            mydb.close()
            return data1, data2, data3, data4
    c1, c2, c3, c4 = st.columns([1, 16, 4, 1])
    with c1:
        st.markdown(""" """, unsafe_allow_html=True)
        image = Image.open('/home/troondxadmin/SUTfromlink.png')
        st.image(image)
    with c2:
        st.markdown("""
                <html>
                    <head>
                    </head>
                    <body>
                          <h1 style= color:#6554c0;line-height:30px;font-family:verdana;font-weight:bold;>&nbsp UPEXCISE DASHBOARD </h1>
                    </body>
                </html>
                """, unsafe_allow_html=True)
    with c3:
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.now(IST)
        q = datetime_ist.strftime('%d:%m:%Y / %H:%M:%S')
        date, time = q[:10], q[11:]
        st.markdown("""
            <html>
                <head>
                </head>
                <body>
                <div>
                      <h3 style=color:#6554c0;font-size:25px;font-weight:bold;>Date  &  Time</h3>
                </div>
                 <div style=color:#6554c0;font-size:20px;font-weight:bold;line-height:0.8;>%s %s
                 </div>
                </body>
            </html>
            """ % (date, time), unsafe_allow_html=True)
    with c4:
        st.markdown("""<br>""", unsafe_allow_html=True)
        authenticator.logout('Logout', 'main')
        st.markdown("<br>", unsafe_allow_html=True)

    with st.container():
        mydb1 = mysql.connector.connect(
                host="10.2.2.111",port="3306",
        user="misuser",
        password="MiSUsER@2022",
        database="trackandtrace_10_04_2022")
        query5 = "SELECT distinct cast(lh.created_date as date) as sdate,uau.district_desc,count(distinct lh.user_id) as total_users_logged from user_managment_service_10_04_2022.login_history lh join user_managment_service_10_04_2022.user_allocated_unit uau on lh.user_id=uau.user_id join user_managment_service_10_04_2022.user u on u.id=lh.user_id where u.user_type_code like '%RETAIL%' group by cast(lh.created_date as date),uau.district_desc"
        data5 = pd.read_sql_query(query5, mydb1)

        data5.columns = ['date','district','count']
        data5['date'] = pd.to_datetime(data5['date']).dt.date
        data5['date'] = pd.to_datetime(data5['date']).dt.normalize()

        today = dt.date.today()
        wk = today - dt.timedelta(days=6)
        week_ago = today - dt.timedelta(days=7)
        filtersf = data5[(data5['date'] > str(week_ago)) & (data5['date'] <= str(today))]
        filtersf.groupby(by=filtersf['date'].dt.date).count()
        #filtersf = data5[(data5['date'] >= '2022-04-01') & (data5['date'] <= '2022-07-13')]
        #df2 = filtersf.groupby(['district'])['count'].sum().reset_index()
        asd = st.selectbox("filter", filtersf["district"].unique())
        wwe = filtersf[filtersf["district"] == asd]

        cola1, cola2 = st.columns(2)
    with cola1:
        fig =px.bar(wwe,x = "date",y = "count",text_auto = True,color_discrete_sequence=px.colors.diverging.Earth,color=None)
        fig.update_layout(height=500,yaxis_title = "Total Users logged")
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
            #fig.update_layout(width=900, height=400)
        st.plotly_chart(fig)
    with cola2:
        query6 = f"select em.district_name,cast(fbd.bill_time as date) as date,count(fbd.id) as total_transactions from flat_bill_details fbd join entity_master em on em.entity_code=fbd.entity_code where em.district_name='{asd}' and em.entity_type_code='RETAIL_SHOP' and bill_time BETWEEN '{wk} 00:00:00' and '{today} 23:59:59'  group by em.district_name,cast(fbd.bill_time as date)"

        data6 = pd.read_sql_query(query6,mydb1)
        mydb1.close()
        figg =px.bar(data6,x = "date",y = "total_transactions",text_auto = True,color=None,color_discrete_sequence=px.colors.diverging.Tropic,labels=None)
        figg.update_layout(height=500,yaxis_title = "Total transactions count")
        figg.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(figg)

    cola1, cola2= st.columns([18,2])

    with cola1:
        dists = st.selectbox("District", ['Agra', 'Aligarh', 'AmbedkarNagar', 'Amethi', 'Amroha', 'Auraiya', 'Ayodhya', 'Azamgarh', 'Bagpat', 'Behraich', 'Ballia', 'Balrampur', 'Banda', 'Barabanki', 'Bareilly', 'Basti', 'Bijnor', 'Badaun', 'Bulandshahar', 'Chandauli', 'Chitrakoot', 'Deoria', 'Etah', 'Etawah', 'Farrukhabad', 'Fatehpur', 'Firozabad', 'Gbnagar', 'Ghaziabad', 'Ghazipur', 'Gonda', 'Gorakhpur', 'Hamirpur', 'Hapur', 'Hardoi', 'Hathras', 'Jalaun', 'Jaunpur', 'Jhansi', 'Kannauj', 'KanpurDehat', 'KanpurNagar', 'Kasganj', 'Kaushambhi', 'Kheri', 'Kushinagar', 'Lalitpur', 'Lucknow', 'Mahoba', 'Maharajganj', 'Mainpuri', 'Mathura', 'Mau', 'Meerut', 'Mirzapur', 'Moradabad', 'Muzaffarnagar', 'Pilibhit', 'Pratapgarh', 'Pryagraj', 'Raebareli', 'Rampur', 'Saharanpur', 'Sambhal', 'Sknagar', 'SRNagar', 'Shahjahanpur', 'Shamali', 'Shravasti', 'Sidharthnagar', 'Sitapur', 'Sonbhadra', 'Sultanpur', 'Unnao', 'varanasi'])
    with cola2:
        st.markdown("<br>", unsafe_allow_html=True)
        select = st.radio("Select all Districts", ["No","Yes"])
        #sd = st.radio("", ['None', 'Ascending', 'Descending'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;border-radius: 15px 15px; height: 10px; width: 200000px;}</style>',unsafe_allow_html=True)
    coa1, coa2 = st.columns(2)
    with coa1:
        fdy = st.date_input("Pick a date")
    with coa2:
        tdy = st.date_input("Pick a date", key="dshb")
    if select == "Yes":
        data1,data2,data3,data4 = mysql_all()[0],mysql_all()[1],mysql_all()[2],mysql_all()[3]
        # weight 1
        data1.drop(data1.columns[[5, 6, 7]], axis=1, inplace=True)
        flt_df = data1.dropna()
        fin = flt_df.set_index(['last_login_time'])
        wd1_val = fin.loc[str(fdy):str(tdy)]
        w1_val = len(wd1_val)
        w1_sva = len(data1)
        # weight 2
        data2["date"] = pd.to_datetime(data2["date"])
        ww3 = data2.set_index(['date'])
        wwd3 = ww3.loc[str(fdy):str(tdy)]
        w2_val = len(pd.unique(wwd3["gate_pass_number"]))
        # weight 3
        data3["created_date"] = pd.to_datetime(data3["created_date"])
        wwd4 = data3.set_index(['created_date'])
        wwi4 = wwd4.loc[str(fdy):str(tdy)]
        wd4_val = wwi4['item_scanned'].sum()
        w3_val = round(wd4_val)
        # weight 4
        data4['DATE'] = pd.to_datetime(data4['DATE'])
        ww4 = data4.set_index(['DATE'])
        wd4 = ww4.loc[str(fdy):str(tdy)]
        wd4_v = wd4["OB_INWARD"].sum()
        w4_val = round(wd4_v)
    else:
        data_limit1,data_limit2,data_limit3, data_limit4 = mysql_limt(dists,fdy,tdy)[0],mysql_limt(dists,fdy,tdy)[1],mysql_limt(dists,fdy,tdy)[2],mysql_limt(dists,fdy,tdy)[3]
        # weight 1
        #r1 = data_limit1[data_limit1["District"] == f]
        r1 = data_limit1
        r1.drop(r1.columns[[5, 6, 7]], axis=1, inplace=True)
        flt_df = r1.dropna()
        fin = flt_df.set_index(['last_login_time'])
        wd1_val = fin.loc[str(fdy):str(tdy)]
        w1_val = len(wd1_val)
        w1_sva = len(r1)
        # weight 2
        # r2 = data_limit2[data_limit2["District"] == f]
        r2 = data_limit2
        r2["date"] = pd.to_datetime(r2["date"])
        ww3 = r2.set_index(['date'])
        wwd3 = ww3.loc[str(fdy):str(tdy)]
        w2_val = len(pd.unique(wwd3["gate_pass_number"]))
        # weight 3
        r3 = data_limit3
        #r3 = data_limit3[data_limit3["District"] == f]
        r3["created_date"] = pd.to_datetime(r3["created_date"])
        wwd4 = r3.set_index(['created_date'])
        wwi4 = wwd4.loc[str(fdy):str(tdy)]
        wd4_val = wwi4['item_scanned'].sum()
        w3_val = round(wd4_val)
        # weight 4
        r4 = data_limit4
        #r4 = data_limit4[data_limit4["District"] == f]
        r4['DATE'] = pd.to_datetime(r4['DATE'])
        ww4 = r4.set_index(['DATE'])
        wd4 = ww4.loc[str(fdy):str(tdy)]
        wd4_v = wd4["OB_INWARD"].sum()
        w4_val = round(wd4_v)
    st.markdown("<br>", unsafe_allow_html=True)
    cl1, cl2, cl3, cl4 = st.columns(4)
    with cl1:
        q = "Total Retail Users logged"
        st.markdown("""
                 <html>
                    <head>
                 <style>
                    .one{
                            background: #4680ff;
                            border-radius: 14px;
                            padding: 30px 50px 110px 35px;
                            width: 350px;
                            height: 20px;
                            font-size: 20px;
                            color:white;
                            line-height: 1;
                            text-align: center;
                            font-weight:bold;
                     }
                    .oneplus{
                    fond-weight:bold;
                    line-height: 2.5;
                    margin-left:18px;
                    font-size: 30px;
                    }
                    </style>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                    </head>
                        <body>
                            <div class= "container-fluid one">%s
                            <div class= "container-fluid oneplus">%i / %i
                            </div>
                            </div>
                        </body>
                    </html>
                    """ % (q, w1_val, w1_sva), unsafe_allow_html=True)
    with cl2:
        q = "Stock in through TP"
        st.markdown("""
                <html>
                <head>
                <style>
                .oneq{
                        background: #11c15b;;
                        border-radius: 14px;
                        padding: 30px 50px 110px 35px;
                        width: 350px;
                        height: 20px;
                        font-size: 20px;
                        color:white;
                        line-height: 1;
                        text-align: center;
                        font-weight:bold;
                    }
                .oneplusq{
                fond-weight:bold;
                line-height: 2.7;
                margin-left:10px;
                font-size: 30px;
                }
                </style>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                </head>
                 <body>
                      <div class="container-fluid oneq">%s
                           <div class= "container-fluid oneplusq">%i
                        </div>
                        </div>
                </body>
                </html>
                """ % (q, w2_val), unsafe_allow_html=True)
    with cl3:
        q = "Stock in through opening balance"
        st.markdown("""
                <html>
                <head>
                <style>
                .oaneq{
                        background: #FF5370;
                        border-radius: 14px;
                        padding: 30px 50px 110px 35px;
                        width: 350px;
                        height: 20px;
                        font-size: 20px;
                        color:white;
                        line-height: 0.8;
                        text-align: center;
                        font-weight:bold;
                 }
                .oaneplusq{
                fond-weight:bold;
                line-height: 2.9;
                margin-left:10px;
                font-size: 30px;
                }
                </style>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                </head>
                    <body>
                        <div class="container-fluid oaneq">%s
                        <div class= "container-fluid oaneplusq">%i
                        </div>
                        </div>
                    </body>
                </html>
                """ % (q, w4_val), unsafe_allow_html=True)

    with cl4:
        q = "Total Retail Sales"
        st.markdown("""
                <html>
                <head>
                <style>
                .onew{
                        background: #6644da;
                        border-radius: 14px;
                        padding: 30px 50px 110px 35px;
                        width: 350px;
                        height: 20px;
                        font-size: 20px;
                        color:white;
                        line-height: 1;
                        text-align: center;
                        font-weight:bold;
                 }
                .oneplusw{
                fond-weight:bold;
                line-height: 2.8;
                margin-left:10px;
                font-size: 30px;
                }
                </style>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                </head>
                    <body>
                        <div class="container-fluid onew">%s
                        <div class= "container-fluid oneplusw">%i
                        </div>
                        </div>
                    </body>
                </html>
                """ % (q, w3_val), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    coll1, coll2 = st.columns([15, 2])
    with coll1:
        dfg = st.selectbox("Please select the report", ["Retail Users Logged", "Retail Stock In through TP", "Retail Sales"])
    with coll2:
        if dfg == "Retail Users Logged":
            if select == "Yes":
                datan  = data1.copy()
                rau = datan.set_index(['last_login_time'])
                tab = rau.loc[str(fdy):str(tdy)]
                tab.reset_index(inplace=True)
                lld = tab.pop('last_login_time')
                tab.insert(4, 'last_login_time', lld)
                tab1 = tab
            else:
                ra1 = data_limit1
                ra1['last_login_time'] = pd.to_datetime(ra1['last_login_time'])
                rau = ra1.set_index(['last_login_time'])
                tab = rau.loc[str(fdy):str(tdy)]
                tab.reset_index(inplace=True)
                lld = tab.pop('last_login_time')
                tab.insert(4, 'last_login_time', lld)
                tab1 = tab
        elif dfg == "Retail Stock In through TP":
            if select == "Yes":
                data2["date"] = pd.to_datetime(data2["date"])
                rsi = data2.set_index(['date'])
                rsi1 = rsi.loc[str(fdy):str(tdy)]
                rsi1.reset_index(inplace=True)
                rld = rsi1.pop('date')
                rsi1.insert(4, 'date', rld)
                rsi1["date"] = pd.to_datetime(rsi1["date"]).dt.date
                tab1 = rsi1
            else:
                ra2 = data_limit2
                ra2["date"] = pd.to_datetime(ra2["date"])
                rsi = ra2.set_index(['date'])
                rsi1 = rsi.loc[str(fdy):str(tdy)]
                rsi1.reset_index(inplace=True)
                rld = rsi1.pop('date')
                rsi1.insert(4, 'date', rld)
                rsi1["date"] = pd.to_datetime(rsi1["date"]).dt.date
                tab1 = rsi1
        else:
            if select == "Yes":
                data3["created_date"] = pd.to_datetime(data3["created_date"])
                rst = data3.set_index(['created_date'])
                rst1 = rst.loc[str(fdy):str(tdy)]
                rst1.reset_index(inplace=True)
                rlt = rst1.pop('created_date')
                rst1.insert(3, 'created_date', rlt)
                rst1["created_date"] = pd.to_datetime(rst1["created_date"]).dt.date
                tab1 = rst1
            else:
                ra3 = data_limit3
                ra3["created_date"] = pd.to_datetime(ra3["created_date"])
                rst = ra3.set_index(['created_date'])
                rst1 = rst.loc[str(fdy):str(tdy)]
                rst1.reset_index(inplace=True)
                rlt = rst1.pop('created_date')
                rst1.insert(3, 'created_date', rlt)
                rst1["created_date"] = pd.to_datetime(rst1["created_date"]).dt.date
                tab1 = rst1
        csv = tab1.to_csv().encode('utf-8')
        st.markdown("")
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv',
        )
    st.markdown("<br>", unsafe_allow_html=True)
    place = st.empty()
    with place.container():
        gb = GridOptionsBuilder.from_dataframe(tab1)
        gb.configure_pagination()
        gridOptions = gb.build()
        data = AgGrid(tab1,
                      gridOptions=gridOptions,
                      enable_enterprise_modules=True,
                      allow_unsafe_jscode=True,
                      height=1440, fit_columns_on_grid_load=True)
    st.markdown(
        """
           <style>
           .main {
           background-color: #FFFFFF;
           }
           </style>
           """,
        unsafe_allow_html=True
    )

    st.markdown("""
        <style>
           #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2.5rem;}
        </style>
        """, unsafe_allow_html=True)
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

~                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
~                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
~                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
