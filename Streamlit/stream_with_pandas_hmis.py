import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import plotly.express as px
from time import gmtime, strftime
import pytz
from datetime import date, datetime
from streamlit_plotly_events import plotly_events

IST = pytz.timezone('Asia/Kolkata')
st.set_page_config(
    page_title = 'Oasys_viz',
    layout="wide"
)
# # @st.cache
@st.cache(allow_output_mutation=True)
def big_data():
    df = pd.read_csv("/home/troondxadmin/aimp/csv_file/finhms2.csv")
    return df
dfs = big_data()



df = dfs[["Directorate Name", "Facility Type", "Total Facility Count","Total Live Facility Count","Facility Live count %","Total User Count", "User Login Count", "Users Login  %","Registration Count","Lab Order Count","Admission Count","Total Department Count","Total Active Department Count","Department Using %","Total Doctor Count","Total Doctor Login Count","Doctor Login %","Total Nurse Count","Total Nurse Login Count","Nurse Login %"]]
df["Users Login  %"] = pd.to_numeric(df["Users Login  %"].str.replace("\%",'', regex=True))
df["Facility Live count %"] = pd.to_numeric(df["Facility Live count %"].str.replace("\%",'', regex=True))
df["Department Using %"] = pd.to_numeric(df["Department Using %"].str.replace("\%",'',regex=True))
df["Doctor Login %"] = pd.to_numeric(df["Doctor Login %"].str.replace("\%",'',regex=True))
df["Nurse Login %"] = pd.to_numeric(df["Nurse Login %"].str.replace("\%",'',regex=True))


datetime_ist = datetime.now(IST)
times = datetime_ist.strftime('%d:%m:%Y: %H:%M:%S')
nongt = df[df["Directorate Name"] != "Grand Total"]
x = df[df["Directorate Name"] == "Grand Total"]
#
ulogin = x["Users Login  %"].iloc[0]
Dpt = x["Department Using %"].iloc[0]
dlogin = x["Doctor Login %"].iloc[0]
nlogin = x["Nurse Login %"].iloc[0]

col21, col22 = st.columns([9,3])
with col21:
    st.markdown('<h2 style="font-family:Verdana;text-align:top;color:#4e518b; font-size: 50px;">HMS2.0 Overall Live Report </h2>',
                unsafe_allow_html=True)
    st.caption('Dashboard displays the Overall live User, Doctor and Nurse login in % everyday ')
    st.subheader('Metric values by facility type')
with col22:
    st.markdown(f'<p style="text-align:right;color:#4e518b;font-size:18px">Date & Time</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:right;color:#4e518b;font-size:18px">{times}</p>', unsafe_allow_html=True)
st.sidebar.markdown('<h1 style="font-family:Verdana; color:#4e518b; font-size: 50px;">Oasys viz</h1>', unsafe_allow_html=True)
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown(f'<p style="color:black;">Total User login in %</p>', unsafe_allow_html=True)
    st.markdown(
        f"<h1 style='text-align: center; color:#4e518b;font-family:verdana;border-color:black; border: solid; border-radius: 15px 15px;border-width: 5px 5px; height:fixed; width: fixed;font-size:40px;'>{ulogin}</h1>",
        unsafe_allow_html=True)
with col2:
    st.markdown(f'<p style="color:black;">Total Department usage in %</p>', unsafe_allow_html=True)
    # number1 = product_name
    st.markdown(
        f"<h1 style='text-align: center; color:#4e518b;font-family:verdana;border-color:black; border: solid; border-radius: 15px 15px;border-width: 5px 5px; height:fixed; width: fixed;font-size:40px;'>{Dpt}</h1>",
        unsafe_allow_html=True)
with col3:
    st.markdown(f'<p style="color:black;">Total Doctor login in %</p>', unsafe_allow_html=True)
    # number1 = city
    st.markdown(
        f"<h1 style='text-align: center; color: #4e518b;font-family:verdana;border-color:black; border: solid; border-radius: 15px 15px;border-width: 5px 5px; height:fixed; width: fixed;font-size:40px;'>{dlogin}</h1>",
        unsafe_allow_html=True)
with col4:
    st.markdown(f'<p style="color:black;">Total Nurse login %</p>', unsafe_allow_html=True)
    st.markdown(
        f"<h1 style='text-align: center; color: #4e518b;font-family:verdana;border-color:black; border: solid; border-radius: 15px 15px;border-width: 5px 5px; height:fixed; width: fixed;font-size:40px;'>{nlogin}</h1>",
        unsafe_allow_html=True)
st.markdown("<hr/>", unsafe_allow_html=True)

