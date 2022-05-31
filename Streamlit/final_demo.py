import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import plotly.express as px
from time import gmtime, strftime
import pytz
from datetime import date, datetime
from streamlit_plotly_events import plotly_events
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
IST = pytz.timezone('Asia/Kolkata')
st.set_page_config(
    page_title = 'Oasys_viz',
    layout="wide"
)
#@st.cache
@st.cache(allow_output_mutation=True)
def big_data():
    df = pd.read_csv("/home/troondxadmin/aimp/csv_file/train.csv")
    return df
df = big_data()
df['year'] = pd.DatetimeIndex(df['ShipDate']).year
dff = df[df["year"] == 2017]
fin = dff.groupby(["ProductName", "City"])['Sales'].sum().sort_values(ascending=False).reset_index()
datetime_ist = datetime.now(IST)
times = datetime_ist.strftime('%d:%m:%Y: %H:%M:%S')
mnth = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
mnth_df = pd.DataFrame(mnth)
col21, col22 = st.columns([8,4])
with col21:
    st.markdown('<h2 style="font-family:Verdana;text-align:top;color:#ff4c4b; font-size: 55px;">Sales Performance Dashboard </h2>',
                unsafe_allow_html=True)
    st.subheader('Dashboard displays the Sales performance of ABC Corp for the year 2017')
with col22:
    st.markdown(f'<p style="text-align:right;color:#ff4c4b;font-size:18px">Date & Time</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:right;color:red;font-size:18px">{times}</p>', unsafe_allow_html=True)
st.sidebar.markdown('<h1 style="font-family:Verdana; color:#ff4c4b; font-size: 50px;">Oasys viz</h1>', unsafe_allow_html=True)
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown(f'<p style="color:black;">Max sale of the Product</p>', unsafe_allow_html=True)
    st.markdown(
        f"<h1 style='text-align: center; color: red; background-color:ivory;font-family:verdana;border-color:black; border: solid; border-radius: 15px 15px;border-width: 5px 5px; height:fixed; width: fixed;font-size:40px;'>{fin.iloc[0].tolist()[2]}</h1>",
        unsafe_allow_html=True)
with col2:
    st.markdown(f'<p style="color:black;">Name of the maximum sold Product</p>', unsafe_allow_html=True)
    # number1 = product_name
    st.markdown(
        f"<h1 style='text-align: center; color: red; background-color:ivory;font-family:verdana;border-color:black; border: solid; border-radius: 15px 15px;border-width: 5px 5px; height:fixed; width: fixed;font-size:19.5px;'>{fin.iloc[0].tolist()[0]}</h1>",
        unsafe_allow_html=True)
with col3:
    st.markdown(f'<p style="color:black;">City name of the product sold</p>', unsafe_allow_html=True)
    # number1 = city
    st.markdown(
        f"<h1 style='text-align: center; color: red; background-color:ivory;font-family:verdana;border-color:black; border: solid; border-radius: 15px 15px;border-width: 5px 5px; height:fixed; width: fixed;font-size:40px;'>{fin.iloc[0].tolist()[1]}</h1>",
        unsafe_allow_html=True)
st.markdown("<hr/>", unsafe_allow_html=True)
if st.sidebar.checkbox("view data"):
    with st.container():
        df['year'] = pd.DatetimeIndex(df['ShipDate']).year

        x = st.selectbox('select  year ', df['year'].unique())
        d = df[df["year"] == x]
        st.table(d)
