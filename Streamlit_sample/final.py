import streamlit as st
import pandas as pd
import numpy as np
from  PIL import Image
import plotly.express as px
from time import gmtime, strftime
import pytz
from datetime import datetime
from datetime import date, datetime



IST = pytz.timezone('Asia/Kolkata')


st.set_page_config(
    page_title = 'Streamlit',
    layout="wide"
)

datetime_ist = datetime.now(IST)                             ##979A9A #09af75
times = datetime_ist.strftime('%d:%m:%Y: %H:%M:%S')

st.sidebar.markdown('<h1 style="font-family:Courier; color:#09af75; font-size: 50px;">Dashboard</h1>', unsafe_allow_html=True)


col21, col22 = st.columns([1,4])
with col21:
    st.markdown('<h1 style="font-family:Courier; color:#09af75; font-size: 50px;">Dashboard</h1>',
                unsafe_allow_html=True)
with col22:
    st.markdown(f'<p style="text-align:right;color:#09af75;font-size:18px">Date & Time</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:right;color:white;font-size:18px">{times}</p>', unsafe_allow_html=True)

st.markdown("<hr/>", unsafe_allow_html=True)
#
df =pd.read_csv("train.csv")
# print(df.columns)
sdd = df["Sales"].sum()
total = round(sdd,4)

col21, col22, col23, col24, col25, col26 = st.columns([1.5,1,1.5,1,1.5,1])

with col21:
    fg = ["Sales", "Order Date", "Ship Date"]
    ghh = df[fg]
    sd = st.selectbox("VALUE:", ghh.columns)
    gg = ghh[sd]

with col22:
    rr = st.radio("VALUE:", ["Sum", "Avg","Max","Min"])
    st.write(
        '<style>div.row-widget.stRadio > div{flex-direction:row;border-radius: 15px 15px; height: 10px; width: 140px;}</style>',
        unsafe_allow_html=True)

with col23:
    fg = ["Order Date", "Ship Date"]
    ghh = df[fg]
    st.selectbox("DATE VALUE:", ghh.columns)
    # gg = ghh[sd]

with col24:
    st.radio("VALUE:", ["Max", "Min"])

with col25:
    # fg = ["Sales", "Order Date", "Ship Date"]
    # ghh = df[fg]
    st.selectbox("String VALUE:", ["State","City"])
    # gg = ghh[sd]
with col26:
    st.radio("VALUE:", ["Max", "Min"],key="h")


col1, col2, col3 = st.columns(3)

with col1:
    if rr == "Sum":
        to = gg.sum()
        if type(to) == str:
            st.write("We can't do that")
        else:
            total = round(to, 2)
            av = rr + " of " + sd
            st.markdown(f'<p style="color:white;font-size:18px">{av}</p>', unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:fixed; width: fixed;font-size:40px;'>{total}</h1>",
                        unsafe_allow_html=True)

    elif rr == "Avg":
        if sd == "Sales":
            to = gg.mean()
            total = round(to, 2)
            av = rr + " of " + sd
            st.markdown(f'<p style="color:white;font-size:18px">{av}</p>', unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:fixed; width: fixed;font-size:40px;'>{total}</h1>",
                        unsafe_allow_html=True)
        else:
            st.write("We can't do that")

    elif rr == "Max":
        to = gg.max()
        if type(to) == str:
            total = to
            av = rr + " of " + sd
            st.markdown(f'<p style="color:white;font-size:18px">{av}</p>', unsafe_allow_html=True)
            st.markdown(
                f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:fixed; width: fixed;font-size:40px;'>{total}</h1>",
                unsafe_allow_html=True)
        else:
            total = round(to, 2)
            av = rr + " of " + sd
            st.markdown(f'<p style="color:white;font-size:18px">{av}</p>', unsafe_allow_html=True)
            st.markdown(
                f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:fixed; width: fixed;font-size:40px;'>{total}</h1>",
                unsafe_allow_html=True)

    elif rr == "Min":
        to = gg.min()
        if type(to) == str:
            total = to
            av = rr + " of " + sd
            st.markdown(f'<p style="color:white;font-size:18px">{av}</p>', unsafe_allow_html=True)
            st.markdown(
                f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:fixed; width: fixed;font-size:40px;'>{total}</h1>",
                unsafe_allow_html=True)
        else:
            total = round(to, 2)
            av = rr + " of " + sd
            st.markdown(f'<p style="color:white;font-size:18px">{av}</p>', unsafe_allow_html=True)
            st.markdown(
                f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:fixed; width: fixed;font-size:40px;'>{total}</h1>",
                unsafe_allow_html=True)

with col2:
    st.markdown(f'<p style="color:white;font-size:18px">Total no of Sub categories</p>', unsafe_allow_html=True)
    total = 444
    st.markdown(
        f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:100%; width: 100%;font-size:40px;'>{total}</h1>",
        unsafe_allow_html=True)

with col3:
    st.markdown(f'<p style="color:white;font-size:18px">First Value</p>', unsafe_allow_html=True)
    total = 533
    st.markdown(
        f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:fixed; width: fixed;font-size:40px;'>{total}</h1>",
        unsafe_allow_html=True)

