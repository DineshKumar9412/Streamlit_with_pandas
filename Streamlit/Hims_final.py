import streamlit as st
import streamlit.components.v1 as components
import plotly.figure_factory as ff
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
import plotly.express as px


st.set_page_config(
    page_title = 'LIMS DASHBOARD',
    layout="wide",
    initial_sidebar_state = 'expanded'
)

@st.cache(allow_output_mutation=True)
def big_data():
    df = pd.read_csv("/home/troondxadmin/aimp/csv_file/hmis_test_cnt.csv")
    return df
df = big_data()

def tabl():
    df["Order_test_date"] = pd.to_datetime(df["Order_test_date"])
    days = pd.DatetimeIndex(df["Order_test_date"].sort_values().unique())
    test_name = pd.read_csv("/home/troondxadmin/aimp/csv_file/test_names.csv")
    first_da = [test_name]
    for h in days:
        da = df[df["Order_test_date"] == h].groupby(["Test_name"])['Test_count'].sum().sort_values(
            ascending=False).reset_index()
        da.rename({'Test_count': h.strftime("%d-%b-%Y")}, axis=1, inplace=True)
        first_da.append(da)
    sd = reduce(lambda left, right: pd.merge(left, right, how='outer', on='Test_name'), first_da).fillna(0)
    sd.drop(sd.filter(regex="Unname"), axis=1, inplace=True)
    # st.table(sd)
    sd[[sd.columns[1], sd.columns[2], sd.columns[3], sd.columns[4], sd.columns[5]]] = sd[
        [sd.columns[1], sd.columns[2], sd.columns[3], sd.columns[4], sd.columns[5]]].astype(int)
    sd["Grand_Total"] = sd.sum(axis=1, numeric_only=True)
    sd = sd.sort_values(ascending=False, by="Grand_Total")
    ro = sd.sum(axis=0, numeric_only=True)
    new_row = {'Test_name': 'Grand_Total', sd.columns[1]: ro[0], sd.columns[2]: ro[1], sd.columns[3]: ro[2],
               sd.columns[4]: ro[3], sd.columns[5]: ro[4], sd.columns[6]: ro[5]}
    sd = sd.append(new_row, ignore_index=True)
    # dictionary = {"wig":int(sd['Grand_Total'].iloc[-1])}
    # with open("sample.json", "w") as outfile:
    #     json.dump(dictionary, ou
    sds = sd[sd["Grand_Total"] != 0]
    return sds
sd = tabl()
c1, c2 = st.columns([8,2])
with c1:
    st.markdown("""
        <html>
            <head>
            </head>
            <body>
                  <h1 style= color:red;line-height:30px;font-family:verdana;font-weight:bold;>&nbsp LIMS DASHBOARD </h1>
            </body>
        </html>
        """, unsafe_allow_html=True)