if st.sidebar.checkbox("View 1"):

    col, col2 = st.columns([15, 1])
    with col:
        fls = st.selectbox("you selected", ["None", "Users Login  %","Facility Live count %","Department Using %", "Doctor Login %", "Nurse Login %"], key='2')
        if fls == "None":
            st.write("Nothing Selected")
        # elif fls == "Users Login  %":
        else:
            sd = st.radio("", ['None', 'Ascending', 'Descending'])
            st.write(
                '<style>div.row-widget.stRadio > div{flex-direction:row;border-radius: 15px 15px; height: 10px; width: 200000px;}</style>',
                unsafe_allow_html=True)
            if sd == "None":
                fig = px.bar(nongt, x=fls, y="Facility Type",color="Directorate Name",barmode="relative",text_auto=True, color_discrete_sequence=px.colors.cyclical.Twilight,title="<b>{} Login status</b> <br>Overview of login percentage by {}".format(fls.partition(' ')[0], fls.partition(' ')[0]))
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'title_font_size': 20,
                    'title_x' : 0.07,
                    'height': 650,
                    # 'xaxis_title': x,
                    # 'categoryorder': 'total descending',
                })
                fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
                dfms = plotly_events(fig, click_event=True, select_event=True, override_height=650,
                                     key="gffh")
                if st.radio("View Data", ["No", "Yes"]) == "Yes":
                    st.markdown("<br>", unsafe_allow_html=True)
                    fin = nongt[nongt["Facility Type"] == dfms[0]['y']]
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.dataframe(fin)
                else:
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.write("Nothing to show, if you need to see data Select Yes")
            elif sd == "Ascending":
                fig = px.bar(nongt, x=fls, y="Facility Type",color="Directorate Name",barmode="relative",text_auto=True,color_discrete_sequence=px.colors.cyclical.Twilight,
                                   title="<b>{} Login status</b> <br>Overview of login percentage by {}".format(fls.partition(' ')[0], fls.partition(' ')[0]))
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'height': 650,
                    'title_font_size': 20,
                    'title_x' : 0.07,

                    # 'categoryorder': 'total descending',
                })
                fig.update_layout(barmode='relative', yaxis={'categoryorder': 'total ascending'})
                fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
                # fig.update_traces(width = 30)

                dfms = plotly_events(fig, click_event=True, select_event=True, override_height=650,
                                     key="gffh")
                if st.radio("View Data", ["No", "Yes"]) == "Yes":
                    st.markdown("<br>", unsafe_allow_html=True)
                    fin = nongt[nongt["Facility Type"] == dfms[0]['y']]
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.dataframe(fin)
                else:
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.write("Nothing to show, if you need to see data Select Yes")
            else:
                fig = px.bar(nongt, x=fls, y="Facility Type",color="Directorate Name",barmode="relative",text_auto=True,color_discrete_sequence=px.colors.cyclical.Twilight,
                                   title="<b>{} Login status</b> <br>Overview of login percentage by {}".format(fls.partition(' ')[0], fls.partition(' ')[0]))
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'height': 650,
                    'title_font_size': 20,
                    'title_x' : 0.07,
                    # 'xaxis_title': x
                    # 'categoryorder': 'total descending',
                })
                fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
                fig.update_layout(barmode='relative', yaxis={'categoryorder': 'total descending'})
                fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
                dfms = plotly_events(fig, click_event=True, select_event=True, override_height=650,
                                     key="gffh")
                # st.markdown("<hr/>", unsafe_allow_html=True)
                if st.radio("View Data", ["No","Yes"]) == "Yes":
                    fin = nongt[nongt["Facility Type"] == dfms[0]['y']]
                    st.markdown("<br>",unsafe_allow_html=True)
                    st.dataframe(fin)
                else:
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.write("Nothing to show, if you need to see data Select Yes")

if st.sidebar.checkbox("View 2"):
    sumry = pd.read_csv("/home/troondxadmin/aimp/csv_file/hmssmry.csv")
    col, col2 = st.columns([15, 1])
    with col:
        fls = st.selectbox("Please select the Directorate", sumry["Directorate Name"].unique(), key='21')
        sd = st.radio("", ['None', 'Ascending', 'Descending'],key='32')
        st.write(
            '<style>div.row-widget.stRadio > div{flex-direction:row;border-radius: 15px 15px; height: 10px; width: 200000px;}</style>',
            unsafe_allow_html=True)

    uln = sumry["Users Login  %"].iloc[0]
    Dp = sumry["Department Using %"].iloc[0]
    dln = sumry["Doctor Login %"].iloc[0]
    nln = sumry["Nurse Login %"].iloc[0]
    fln = sumry["Facility Live count %"].iloc[0]
#--------------------Edited by Ashok
    dfs = sumry[sumry["Directorate Name"] == fls]
#    print(dfs)
    xd = dfs.filter(["Users Login  %","Facility Live count %","Department Using %","Doctor Login %","Nurse Login %"])
#    print(xd.columns)
#    tds = xd.T
#    print(tds.columns)
#    fig = px.bar(tds,x=tds["1"],y=range(0-100),text_auto=True,color_discrete_sequence=px.colors.cyclical.Twilight)
#    fig.update_layout({
#                    'plot_bgcolor': 'rgb(229,236,246)',
#                    'paper_bgcolor': 'rgb(255,255,255)',
#                    'height': 650,
#                    'title_font_size': 20,
#                    'title_x' : 0.07,
                    # 'xaxis_title': x
                    # 'categoryorder': 'total descending',
#                })
#    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
#    fig.update_layout(barmode='relative', yaxis={'categoryorder': 'total descending'})
#    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