dr11, dr12 = st.columns(2)
dr13, dr14 = st.columns(2)
if st.sidebar.checkbox("Bar chart 1"):
    option = st.sidebar.radio("Do You need filters", ["No", "Yes"],key="1")
    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if option == "No":
        x = st.sidebar.selectbox('Select dimension for X-axis', df.columns,key='1')
        y = st.sidebar.selectbox('Select measure for Y-axis', df.columns,key='1')
        c= st.sidebar.multiselect('Select additional dimension', df.columns,key='1')
        if c == []:
            c = None
        else:
            c = c[0]
        if st.sidebar.checkbox("Display bar chart",key='1'):

            sd = st.radio("", ['None', 'Ascending', 'Descending'])
            st.write(
                '<style>div.row-widget.stRadio > div{flex-direction:row;border-radius: 15px 15px; height: 10px; width: 200000px;}</style>',
                unsafe_allow_html=True)
            if sd == "None":
                fig = px.histogram(df, x=x, y=y,color=c, barmode="group",color_discrete_sequence=px.colors.cyclical.Twilight,title="<b>Sales by city </b> <br>Overview of sales by city or cities in a state for the year 2017")
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'title_font_size': 20,
                    'title_x' : 0.07,
                    'height': 600,
                    # 'categoryorder': 'total descending',
                })
                st.plotly_chart(fig, use_container_width=True)
            elif sd == "Ascending":
                fig = px.histogram(df, x=x, y=y, color=c, barmode="group",color_discrete_sequence=px.colors.cyclical.Twilight,
                                   title="<b>Sales by city </b> <br>Overview of sales by city or cities in a state for the year 2017")
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'height': 600,
                    'title_font_size': 20,
                    'title_x' : 0.07,

                    # 'categoryorder': 'total descending',
                })
                fig.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})

                st.plotly_chart(fig, use_container_width=True)
            else:
                fig = px.histogram(df, x=x, y=y, color=c, barmode="group",color_discrete_sequence=px.colors.cyclical.Twilight,
                                   title="<b>Sales by city </b> <br>Overview of sales by city or cities in a state for the year 2017")
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'height': 600,
                    'title_font_size': 20,
                    'title_x' : 0.07,
                    # 'categoryorder': 'total descending',
                })
                fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("<hr/>", unsafe_allow_html=True)
    else:
        a = st.sidebar.selectbox("Select dimension for X-axis", df.columns,key='1')
        b = st.sidebar.selectbox("Select measure for Y-axis", df.columns,key='1')
        c = st.sidebar.multiselect("Select additional dimensiion", df.columns,key='1')
        fil = st.sidebar.selectbox("Select filter", df.columns,key='1')
        fils = st.sidebar.selectbox("Select additional filter", df.columns,key='1')
        if c == []:
            c = None
        else:
            c = c[0]
        def new():
            if 'count' not in st.session_state:
                st.session_state['count'] = 0
            col, col2 = st.columns(2)
            with col:
                fls = st.multiselect("you selected : {}".format(fil), df[fil].unique(),key='1')
                frame = df[df[fil].isin(fls)]
            with col2:
                flse = st.multiselect("you selected : {}".format(fils), frame[fils].unique(),key='2')
            placeholder = st.empty()
            with placeholder.container():
                sf = st.radio("", ['None', 'Ascending', 'Descending'])
                st.write(
                    '<style>div.row-widget.stRadio > div{flex-direction:row;border-radius: 15px 15px; height: 10px; width: 200000px;}</style>',
                    unsafe_allow_html=True)
            with st.empty():
                fig = px.histogram(df, x=a, y=b, color=c, barmode="group", title="<b>Sales by city </b> <br>Overview of sales by city or cities in a state for the year 2017",color_discrete_sequence=px.colors.cyclical.Twilight)
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'height': 600,
                    'title_font_size': 20,
                    'title_x' : 0.07,

                    # 'categoryorder': 'total descending',
                })
                if sf == "None":
                    st.plotly_chart(fig, use_container_width=True)
                elif sf == "Ascending":
                    fig.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})
                    st.plotly_chart(fig, use_container_width=True)
                fg = frame[frame[fils].isin(flse)]  # New York City
                if len(fg) > 0:
                    fig = px.histogram(fg, x=a, y=b, color=c, barmode="group", title="<b>Sales by city </b> <br>Overview of sales by city or cities in a state for the year 2017",color_discrete_sequence=px.colors.cyclical.Twilight)
                    fig.update_layout({
                        'plot_bgcolor': 'rgb(229,236,246)',
                        'paper_bgcolor': 'rgb(255,255,255)',
                        'font_color': "black",
                        'title_font_family': "Times New Roman",
                        'title_font_color': "black",
                        'title_font_size': 20,
                    'title_x' : 0.07,
                        # 'legend_title_font_color':"green"
                    })
                    if sf == "None":
                        dfm = plotly_events(fig, click_event=True, select_event=True, override_height=700,
                                            key=st.session_state.count + 1)
                    elif sf == "Ascending":
                        
                        fig.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})
                        dfm = plotly_events(fig, click_event=True, select_event=True, override_height=600,
                                            key=st.session_state.count + 2)
                    else:
                        fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})
                        dfm = plotly_events(fig, click_event=True, select_event=True, override_height=600,
                                            key=st.session_state.count + 2)
                    if len(dfm) > 0:
                        placeholder.empty()
                        st.session_state.count += 1
                        fgs = fg[fg[a] == dfm[0]["x"]]
                        fgs['Month'] = pd.DatetimeIndex(fgs['ShipDate']).month
                        fgs['Month'] = fgs.apply(
                            lambda row: '{:%b}'.format(datetime.strptime(str(row['Month']), '%m')),
                            axis=1
                        )
                        dg = fgs.groupby(["Month"])['Sales'].sum().reset_index()
                        dfj = pd.merge(mnth_df, dg, how='outer', on='Month').replace(np.nan, 0)
                        dfd = dfj.round(decimals=2)
                        fig = px.line(dfd, x="Month", y="Sales", text="Sales", markers=True,title = "Line chart by the Month and Sales")
                        fig.update_traces(textposition="bottom right", marker=dict(size=12, line=dict(width=2)))
                        # fig.add_bar(x="Month", y="Sales", name="Last year")
                        sels = plotly_events(fig, click_event=True, select_event=True, override_height=600,
                                             key=st.session_state.count + 3)
                        if len(sels) > 0:
                            st.session_state.count += 1
                            new()
                            st.markdown("<hr/>", unsafe_allow_html=True)
        if st.sidebar.checkbox("Display bar chart"):
            new()

