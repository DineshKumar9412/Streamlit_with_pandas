import plotly.express as px
import streamlit as st
import pandas as pd
from streamlit_plotly_events import plotly_events
from datetime import *
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title = 'Streamlit',
    layout="wide"
)

# st.sidebar.title("Oasys Viz Dashboard")
st.sidebar.markdown('<h1 style="font:arial;color:black;font-size:30px;" Oasys Viz Dashboard</h1>',unsafe_allow_html=True)
st.sidebar.caption('<h1 style="font:arial;color:Red;font-size:20px;">Dashboard displays the Sales Performance of ABC Corp for the year 2017</h1>',unsafe_allow_html=True)
#
# @st.cache
# def df():
#    df = pd.read_csv("train.csv")
#    return df
# df = df()
# # df = pd.read_csv("train.csv")
#
# mnth = {'Month':['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
# mnth_df = pd.DataFrame(mnth)
#
# a = st.sidebar.selectbox("X value", df.columns)
# b = st.sidebar.selectbox("y value", df.columns)
# c = st.sidebar.multiselect("Color value", df.columns)
# fil = st.sidebar.selectbox("Filter", df.columns)
# fils = st.sidebar.selectbox("Filter 1", df.columns)
#
# if c == []:
#     c = None
# else:
#     c = c[0]
#
# def new():
#     if 'count' not in st.session_state:
#             st.session_state['count'] = 0
#     col, col2 = st.columns(2)
#     with col:
#         fls = st.multiselect("you selected : {}".format(fil), df[fil].unique())
#         frame = df[df[fil].isin(fls)]
#     with col2:
#         flse = st.multiselect("you selected : {}".format(fils), frame[fils].unique())
#     placeholder = st.empty()
#     with placeholder.container():
#         sd = st.radio("",['None','Ascending','Descending'])
#         st.write(
#             '<style>div.row-widget.stRadio > div{flex-direction:row;border-radius: 15px 15px; height: 10px; width: 200000px;}</style>',
#             unsafe_allow_html=True)
#     with st.empty():
#         fig = px.bar(df, x=a, y=b, color=c, barmode="group",title="Bar_chart",color_discrete_sequence=px.colors.cyclical.Twilight)
#         fig.update_layout({
#                         'plot_bgcolor': 'rgb(249,251,253)',
#                         'paper_bgcolor':'rgb(255,255,255)',
#                         'height': 600,
#                         # 'categoryorder': 'total descending',
#                     })
#         if sd == "None":
#             st.plotly_chart(fig, use_container_width=True)
#         elif sd == "Ascending":
#             fig.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})
#             st.plotly_chart(fig, use_container_width=True)
#         else:
#             fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})
#             st.plotly_chart(fig, use_container_width=True)
#         fg = frame[frame[fils].isin(flse)]   # New York City
#         if len(fg) > 0:
#             fig = px.histogram(fg, x=a, y=b, color=c, barmode="group",
#                                title="<b>Sales by city</b> <br>Overview of sales by city or cities in a state for the year 2017",color_discrete_sequence=px.colors.cyclical.Twilight)
#             fig.update_layout({
#                 'plot_bgcolor': 'rgb(229,236,246)',
#                 'paper_bgcolor':'rgb(255,255,255)',
#                 'font_color': "black",
#                 'title_font_family':"Fredoka One Regular font",
#                 'title_font_color':"black",
#                 'title_font_size': 20,
#                 'title_x' : 0.07,
#                 # 'legend_title_font_color':"green"
#             })
#             # fig.update_layout(title_x=0.5)
#             if sd == "None":
#                 dfm = plotly_events(fig, click_event=True, select_event=True, override_height=650,
#                                     key=st.session_state.count)
#             elif sd == "Ascending":
#                 fig.update_layout(barmode='group', xaxis={'categoryorder': 'total ascending'})
#                 dfm = plotly_events(fig, click_event=True, select_event=True, override_height=600,
#                                     key=st.session_state.count)
#             else:
#                 fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})
#                 dfm = plotly_events(fig, click_event=True, select_event=True, override_height=600,
#                                     key=st.session_state.count)
#             if len(dfm) > 0:
#                 placeholder.empty()
#                 st.session_state.count += 1
#                 fgs = fg[fg[a] == dfm[0]["x"]]
#                 fgs['Month'] = pd.DatetimeIndex(fgs['Ship Date']).month
#                 fgs['Month'] = fgs.apply(
#                     lambda row: '{:%b}'.format(datetime.strptime(str(row['Month']), '%m')),
#                     axis=1
#                 )
#                 dg = fgs.groupby(["Month"])['Sales'].sum().reset_index()
#                 dfj = pd.merge(mnth_df, dg, how='outer', on='Month').replace(np.nan, 0)
#                 dfd = dfj.round(decimals=2)
#                 fig = px.line(dfd, x ="Month", y ="Sales", text="Sales",markers=True,color_discrete_sequence=["#ff4c4b"])
#                 fig.update_traces(textposition = 'top right',textfont = dict(color = '#000000', size = 15),marker=dict(size=12))  #marker=dict(size=12, line=dict(width=2)))
#                 fig2 = px.bar(dfd, x ="Month", y ="Sales",color_discrete_sequence=px.colors.diverging.Tealrose)
#                 fig.add_trace(fig2.data[0])
#                 sels = plotly_events(fig, click_event=True, select_event=True, override_height=650,
#                                      key=st.session_state.count + 1)
#                 if len(sels) > 0:
#                     st.session_state.count += 1
#                     new()
# if st.sidebar.checkbox("show bar"):
#     new()


# import pandas as pd
# #
# df = pd.read_csv("train.csv")
# df['year'] = pd.DatetimeIndex(df['Ship Date']).year
# dff = df[df["year"] == 2017]
# fin = dff.groupby(["Product Name", "City"])['Sales'].sum().sort_values(ascending=False).reset_index()
# # fin.iloc[0].tolist()
# print(fin.iloc[0].tolist()[0])


#pivort Tablr
# import streamlit.components.v1 as components
# from pivottablejs import pivot_ui
# import pandas as pd
# import streamlit as st
# from datetime import datetime
# from datetime import date

# def cache_clear_dt(dummy):
# 	clear_dt = date.today()
# 	return clear_dt
#
# if cache_clear_dt("dummy")<date.today():
# 	caching.clear_cache()

# @st.experimental_memo
# def df():
#    df = pd.read_csv("train.csv")
#    return df
# # df = df()
# # df = pd.read_csv("train.csv")
#
# t = pivot_ui(df())
# with open(t.src) as t:
#     components.html(t.read(), width=1200, height=550, scrolling=True)


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
# fig2.show()