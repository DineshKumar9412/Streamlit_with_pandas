import streamlit as st
import pandas as pd
import numpy as np
from  PIL import Image
import plotly.express as px
import json
import geopandas as gpd
from streamlit_folium import folium_static
import folium
from branca.element import Figure
import geemap
from streamlit_plotly_events import plotly_events
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


st.set_page_config(
    page_title = 'Streamlit',
    layout="wide"
)
# st.sidebar.header("Upload your File")
st.markdown('<h1 style="font-family:Courier; color:black; font-size: 50px;">MAP</h1>', unsafe_allow_html=True)
st.markdown("<hr/>", unsafe_allow_html=True)

col1, col2 = st.columns([6,1])
with col1:
    df = pd.read_csv(
            "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
    dg = df["state"].unique()
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='Reds',title="INDIAN STATES"
    )
    fig.update_geos(fitbounds="locations", visible=False)
    # fig.update_layout(width=1500, height=850)
    # st.plotly_chart(fig)
    sel = plotly_events(fig, click_event=True, hover_event=False, override_height=800,
    override_width="100%")
    dat = sel[0]["pointNumber"]

st.markdown("<hr/>", unsafe_allow_html=True)
#
co1, co2 = st.columns([6,1])

with co1:
    if dat == 29:
        tngdf = gpd.read_file('perfecttamilnadu.geojson')
        # print(tngdf["district"].unique())
        limsdf = pd.read_csv('lims_gis.csv')
        # dd = limsdf.groupby(['District Name']).sum()
        df = limsdf[["District Name","Manual Test"]]

        # dd =  df.groupby(['District Name', "Manual Test"]).sum().reset_index()
        dd = df.groupby(['District Name'])['Manual Test'].sum().reset_index()

        # dd = df.groupby(["District Name", "Manual Test"]).size()
        # dd = df.sum(['Manual Test'])
        # dd = df.groupby(['District Name']).sum()
        # print(dd.head(20))

        # dff = dd[dd["District Name"] == "Thiruchirappalli"]

        fig = px.choropleth(dd, geojson=tngdf,
                        featureidkey='properties.district',
                        locations="District Name",
                        hover_name="District Name",
                        color="Manual Test"
                        )
        fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(width=1250, height=700)
        sel = plotly_events(fig, click_event=True, hover_event=False, override_height=800,
                            override_width="100%")
        dat = sel[0]["pointNumber"]
        print(dat)
        # st.plotly_chart(fig)


# with co2:
#     sg = st.multiselect("PLEASE CHOOS STATES NAMES",dd["District Name"], key="gcgbvu")
#     print(sg)

st.markdown("<hr/>", unsafe_allow_html=True)