if st.sidebar.checkbox("Bar chart 2"):
    option = st.sidebar.radio("Do you need filters", ["No", "Yes"],key="2")
    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if option == "No":
        x = st.sidebar.selectbox('Select dimension for X-axis', df.columns,key='2')
        y = st.sidebar.selectbox('Select measure for Y-axis', df.columns,key='2')
        c= st.sidebar.multiselect('Select additional dimension', df.columns,key='2')
        if c == []:
            c = None
        else:
            c = c[0]
        if st.sidebar.checkbox("Show bar chart",key='2'):

            sd = st.radio("", ['None', 'Ascending', 'Descending'],key="2")
            st.write(
                '<style>div.row-widget.stRadio > div{flex-direction:row;border-radius: 15px 15px; height: 10px; width: 200000px;}</style>',
                unsafe_allow_html=True)
            if sd == "None":
                fig = px.histogram(df, x=x, y=y,color=c, barmode="group",color_discrete_sequence=px.colors.cyclical.Twilight,title="<b>Sales by Segment </b> <br>Overview if sales by segment for the year 2017")
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'height': 600,
                    'title_font_color': "black",
                    'title_font_size': 20,
                    
                })
                st.plotly_chart(fig, use_container_width=True)
            elif sd == "Ascending":
                fig = px.histogram(df, x=x, y=y, color=c, barmode="group",color_discrete_sequence=px.colors.cyclical.Twilight,
                                   title="<b>Sales by Segment </b> <br>Overview if sales by segment for the year 2017")
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'height': 600,
                    'title_font_color': "black",
                    'title_font_size': 20,
                    
                })
                fig.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})

                st.plotly_chart(fig, use_container_width=True)
            else:
                fig = px.histogram(df, x=x, y=y, color=c, barmode="group",color_discrete_sequence=px.colors.cyclical.Twilight,
                                   title="<b>Sales by Segment </b> <br>Overview if sales by segment for the year 2017")
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'height': 600,
                    'title_font_color': "black",
                    'title_font_size': 20,
                    
                })
                fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})
                st.plotly_chart(fig, use_container_width=True)
    else:
        a = st.sidebar.selectbox("Select dimension X-axis", df.columns,key='2')
        b = st.sidebar.selectbox("Select measure Y-axis", df.columns,key='2')
        c = st.sidebar.multiselect("Select additional dimension", df.columns,key='2')
        fil = st.sidebar.selectbox("Select filter", df.columns,key='2')
        fils = st.sidebar.selectbox("Select additional filter", df.columns,key='2')
        if c == []:
            c = None
        else:
            c = c[0]
        def new_one():
            if 'count' not in st.session_state:
                st.session_state['count'] = 0
            col, col2 = st.columns(2)
            with col:
                fls = st.multiselect("you selected : {}".format(fil), df[fil].unique(),key='2')
                frame = df[df[fil].isin(fls)]
            with col2:
                flse = st.multiselect("you selected : {}".format(fils), frame[fils].unique(),key='3')
            placeholders = st.empty()
            with placeholders.container():
                sd = st.radio("", ['None', 'Ascending', 'Descending'],key='2')
                st.write(
                    '<style>div.row-widget.stRadio > div{flex-direction:row;border-radius: 15px 15px; height: 10px; width: 200000px;}</style>',
                    unsafe_allow_html=True)
            with st.empty():
                fig = px.histogram(df, x=a, y=b, color=c, barmode="group", title="<b>Sales by Segment </b> <br>Overview if sales by segment for the year 2017",color_discrete_sequence=px.colors.cyclical.Twilight)
                fig.update_layout({
                    'plot_bgcolor': 'rgb(229,236,246)',
                    'paper_bgcolor': 'rgb(255,255,255)',
                    'height': 600,
                    'title_font_color': "black",
                    'title_font_size': 20,
                })
                if sd == "None":
                    st.plotly_chart(fig, use_container_width=True)
                elif sd == "Ascending":
                    fig.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})
                    st.plotly_chart(fig, use_container_width=True)
                fgm = frame[frame[fils].isin(flse)]  # New York City
                if len(fgm) > 0:
                    fig = px.histogram(fgm, x=a, y=b, color=c, barmode="group", title="<b>Sales by Segment </b> <br>Overview if sales by segment for the year 2017",color_discrete_sequence=px.colors.cyclical.Twilight)
                    

                    fig.update_layout({
                        'plot_bgcolor': 'rgb(229,236,246)',
                        'paper_bgcolor': 'rgb(255,255,255)',
                        'font_color': "black",
                        'title_font_family': "Times New Roman",
                        'title_font_color': "black",
                        'title_font_color': "black",
                        'title_font_size': 20,

                        
                    })
                    if sd == "None":
                        dfms = plotly_events(fig, click_event=True, select_event=True, override_height=700,
                                            key=st.session_state.count + 5)
                    elif sd == "Ascending":
                        fig.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})
                        dfms = plotly_events(fig, click_event=True, select_event=True, override_height=600,
                                            key=st.session_state.count + 2)
                    else:
                        fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})
                        dfms = plotly_events(fig, click_event=True, select_event=True, override_height=600,
                                            key=st.session_state.count + 2)
                    if len(dfms) > 0:
                        placeholders.empty()
                        st.session_state.count += 1
                        fgss = fgm[fgm[a] == dfms[0]["x"]]
                        fgss['Month'] = pd.DatetimeIndex(fgss['ShipDate']).month
                        fgss['Month'] = fgss.apply(
                            lambda row: '{:%b}'.format(datetime.strptime(str(row['Month']), '%m')), axis=1)
                        dg = fgss.groupby(["Month"])['Sales'].sum().reset_index()
                        dfj = pd.merge(mnth_df, dg, how='outer', on='Month').replace(np.nan, 0)
                        dfd = dfj.round(decimals=2)
                        fig = px.line(dfd, x="Month", y="Sales", text="Sales", markers=True,title = "Line chart by the month and sales")
                        fig.update_traces(textposition="bottom right", marker=dict(size=12, line=dict(width=2)))
                        
                        sels = plotly_events(fig, click_event=True, select_event=True, override_height=600,key=st.session_state.count + 3)
                        if len(sels) > 0:
                            st.session_state.count += 1
                            new_one()
        if st.sidebar.checkbox("Display bar cart"):
            new_one()
