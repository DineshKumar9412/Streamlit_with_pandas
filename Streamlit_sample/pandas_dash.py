import streamlit as st
import pandas as pd
import numpy as np
from  PIL import Image
import plotly.express as px

st.set_page_config(
    page_title = 'Streamlit',
    layout="wide"
)

st.sidebar.header("Upload your File")
st.markdown('<h1 style="font-family:Courier; color:#8AF572; font-size: 50px;">Dashboard</h1>', unsafe_allow_html=True)
st.markdown("<hr/>", unsafe_allow_html=True)

df =pd.read_csv("train.csv")
sdd = df["Sales"].sum()
total = round(sdd,4)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'<p style="color:white;font-size:18px">Total Sales</p>', unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: black; background-color:#8AF572;font-family:verdana; border: double; border-radius: 15px 15px; height: 120px; width: 380px;font-size:40px;'>{total}</h1>",
                unsafe_allow_html=True)

with col2:
    st.markdown(f'<p style="color:white;font-size:18px">Total no of Sub categories</p>', unsafe_allow_html=True)
    number1 = 444
    st.markdown(
        f"<h1 style='text-align: center; color: black; background-color:#8AF572;font-family:verdana; border: double; border-radius: 15px 15px; height: 120px; width: 380px;font-size:45px;'>{number1}</h1>",
        unsafe_allow_html=True)

with col3:
    st.markdown(f'<p style="color:white;font-size:18px">First Value</p>', unsafe_allow_html=True)
    number1 = 533
    st.markdown(
        f"<h1 style='text-align: center; color:black; background-color:#8AF572;font-family:verdana; border: double; border-radius: 15px 15px; height: 120px; width: 380px;'>{number1}</h1>",
        unsafe_allow_html=True)

st.markdown("<hr/>", unsafe_allow_html=True)
image_file = st.sidebar.file_uploader("upload your file")
if image_file is not None:
    df = pd.read_csv(image_file)
    if st.sidebar.checkbox("view data"):
        st.write(df)
    dr11, dr12 = st.columns(2)
    dr13, dr14 = st.columns(2)
    dr15, dr16 = st.columns(2)
    if st.sidebar.checkbox("Bar chat"):
        x = st.sidebar.selectbox('select you X value', df.columns)
        y = st.sidebar.selectbox('select you Y value', df.columns)
        colr = st.sidebar.selectbox('select you color value', df.columns)
        con = st.sidebar.selectbox('select you contacted value', df.columns)
        if st.sidebar.checkbox("show Bar Chart"):
            with dr11:
                dfd = df[con].unique()
                option = st.selectbox('How would you like to be contacted?', dfd, key="one")
                dfg = df[df[con] == option]
                # print(dfg.head().to_string())
                fig = px.bar(dfg, x=x, y=y, color=colr,
                             barmode="group")
                fig.update_layout(width=500, height=400)
                st.plotly_chart(fig)

    if st.sidebar.checkbox("Line chat"):
        x = st.sidebar.selectbox('select you X value', df.columns, key="one")
        y = st.sidebar.selectbox('select you Y value', df.columns, key="one")
        colr = st.sidebar.selectbox('select you color value', df.columns, key="one")
        con = st.sidebar.selectbox('select you contacted value', df.columns, key="one")
        if st.sidebar.checkbox("show line chart"):
            with dr12:
                dfd = df[con].unique()
                option = st.selectbox('How would you like to be contacted?', dfd, key="two")
                dfg = df[df[con] == option]
                # print(dfg.head().to_string())
                fig = px.line(dfg, x=x, y=y, color=colr)
                # st.plotly_chart(fig,use_container_width=True)
                fig.update_layout(width=500, height=400)

                st.plotly_chart(fig)
    if st.sidebar.checkbox("Pie chat"):
        x = st.sidebar.selectbox('select your  value', df.columns)
        y = st.sidebar.selectbox('select you names value', df.columns)
        colr = st.sidebar.selectbox('select you color value', df.columns, key="two")
        con = st.sidebar.selectbox('select you contacted value', df.columns, key="two")
        if st.sidebar.checkbox("show Pie chart"):
            with dr13:
                dfd = df[con].unique()
                option = st.selectbox('How would you like to be contacted?', dfd, key="three")
                dfg = df[df[con] == option]
                fig = px.pie(dfg, values=y, names=x)
                fig.update_layout(width=500, height=400)
                st.plotly_chart(fig)
    if st.sidebar.checkbox("Scatter chart"):
        x = st.sidebar.selectbox('select you X value', df.columns, key="three")
        y = st.sidebar.selectbox('select you Y value', df.columns, key="three")
        colr = st.sidebar.selectbox('select you color value', df.columns, key="three")
        con = st.sidebar.selectbox('select you contacted value', df.columns, key="three")
        if st.sidebar.checkbox("show Scatter chart"):
            with dr14:
                dfd = df[con].unique()
                option = st.selectbox('How would you like to be contacted?', dfd, key="four")
                dfg = df[df[con] == option]
                fig = px.scatter(dfg, x=x, y=y, color=colr)
                fig.update_layout(width=500, height=400)
                st.plotly_chart(fig)
    if st.sidebar.checkbox("Pivot Table"):
        x = st.sidebar.selectbox('select you X2 value', df.columns, key="four")
        y = st.sidebar.selectbox('select you Y2 value', df.columns, key="four")
        group = st.sidebar.selectbox('select you Group by value', df.columns)
        val = st.sidebar.selectbox('select your value', df.columns)
        if st.sidebar.checkbox("show Pivot Table "):
            with dr15:
                dfd = df[y].unique()
                option = st.selectbox('How would you like to be contacted?', dfd, key="five")
                dfg = df[df[y] == option]
                fig = pd.pivot_table(dfg, values=val, index=[group, x],
                                     )
                st.write(fig)