with c2:
    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST)
    q = datetime_ist.strftime('%d:%m:%Y / %H:%M:%S')
    date,time = q[:10], q[11:]
    st.markdown("""
    <html>
        <head>
        </head>
        <body>
           <div>
              <h3 style=color:red;font-size:32px;font-weight:bold;>Data  &  Time</h3>
           </div>
           <div style=color:black;font-size:28px;font-weight:bold;line-height:0.5;>%s %s
           </div>
        </body>
    </html>
    """%(date, time),unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

col1,col2,col3,col4 =st.columns(4)
with col1:
    place = st.empty()
    with place.container():
        q = "Total No of Test Conducted"
        w = sd['Grand_Total'].iloc[-1]
        st.markdown("""
        <html>
        <head>
        <style>
        .one{
                background: linear-gradient(45deg,#2ed8b6,#59e0c5);
                border-radius: 25px;
                padding: 25px 20px 120px 25px;
                width: 300px;
                height: 20px;
                font-size: 23px;
                line-height: 1;
                font-weight:bold;
                box-shadow: 0.1px 1.9px 3px 0.1px #888888;
                transition: transform 1s;
                border-bottom: 5px solid black;
            }
        .one:hover {
            transform: scale(1.1); / Animation /
            box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
        }
        .oneplus{
        fond-weight:bold;
        line-height: 1.4;
        margin-left:110px;
        font-size: 45px;
        }
        </style>
        </head>
            <body>
                <div class="one">%s
                   <div class= "oneplus">%i
                   </div>
                </div>
            </body>
        </html>
        """ % (q,w), unsafe_allow_html=True)
with col2:
    e = "Total No of Reported Districts"
    r = 36
    st.markdown("""
        <html>
        <head>
        <style>
        .two{   background: linear-gradient(45deg,#4099ff,#73b4ff);
                border-radius: 25px;
                padding: 25px 20px 120px 25px;
                width: 300px;
                height: 20px;
                font-size: 23px;
                line-height: 1.1;
                font-weight:bold;
                box-shadow: 0.1px 1.9px 3px 0.1px #888888;
                transition: transform 1s;
                border-bottom: 5px solid black;
            }
        .two:hover {
            transform: scale(1.1); / Animation /
            box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
        }
        .twoplus{
        fond-weight:bold;
        line-height: 1.3;
        margin-left:170px;
        font-size: 50px;
        }
        </style>
        </head>
            <body>
                <div class="two">%s
                   <div class= "twoplus">%i
                   </div>
                </div>
            </body>
        </html>
        """ % (e, r), unsafe_allow_html=True)
with col3:
    t = "Total No of Reported HUD"
    y = 36
    st.markdown("""
            <html>
            <head>
            <style>
            .three{
                    background: linear-gradient(45deg,#FFB64D,#ffcb80);
                    border-radius: 25px;
                    padding: 25px 20px 120px 25px;
                    width: 300px;
                    height: 20px;
                    font-size: 25px;
                    line-height: 1;
                    font-weight:bold;
                    box-shadow: 0.1px 1.9px 3px 0.1px #888888;
                    transition: transform 1s;
                    border-bottom: 5px solid black;
                }
            .three:hover {
                transform: scale(1.1); / Animation /
                box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
            }
            .threeplus{
            fond-weight:bold;
            line-height: 1.3;
            margin-left:170px;
            font-size: 50px;
            }
            </style>
            </head>
                <body>
                    <div class="three">%s
                       <div class= "threeplus">%i
                       </div>
                    </div>
                </body>
            </html>
    """ % (t, y), unsafe_allow_html=True)
with col4:
    u = "Total No of Reported Facilities"
    i = 2015
    st.markdown("""
                <html>
                <head>
                <style>
                .four{
                        background: linear-gradient(45deg,#FF5370,#ff869a);
                        border-radius: 25px;
                        padding: 25px 20px 120px 25px;
                        width: 300px;
                        height: 20px;
                        font-size: 23px;
                        line-height: 1.1;
                        font-weight:bold;
                        box-shadow: 0.1px 1.9px 3px 0.1px #888888;
                        transition: transform 1s;
                        border-bottom: 5px solid black;
                    }
                .four:hover {
                    transform: scale(1.1); / Animation /
                    box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
                }
                .fourplus{
                fond-weight:bold;
                line-height: 1.1;
                margin-left:140px;
                font-size: 50px;
                }
                </style>
                </head>
                    <body>
                        <div class="four">%s
                           <div class= "fourplus">%i
                           </div>
                        </div>
                    </body>
                </html>
    """ % (u, i), unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

col5,col6,col7,col8 = st.columns([5,5,5,5])

with col5:
    dis1 = st.multiselect("Directorate",df["Facility type"].unique())
    new = (df[df["Facility type"].isin(dis1)])
with col6:
    dis2 = st.multiselect("District",new["District"].unique())
    two = (new[new["District"].isin(dis2)])
with col7:
    dis3 = st.multiselect("HUD",two["HUD"].unique())
    three = (two[two["HUD"].isin(dis3)])
with col8:
    dis4 = st.multiselect("Institution",three["Institution"].unique())
    four = three[three["Institution"].isin(dis4)]
st.markdown("<br>", unsafe_allow_html=True)

places = st.empty()
with places.container():
    gb = GridOptionsBuilder.from_dataframe(sd)
    gb.configure_pagination()

    gridOptions = gb.build()
    data = AgGrid(sd,
                  gridOptions=gridOptions,
                  enable_enterprise_modules=True,
                  allow_unsafe_jscode=True,
                  height=1440)

if len(four) >0:
    flt = pd.read_csv("/home/troondxadmin/aimp/csv_file/test_names.csv")
    flt.drop(flt.filter(regex="Unname"), axis=1, inplace=True)
    four["Order_test_date"] = pd.to_datetime(four["Order_test_date"])
    days = pd.DatetimeIndex(four["Order_test_date"].sort_values().unique())
    all_datta = [flt]
    for s in days:
        da = four[four["Order_test_date"] == s].groupby(["Test_name"])['Test_count'].sum().sort_values(
            ascending=False).reset_index()
        da.rename({'Test_count': s.strftime("%d-%b-%Y")}, axis=1, inplace=True)
        all_datta.append(da)
    sds = reduce(lambda left, right: pd.merge(left, right, how='outer', on='Test_name'), all_datta).fillna(0)
    float_col = sds.select_dtypes(include=['float64'])
    for col in float_col.columns.values:
        sds[col] = sds[col].astype('int64')
    sds["Grand_Total"] = sds.sum(axis=1, numeric_only=True)
    sds = sds.sort_values(ascending=False, by="Grand_Total")
    ro = sds.sum(axis=0, numeric_only=True).to_frame().T.assign(Test_name=['Grand_Total']).to_dict('records')
    # ro = ro.assign(Test_name=['Grand_Total'])
    # ro = ro.to_dict('records')
    sds_final = sds.append(ro, ignore_index=True)
    sds_new = sds_final[sds_final["Grand_Total"] != 0]
    with place.container():
        q = "Total No of Test Conducted"
        w = sds_new['Grand_Total'].iloc[-1]
        st.markdown("""
                <html>
                <head>
                <style>
                .one{
                        background: linear-gradient(45deg,#2ed8b6,#59e0c5);
                        border-radius: 25px;
                        padding: 25px 20px 120px 25px;
                        width: 300px;
                        height: 20px;
                        font-size: 23px;
                        line-height: 1;
                        font-weight:bold;
                        box-shadow: 0.1px 1.9px 3px 0.1px #888888;
                        transition: transform 1s;
                        border-bottom: 5px solid black;
                    }
                .one:hover {
                    transform: scale(1.1); / Animation /
                    box-shadow: 0 0 0px rgba(0, 0, 0, 9.5);
                }
                .oneplus{
                fond-weight:bold;
                line-height: 1.4;
                margin-left:110px;
                font-size: 45px;
                }
                </style>
                </head>
                    <body>
                        <div class="one">%s
                           <div class= "oneplus">%i
                           </div>
                        </div>
                    </body>
                </html>
                """ % (q, w), unsafe_allow_html=True)
    with places.container():
        gb = GridOptionsBuilder.from_dataframe(sds_new)
        gb.configure_pagination()

        gridOptions = gb.build()
        data = AgGrid(sds_new,
                      gridOptions=gridOptions,
                      enable_enterprise_modules=True,
                      allow_unsafe_jscode=True,
                      height=1440)

