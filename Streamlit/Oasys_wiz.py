import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
from streamlit_folium import folium_static
import folium
from  PIL import Image
from branca.element import Figure
import duckdb as db
import plotly.express as px
from time import gmtime, strftime
import pytz
from datetime import date, datetime
from streamlit_plotly_events import plotly_events
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
IST = pytz.timezone('Asia/Kolkata')

# # @st.cache
#
# def big_data():
#     df = pd.read_csv("train.csv")
#     return df
df = pd.read_csv("/home/troondxadmin/aimp/csv_file/train.csv")
df['year'] = pd.DatetimeIndex(df['ShipDate']).year
dff = df[df["year"] == 2017]
fin = dff.groupby(["ProductName", "City"])['Sales'].sum().sort_values(ascending=False).reset_index()
# st.write(fin.iloc[0].tolist()[0])
# max_sales = header[2]
# product_name = header[0]
# city= header[1]
# st.write(max_sales)
st.set_page_config(
    page_title = 'Oasys_viz',
    layout="wide"
)
datetime_ist = datetime.now(IST)
times = datetime_ist.strftime('%d:%m:%Y: %H:%M:%S')
mnth = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
mnth_df = pd.DataFrame(mnth)
col21, col22 = st.columns([1,4])
with col21:
    st.markdown('<h1 style="font-family:Courier;text-align:top;color:#09af75; font-size: 30px;">Oasys viz</h1>',
                unsafe_allow_html=True)
with col22:
    st.markdown(f'<p style="text-align:right;color:#09af75;font-size:18px">Date & Time</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:right;color:white;font-size:18px">{times}</p>', unsafe_allow_html=True)
st.sidebar.markdown('<h1 style="font-family:Courier; color:#09af75; font-size: 50px;">Oasys viz</h1>', unsafe_allow_html=True)
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown(f'<p style="color:#8AF572;">Max sale of the Product</p>', unsafe_allow_html=True)
    st.markdown(
        f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:fixed; width: fixed;font-size:40px;'>{fin.iloc[0].tolist()[2]}</h1>",
        unsafe_allow_html=True)
with col2:
    st.markdown(f'<p style="color:#8AF572;">Name of the maximum sold Product</p>', unsafe_allow_html=True)
    # number1 = product_name
    st.markdown(
        f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:fixed; width: fixed;font-size:19.5px;'>{fin.iloc[0].tolist()[0]}</h1>",
        unsafe_allow_html=True)
with col3:
    st.markdown(f'<p style="color:#8AF572;">City name of the product sold</p>', unsafe_allow_html=True)
    # number1 = city
    st.markdown(
        f"<h1 style='text-align: center; color: black; background-color:#09af75;font-family:verdana; border: double; border-radius: 15px 15px; height:fixed; width: fixed;font-size:40px;'>{fin.iloc[0].tolist()[1]}</h1>",
        unsafe_allow_html=True)
st.markdown("<hr/>", unsafe_allow_html=True)


if st.sidebar.checkbox("view data"):
    with st.container():
        df['year'] = pd.DatetimeIndex(df['ShipDate']).year

        x = st.selectbox('Select  year ', df['year'].unique())
        d = df[df["year"] == x]
        st.table(df)