if st.sidebar.checkbox("Pie chart 1"):
    x = st.sidebar.selectbox('Select name', df.columns)
    y = st.sidebar.selectbox('Select value', df.columns)
    
    if st.sidebar.checkbox("Display pie chart"):
        with st.container():
            fig = px.pie(df, values=y, names=x,title="Sales contribution  by {}".format(x),color_discrete_sequence=px.colors.cyclical.Twilight)

            sel = plotly_events(fig,key="6",override_height=600 )
if st.sidebar.checkbox("Pie chart 2"):
    x = st.sidebar.selectbox('Select name', df.columns,key="s")
    y = st.sidebar.selectbox('Select value', df.columns,key="s")
    if st.sidebar.checkbox("Display pie chart",key="s"):
        with st.container():
            fig = px.pie(df, values=y, names=x,title="Sales contibution  by  {}".format(x),color_discrete_sequence=px.colors.cyclical.Twilight)
            sel = plotly_events(fig,key="7",override_height=600 )
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
            color_continuous_scale='Reds', title="Heat map for india state"
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
                                color="Manual Test",title="You clicked Tammilnadu map"
                                )
            fig.update_geos(fitbounds="locations", visible=False)
            sel = plotly_events(fig, click_event=True, select_event=True,
                                key="9")
            if len(sel) > 0:
                df = pd.read_csv("/home/troondxadmin/aimp/map/chennai_2.csv")
                fig = px.density_mapbox(df, lat='lat', lon='log', z='sales', radius=10,
                                        center=dict(lat=13.0827, lon=80.2707), zoom=10,
                                        mapbox_style="carto-darkmatter",color_continuous_scale=px.colors.sequential.Rainbow,title="You clicked chennai map")
                fig.update_geos(fitbounds="locations", visible=False)
                fig.update_layout(mapbox_style="stamen-terrain",width=1350, height=700)
                st.plotly_chart(fig)
if st.sidebar.checkbox("Pivot Table"):
    # newdf = pd.read_csv("train.csv")
    t = pivot_ui(df)
    with open(t.src) as t:
        components.html(t.read(), width=1200, height=550, scrolling=True)



#st.markdown(
 #   """
  #  <style>
   # .main {
    #background-color: #F9EDEB;
    #secondary-background-color: aqua;
    #}
    #</style>
    #""",
    #unsafe_allow_html=True
#)


# st.markdown(
#     """
#     <style>
#     .main {
#     background-color: #F9EDEB;
#     secondary-background-color: aqua;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