st.markdown("<hr/>", unsafe_allow_html=True)
#
# image_file = st.sidebar.file_uploader("upload your file")
# if image_file is not None:
#     df = pd.read_csv(image_file)
#     if st.sidebar.checkbox("view data"):
#         st.write(df)
#         st.markdown("<hr/>", unsafe_allow_html=True)
#     dr11, dr12 = st.columns(2)
#     dr13, dr14 = st.columns(2)
#     # dr15, dr16 = st.columns(2)
#     if st.sidebar.checkbox("Bar chat"):
#
#         option = st.sidebar.radio("Do You need filters", ["No", "Yes"])
#         st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
#         if option == "No":
#             x = st.sidebar.selectbox('select you X value', df.columns)
#             y = st.sidebar.selectbox('select you Y value', df.columns)
#             colr = st.sidebar.selectbox('select you color value', df.columns)
#             if st.sidebar.checkbox("show Bar Chart"):
#                 with dr11:
#                     fig = px.bar(df, x=x, y=y, color=colr,
#                                  barmode="group")
#                     fig.update_layout(width=610, height=450)
#                     st.plotly_chart(fig)
#                     st.markdown("<hr/>", unsafe_allow_html=True)
#         if option == "Yes":
#             x = st.sidebar.selectbox('select you X axis', df.columns)
#             y = st.sidebar.selectbox('select you Y axis', df.columns)
#             colr = st.sidebar.selectbox('select you color column', df.columns)
#             con = st.sidebar.selectbox('select you filter column', df.columns)
#             if st.sidebar.checkbox("show Bar Chart"):
#                 with dr11:
#                     dfd = df[con].unique()
#                     option = st.selectbox('Which one you want to choose?', dfd, key="one")
#                     dfg = df[df[con] == option]
#                     # print(dfg.head().to_string())
#                     fig = px.bar(dfg, x=x, y=y, color=colr,
#                                  barmode="group")
#                     fig.update_layout(width=610, height=450)
#                     st.plotly_chart(fig)
#                     st.markdown("<hr/>", unsafe_allow_html=True)
#
#     if st.sidebar.checkbox("Line chat"):
#         x = st.sidebar.selectbox('select you X axis', df.columns, key="one")
#         y = st.sidebar.selectbox('select you Y axis', df.columns, key="one")
#         colr = st.sidebar.selectbox('select you color column', df.columns, key="one")
#         con = st.sidebar.selectbox('select you filter column', df.columns, key="one")
#         if st.sidebar.checkbox("show line chart"):
#             with dr12:
#                 dfd = df[con].unique()
#                 option = st.selectbox('Which one you want to choose?', dfd, key="two")
#                 dfg = df[df[con] == option]
#                 # print(dfg.head().to_string())
#                 fig = px.line(dfg, x=x, y=y, color=colr)
#                 # st.plotly_chart(fig,use_container_width=True)
#                 fig.update_layout(width=610, height=450)
#
#                 st.plotly_chart(fig)
#                 st.markdown("<hr/>", unsafe_allow_html=True)
#     if st.sidebar.checkbox("Pie chat"):
#         x = st.sidebar.selectbox('select your value', df.columns)
#         y = st.sidebar.selectbox('select you name ', df.columns)
#         # colr = st.sidebar.selectbox('select you color value', df.columns, key="two")
#         con = st.sidebar.selectbox('select you filter column', df.columns, key="two")
#         if st.sidebar.checkbox("show Pie chart"):
#             with dr13:
#                 dfd = df[con].unique()
#                 option = st.selectbox('Which one you want to choose?', dfd, key="three")
#                 dfg = df[df[con] == option]
#                 fig = px.pie(dfg, values=y, names=x)
#                 fig.update_layout(width=610, height=450)
#                 st.plotly_chart(fig)
#                 st.markdown("<hr/>", unsafe_allow_html=True)
#     if st.sidebar.checkbox("Scatter chart"):
#         x = st.sidebar.selectbox('select you X axis', df.columns, key="three")
#         y = st.sidebar.selectbox('select you Y axis', df.columns, key="three")
#         colr = st.sidebar.selectbox('select you color column', df.columns, key="three")
#         con = st.sidebar.selectbox('select you filter column', df.columns, key="three")
#         if st.sidebar.checkbox("show Scatter chart"):
#             with dr14:
#                 dfd = df[con].unique()
#                 option = st.selectbox('Which one you want to choose?', dfd, key="four")
#                 dfg = df[df[con] == option]
#                 fig = px.scatter(dfg, x=x, y=y, color=colr,size='Sales')
#                 fig.update_layout(width=610, height=450)
#                 st.plotly_chart(fig)
#                 st.markdown("<hr/>", unsafe_allow_html=True)
#     if st.sidebar.checkbox("Pivot Table"):
#         x = st.sidebar.selectbox('select you x value', df.columns, key="four")
#         y = st.sidebar.selectbox('select you y value', df.columns, key="four")
#         group = st.sidebar.selectbox('select you Group by value', df.columns)
#         val = st.sidebar.selectbox('select you filter column', df.columns)
#         if st.sidebar.checkbox("show Pivot Table "):
#             with st.container():
#                 dfd = df[y].unique()
#                 option = st.selectbox('Which one you want to choose?', dfd, key="five")
#                 dfg = df[df[y] == option]
#                 fig = pd.pivot_table(dfg, values=val, index=[group, x])
#                 st.write(fig)
#                 st.markdown("<hr/>", unsafe_allow_html=True)