dr11, dr12 = st.columns(2)
dr13, dr14 = st.columns(2)
if st.sidebar.checkbox("Bar chart 1"):
    option = st.sidebar.radio("Do You need filters", ["No", "Yes"],key="1")
    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if option == "No":
        x = st.sidebar.selectbox('Select dimension for X-axis', df.columns,key='1')
        y = st.sidebar.selectbox('Select measure for Y-axis', df.columns,key='1')

        colr = st.sidebar.multiselect('Select additional dimension', df.columns,key='1')
        if st.sidebar.checkbox("Show Bar chat",key='1'):
            if colr==[]:
                fig = px.histogram(df, x=x, y=y ,barmode="group",title="Barchart by the {} and {}".format(x,y))
                sels = plotly_events(fig)

            else:
                fig = px.histogram(df, x=x, y=y, color=colr[0], barmode="group",title="Barchart by the {} and {}".format(x,y))
                sels = plotly_events(fig)

    if option == "Yes":


        x_val = st.sidebar.selectbox("Select dimension for X-axis", df.columns)
        y_val= st.sidebar.selectbox("Select dimension for Y-axis", df.columns)
        c = st.sidebar.multiselect("Select additional dimension", df.columns)
        fil = st.sidebar.selectbox("Select filter", df.columns)
        fils = st.sidebar.selectbox("Select additional filter", df.columns)

        if c == []:
            c = None
        else:
            c = c[0]


        def new():
            if 'count' not in st.session_state:
                st.session_state['count'] = 0
            col, col2 = st.columns(2)
            with col:
                fls = st.multiselect("you selected : {}".format(fil), df[fil].unique(),key="bb")
                frame = df[df[fil].isin(fls)]
            with col2:
                flse = st.multiselect("you selected : {}".format(fils), frame[fils].unique(),key="bb")
            with st.empty():
                fig = px.histogram(df, x=x_val, y=y_val, color=c, barmode="group", title=f"Bar chart by the {x_val} and {y_val}")
                fig.update_layout({
                    'plot_bgcolor': 'rgb(100,100,100)',
                    'paper_bgcolor': 'rgb(38,39,48)',
                    'height': 600,
                })
                st.plotly_chart(fig, use_container_width=True)
                fg = frame[frame[fils].isin(flse)]
                if len(fg) > 0:
                    fig = px.histogram(fg, x=x_val, y=y_val, color=c, barmode="group", title=f"Bar chart by the {x_val} and {y_val}")
                    fig.update_layout({
                        'plot_bgcolor': 'rgb(100,100,100)',
                        'paper_bgcolor': 'rgb(38,39,48)',
                        'font_color': "white",
                        'title_font_family': "Times New Roman",
                        'title_font_color': "white",
                        'legend_title_font_color': "green"
                    })
                    dfm = plotly_events(fig, click_event=True, select_event=True, override_height=600,
                                        key=st.session_state.count)

                    if len(dfm) > 0:
                        st.session_state.count += 1
                        fgs = fg[fg[x_val] == dfm[0]["x"]]
                        fgs['Month'] = pd.DatetimeIndex(fgs['ShipDate']).month
                        fgs['Month'] = fgs.apply(
                            lambda row: '{:%b}'.format(datetime.strptime(str(row['Month']), '%m')),
                            axis=1
                        )
                        dg = fgs.groupby(["Month"])['Sales'].sum().reset_index()
                        dfj = pd.merge(mnth_df, dg, how='outer', on='Month').replace(np.nan, 0)
                        dfd = dfj.round(decimals=2)
                        a = "Month"
                        fig = px.line(dfd, x="Month", y=y_val, text=y_val, markers=True, title=f"Line chart by the {a} and {y_val}")
                        fig.update_traces(textposition="bottom right", marker=dict(size=12, line=dict(width=2)))
                        sels = plotly_events(fig, click_event=True, select_event=True, override_height=600,
                                             key=st.session_state.count + 1)
                        if len(sels) > 0:
                            st.session_state.count += 1
                            new()


        if st.sidebar.checkbox("Show bar"):
            new()

if st.sidebar.checkbox("Bar chart 2"):
    option = st.sidebar.radio("Do You need filters", ["No", "Yes"])
    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if option == "No":
        x = st.sidebar.selectbox('Select dimension for X-axis', df.columns,key="0")
        y = st.sidebar.selectbox('Select measure for Y-axis', df.columns,key="0")

        colr = st.sidebar.multiselect('Select additional dimension', df.columns,key="0")
        if st.sidebar.checkbox("Show Bar chat"):
            if colr == []:
                fig = px.histogram(df, x=x, y=y, barmode="group", title="Barchart by the {} and {}".format(x, y))
                sels = plotly_events(fig)

            else:
                fig = px.histogram(df, x=x, y=y, color=colr[0], barmode="group",
                                   title="Barchart by the {} and {}".format(x, y))
                sels = plotly_events(fig)
    if option == "Yes":
        x_val= st.sidebar.selectbox("Select dimension for X-axis", df.columns,key="aa")
        y_val = st.sidebar.selectbox("Select measure for Y-axis", df.columns,key="aa")
        c = st.sidebar.multiselect("Select additional dimension", df.columns,key="aa")
        fil = st.sidebar.selectbox("Select filter", df.columns,key="aa")
        fils = st.sidebar.selectbox("Select additional filter", df.columns,key="aa")

        if c == []:
            c = None
        else:
            c = c[0]


        def new():
            if 'count' not in st.session_state:
                st.session_state['count'] = 0
            col, col2 = st.columns(2)
            with col:
                fls = st.multiselect("you selected : {}".format(fil), df[fil].unique(),key="aa")
                frame = df[df[fil].isin(fls)]
            with col2:
                flse = st.multiselect("you selected : {}".format(fils), frame[fils].unique(),key="a")
            with st.empty():
                fig = px.histogram(df, x=x_val, y=y_val, color=c, barmode="group", title=f"Bar chart for the {x_val} and {y_val}")
                fig.update_layout({
                    'plot_bgcolor': 'rgb(100,100,100)',
                    'paper_bgcolor': 'rgb(38,39,48)',
                    'height': 600,
                })
                st.plotly_chart(fig, use_container_width=True)
                fg = frame[frame[fils].isin(flse)]
                if len(fg) > 0:
                    fig = px.histogram(fg, x=x_val, y=y_val, color=c, barmode="group", title=f"Bar chart by the {x_val} and {y_val}")
                    fig.update_layout({
                        'plot_bgcolor': 'rgb(100,100,100)',
                        'paper_bgcolor': 'rgb(38,39,48)',
                        'font_color': "white",
                        'title_font_family': "Times New Roman",
                        'title_font_color': "white",
                        'legend_title_font_color': "green"
                    })
                    dfm = plotly_events(fig, click_event=True, select_event=True, override_height=600,
                                        key=st.session_state.count)

                    if len(dfm) > 0:
                        st.session_state.count += 1
                        fgs = fg[fg[x_val] == dfm[0]["x"]]
                        fgs['Month'] = pd.DatetimeIndex(fgs['ShipDate']).month
                        fgs['Month'] = fgs.apply(
                            lambda row: '{:%b}'.format(datetime.strptime(str(row['Month']), '%m')),
                            axis=1
                        )
                        dg = fgs.groupby(["Month"])['Sales'].sum().reset_index()
                        dfj = pd.merge(mnth_df, dg, how='outer', on='Month').replace(np.nan, 0)
                        dfd = dfj.round(decimals=2)
                        a = "Month"
                        fig = px.line(dfd, x=a, y=y_val, text=y_val, markers=True, title=f"Line chart by the {a} and {y_val}")
                        fig.update_traces(textposition="bottom right", marker=dict(size=12, line=dict(width=2)))
                        sels = plotly_events(fig, click_event=True, select_event=True, override_height=600,
                                             key=st.session_state.count + 1)
                        if len(sels) > 0:
                            st.session_state.count += 1
                            new()


        if st.sidebar.checkbox("Show bar",key="aa"):
            new()
