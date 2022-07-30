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
    fig.update_layout(width=1250, height=700)
    st.plotly_chart(fig)

with col2:
    sg = st.selectbox("PLEASE CHOOS STATES NAMES",dg)

st.markdown("<hr/>", unsafe_allow_html=True)

co1, co2 = st.columns([6,1])

with co1:
    if sg == "Tamil Nadu":
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
        fig.update_layout(width=1250, height=700)
        st.plotly_chart(fig)


with co2:
    sg = st.multiselect("PLEASE CHOOS STATES NAMES",dd["District Name"], key="gcgbvu")
    print(sg)

st.markdown("<hr/>", unsafe_allow_html=True)


coq1, coq2 = st.columns(2)

with coq1:

    if sg == ['Chennai']:
        df = pd.read_csv("chennai.csv")

        #1 Map

        # fig = px.scatter_mapbox(df, lat="lat", lon="log",
        #                         color="sales",size="sales", zoom=10,hover_name="Name")  # Creates a "Mapbox map" figure
        # fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(mapbox_style="stamen-terrain",
        #                   margin=dict(b=0, t=0, l=0, r=0),
        #                   width=1350, height=700) #carto-darkmatter #stamen-terrain #carto-positron #stamen-terrain
        #                                                    # mapbox=dict( pitch=60, bearing=30)
        # st.plotly_chart(fig)


        # 2 Map
        # fig = px.scatter_mapbox(df
        #                         , lat="lat"
        #                         , lon="log"
        #                         , color="sales"
        #                         , size="sales"
        #                         , text="Name"
        #                         # , hover_name="Name"
        #                         # , hover_data=["sales"]
        #                         , size_max=15
        #                         , zoom=6
        #                         , color_continuous_scale=px.colors.sequential.Rainbow #IceFire
        #                         )
        #
        # fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(mapbox_style="carto-positron",
        #                   margin=dict(b=0, t=0, l=0, r=0),
        #                   width=1350, height=700) #carto-darkmatter #stamen-terrain #carto-positron #
        #                                                             # mapbox=dict( pitch=60, bearing=30)
        #
        # st.plotly_chart(fig)

        #3 Map
        # fig = px.scatter_mapbox(df, lat='lat', lon='log', color='sales',
        #                         color_continuous_scale=[
        #                             [0.0, "green"],
        #                             [0.5, "green"],
        #                             [0.51111111, "yellow"],
        #                             [0.71111111, "yellow"],
        #                             [0.71111112, "red"],
        #                             [1, "red"]],
        #                         # color_continuous_scale=px.colors.sequential.Rainbow, #px.colors.cyclical.IceFire
        #                         opacity=0.5,size="sales", zoom=10
        #                         )
        # fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(mapbox_style="carto-darkmatter") #carto-darkmatter #stamen-terrain #carto-positron
        # fig.update_layout(margin=dict(b=0, t=0, l=0, r=0)   # mapbox=dict( pitch=60, bearing=30)
        #                   )
        # fig.update_layout(width=1350, height=700)
        # st.plotly_chart(fig)

        # # fig.update_layout(
        # #     hoverlabel=dict(
        # #         bgcolor="red",
        # #         font_size=16,
        # #         font_family="Rockwell"
        # #     )
        # # )
        # # st.plotly_chart(fig, use_container_width=False)


        #2 Map
        # fig = px.density_mapbox(df, lat='lat', lon='log', z='sales', radius=30,
        #                         color_continuous_scale=[
        #                             [0.0, "green"],
        #                             [0.5, "green"],
        #                             [0.51111111, "yellow"],
        #                             [0.71111111, "yellow"],
        #                             [0.71111112, "red"],
        #                             [1, "red"]],
        #                         opacity=0.5,mapbox_style="sales"
        #                         )
        # fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(width=1350, height=700)
        # fig.update_layout(mapbox_style="carto-darkmatter")
        # fig.update_layout(margin=dict(b=0, t=0, l=0, r=0))
        #
        # st.plotly_chart(fig)

        #3Map

        # fig = px.density_mapbox(df, lat='lat', lon='log', z='sales', radius=10,
        #                         center=dict(lat=13.0827, lon=80.2707), zoom=10,
        #                         mapbox_style="carto-darkmatter",color_continuous_scale=px.colors.sequential.Rainbow)
        # fig.update_geos(fitbounds="locations", visible=False)
        # fig.update_layout(width=1350, height=700)
        # st.plotly_chart(fig)


        # fig = Figure(width=1800, height=1000)
        # f = folium.Figure(width=600, height=300)
        # m = geemap.Map().add_to(f)
        # m3 = folium.Map(width=1000, height=600, location=[13.0827, 80.2707], tiles="OpenStreetMap", zoom_start=10)
        #
        # # frame = data[['Latitude', 'Longitude', 'Name of State / UT']].drop_duplicates().head(10)
        #
        # for i in range(0, len(df)):
        #     folium.Marker(
        #         location=[df.iloc[i]['lat'], df.iloc[i]['log']],
        #         popup=df.iloc[i]['Name']
        #     ).add_to(m3)
        #
        # folium_static(m3)

        # f = folium.Figure(width=600, height=300)
        # m = geemap.Map().add_to(f)
        # dem = ee.Image('USGS/SRTMGL1_003')
        # m.addLayer(dem, vis_params, 'SRTM DEM', True, 0.5)
        # m

# with coq2:
#     sg = st.selectbox("PLEASE CHOOS STATES NAMES",dfh, key="gcgbvur")
#
#
# st.markdown("<hr/>", unsafe_allow_html=True)


# import plotly.express as px
# import plotly.graph_objs as go
#
# iris = px.data.iris()
# fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
# fig.add_trace(go.Bar(x=[1,2,3,4], y=[5,6,7,8]))
# fig.show()

# import pandas as pd
# import plotly.express as px
#
# iris = px.data.iris()
# fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
# df = pd.DataFrame({
#     'x':[1,2,3,4],
#     'y':[5,6,7,8],})
# fig2 = px.bar(df, x="x", y="y")
# fig.add_trace(fig2.data[0])
# fig.show()