if st.sidebar.checkbox("Pie chart 1"):
    x = st.sidebar.selectbox('Select name', df.columns)
    y = st.sidebar.selectbox('Select value', df.columns)
    
    if st.sidebar.checkbox("Show Pie chat"):
        with st.container():
            fig = px.pie(df, values=y, names=x,title="Pie chart by  the {} and {}".format(y,x))

            sel = plotly_events(fig,key="6" )
if st.sidebar.checkbox("Pie chat2"):
    x = st.sidebar.selectbox('Select name', df.columns,key="s")
    y = st.sidebar.selectbox('Select value', df.columns,key="s")
    # colr = st.sidebar.selectbox('select you color value', df.columns)
    if st.sidebar.checkbox("show Pie chat",key="s"):
        with st.container():
            fig = px.pie(df, values=y, names=x,title="Pie chart by the {} and {}".format(y,x))
            sel = plotly_events(fig,key="7" )

if st.sidebar.checkbox("Map chart"):

    with st.empty():
        df = pd.read_csv(
            "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
        dg = df["state"].unique()
        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='active cases',
            color_continuous_scale='Reds', title="INDIAN STATES"
        )
        fig.update_geos(fitbounds="locations", visible=False)
        sel = plotly_events(fig, click_event=True, select_event=True,
                            key="5")
        if len(sel) >0:
            tngdf = gpd.read_file('/home/troondxadmin/aimp/map/perfecttamilnadu.geojson')
            limsdf = pd.read_csv('/home/troondxadmin/aimp/map/lims_gis.csv')
            df = limsdf[["District Name", "Manual Test"]]
            dd = df.groupby(['District Name'])['Manual Test'].sum().reset_index()
            fig = px.choropleth(dd, geojson=tngdf,
                                featureidkey='properties.district',
                                locations="District Name",
                                hover_name="District Name",
                                color="Manual Test",title="You clicked by Tammilnadu map"
                                )
            fig.update_geos(fitbounds="locations", visible=False)
            sel = plotly_events(fig, click_event=True, select_event=True,
                                key="9")
            if len(sel) > 0:
                df = pd.read_csv("/home/troondxadmin/aimp/map/chennai_2.csv")
                fig = px.density_mapbox(df, lat='lat', lon='log', z='sales', radius=10,
                                        center=dict(lat=13.0827, lon=80.2707), zoom=10,
                                        mapbox_style="carto-darkmatter",color_continuous_scale=px.colors.sequential.Rainbow,title="You clicked by Chennai Map")
                fig.update_geos(fitbounds="locations", visible=False)
                fig.update_layout(mapbox_style="stamen-terrain",width=1350, height=700)
                st.plotly_chart(fig)
if st.sidebar.checkbox("Pivot Table"):
    t = pivot_ui(df)
    with open(t.src) as t:
        components.html(t.read(), width=1200, height=550, scrolling=True)

