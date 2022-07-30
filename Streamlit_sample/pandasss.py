# import pandas as pd
# import streamlit as st
# import plotly.express as px
# from streamlit_plotly_events import plotly_events
#
# df = pd.read_csv("train.csv")
#
#
# with st.container():
#     fig = st.empty()
#     a = "State"
#     c = "City"
#     dh = st.multiselect("Please",df["State"].unique())
#     frame = df[df[a].isin(dh)]
#     dh1 = st.multiselect("Please",frame["City"].unique())
#     fg = frame[frame[c].isin(dh1)]
#     my_slider_val = st.slider('Please choose the y-axis grid interval', 0, 35)
#     figs = px.bar(fg, x="City", y="Sales",color="Segment", barmode="group")
#     sel = plotly_events(fig, click_event=True, hover_event=False, select_event=True, key="fcd")
    # fg = sel[0]["pointNumber"]
    # print(fg)





# fig.update_yaxes(rangebreaks=layout.yaxis.rangebreaks[])
# fig.update_yaxes(constrain="range")
# my_slider_val = st.slider('Please choose the y-axis grid interval', 0, 35)
# fig.update_yaxes(nticks=my_slider_val)
# st.plotly_chart(fig)
# #
# sd = st.radio('Sort value', ['Ascending', 'Descending'])
# if sd == "Ascending":
#     fg = frame[frame[c].isin(dh1)]
#     fig = px.bar(fg, x="City", y="Sales", color="Segment")
#     fig.update_layout(barmode='stack', xaxis={'categoryorder':'total ascending'}, yaxis_range=[1, 5000])
#     # fig.update_layout(yaxis_range=[1, 500])
#     st.plotly_chart(fig)
# if sd == "Descending":
#     fg = frame[frame[c].isin(dh1)]
#     fig = px.bar(fg, x="City", y="Sales",color="Segment" )
#     fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
#     fig.update_layout(yaxis_range=[1, 5000])
#     # fig.update_traces(markercolor= "red")
#
#     st.plotly_chart(fig)
# # #
# # # # st.markdown(
# # # #     """
# # # #     <style>
# # # #     .main {
# # # #     background-color: white;
# # # #     }
# # # #     </style>
# # # #     """,
# # # #     unsafe_allow_html=True
# # # # )
# # # #
# # # #
# # # # #
# import pandas as pd
# import streamlit as st
# import plotly.express as px
#
# df = pd.read_csv("train.csv")
#
# sd = st.sidebar.selectbox("How Many Chart You want",[1,2,3,4,5])

# def filter_dict(dic):
#     cols = list(dic.keys())
#     res = df[df[cols].isin(dic).all(1)]
#     print(res.head(10).to_string())




#     return df[df[dic.keys()].apply(
#             lambda x: x.equals(pd.Series(dic.values(), index=x.index, name=x.name)), asix=1)]
#
# filter_dict(df, filter_v)

    # if len(fil_val) == 1:
    #     x = st.sidebar.selectbox('select you X value', df.columns)
    #     y = st.sidebar.selectbox('select you Y value', df.columns)
    #     colr = st.sidebar.selectbox('select you color value', df.columns)
    #     filter1 = st.sidebar.selectbox("select you filder value", df.columns)
    #     return x,y,colr,filter1
    #
    # if len(fil_val) == 2:
    #     x = st.sidebar.selectbox('select you X value', df.columns)
    #     y = st.sidebar.selectbox('select you Y value', df.columns)
    #     colr = st.sidebar.selectbox('select you color value', df.columns)
    #     filter1 = st.sidebar.selectbox("select you filder value", df.columns)
    #     filter2 = st.sidebar.selectbox("select you filder value", df.columns)
#
# def bar(key):
#     option = st.sidebar.radio("Do You need filters", ["No", "Yes"],key=key)
#     if option == "No":
#         x = st.sidebar.selectbox('select you X value', df.columns, key= key)
#         y = st.sidebar.selectbox('select you Y value', df.columns,key= key)
#         colr = st.sidebar.selectbox('select you color value', df.columns,key= key)
#         if st.sidebar.checkbox("show Bar Chart"):
#             fig = px.bar(df, x=x, y=y, color=colr,
#                          barmode="group")
#             # fig.update_layout(width=610, height=450)
#             st.plotly_chart(fig)
#             st.markdown("<hr/>", unsafe_allow_html=True)
#     # if option == "Yes":
#     #     ss = st.sidebar.selectbox("how many filter  you want ", [1, 2, 3, 4, 5])
#     #     if ss == 1:
#     #         x = st.sidebar.selectbox('select you X value', df.columns)
#     #         y = st.sidebar.selectbox('select you Y value', df.columns)
#     #         colr = st.sidebar.selectbox('select you color value', df.columns)
#     #         filter1 = st.sidebar.selectbox("select filter", df.columns)
#     #         if st.sidebar.checkbox("show Bar Chart"):
#     #             fil = st.selectbox("select filter", df[filter1].unique())
#     #
#     #             fig = px.bar(df, x=x, y=y, color=colr,
#     #                          barmode="group")
#     #             # fig.update_layout(width=610, height=450)
#     #             st.plotly_chart(fig)
#     #             st.markdown("<hr/>", unsafe_allow_html=True)
#     #
#     #
#     #     if ss == 2:
#     #         x = st.sidebar.selectbox('select you X value', df.columns)
#     #         y = st.sidebar.selectbox('select you Y value', df.columns)
#     #         colr = st.sidebar.selectbox('select you color value', df.columns)
#     #         filter1 = st.sidebar.selectbox("select you filder value", df.columns)
#     #         filter2 = st.sidebar.selectbox("select you filder value", df.columns)
#     #
#     #     # print(ds)
#     #
#     #     # x = st.sidebar.selectbox('select you X value', df.columns)
#     #     # y = st.sidebar.selectbox('select you Y value', df.columns)
#     #     # colr = st.sidebar.selectbox('select you color value', df.columns)
#     #
#     #
#     #
#     #
#     #     # filder = st.sidebar.multiselect("Filter All ", df.columns)
#     #     # # frame = df[df[a].isin(dh)]
#     #     # frame = df[filder]
#     #
#     #     # print(frame.head().to_string())
#     #     dict = {}
#     #     for a,g in enumerate(range(ss)):
#     #         gh = st.sidebar.selectbox("Filter {} value".format(a), df.columns, key=a)
#     #         gg = st.multiselect('Which one you want to choose?', df[gh].unique(), key=a)
#     #         dict.update({gh : gg})
#     #     # print(dict.keys())
#     #     cols = list(dict.keys())
#     #     res = df[df[cols].isin(dict).all(1)]
#         # if st.checkbox("Show your chart"):
#         #     fig = px.bar(res, x=x, y=y, color=colr,
#         #                  barmode="group")
#         #     # fig.update_layout(width=800, height=500)
#         #     st.plotly_chart(fig)
#         #     st.markdown("<hr/>", unsafe_allow_html=True)
# #
# #
# def ghgh(hkkk):
#     for a, f  in enumerate(range(hkkk)):
#         gh = st.sidebar.selectbox("chart", ["Map","Bar","Line","Pie","scatter"], key=a)
#         if gh == "Bar":
#             bar(a + 1)
# ghgh(sd)

# import pandas as pd
# import numpy as np
# df1 = pd.DataFrame({'A':[1,0,1,1,6], 'B':[1,1,1,0,1], 'C':['right','right','wrong','right', 'right'],'D':[1,2,2,3,4]})
# filter_v = {'A':1, 'B':0, 'C':'right'}
#
# fg = df1.loc[df1[filter_v.keys()].isin(filter_v.values()).all(axis=1), :]
# fg = df1.loc[(df1[list(filter_v)] == pd.Series(filter_v)).all(axis=1)]
# print(df1)
# print(filter_v)
# print(fg)

# import dash
# import dash_core_components as dcc
# import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd
# import streamlit as st
# from streamlit_plotly_events import plotly_events
#
# df = pd.read_csv("train.csv")
#
# fig = px.bar(df, x="City", y="Sales", color="Segment",
#                              barmode="group")
#
# st.plotly_events(fig)
#
# import streamlit as st
# from streamlit_plotly_events import plotly_events
#
# # Writes a component similar to st.write()
# fig = px.line(x=[1], y=[1])
# selected_points = plotly_events(fig)
#
# # Can write inside of things using with!
# with st.beta_expander('Plot'):
#     fig = px.line(x=[1], y=[1])
#     selected_points = plotly_events(fig)
#
# # Select other Plotly events by specifying kwargs
# fig = px.line(x=[1], y=[1])
# selected_points = plotly_events(fig, click_event=False, hover_event=True)

# @app.callback(
#     Output('bar', 'fig'),
#     Input('bar', 'clickData')
# )
# # def ncjdn():
#     ctx = dash.callback_context
#     trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
#     print(trigger_id)

#
# sd = st.sidebar.selectbox("How Many Chart You want",[1,2,3,4,5], key="hfgh")
#
# for i, f in enumerate(range(sd)):
#     gh = st.sidebar.selectbox("chart", ["Map", "Bar", "Line", "Pie", "scatter"], key=i)
#     if gh == "Bar":
#         option = st.sidebar.radio("Do You need filters", ["No", "Yes"],key=i)
#         if option == "No":
#             x = st.sidebar.selectbox('select you X value', df.columns,key=i)
#             y = st.sidebar.selectbox('select you Y value', df.columns,key=i)
#             colr = st.sidebar.selectbox('select you color value', df.columns,key=i)
#             if st.sidebar.checkbox("show Bar Chart",key=i):
#                 fig = px.bar(df, x=x, y=y, color=colr,
#                              barmode="group")
#                 # fig.update_layout(width=610, height=450)
#                 st.plotly_chart(fig)
#                 st.markdown("<hr/>", unsafe_allow_html=True)
#         if option == "Yes":
#             ss = st.sidebar.selectbox("how many filter  you want ", [1, 2, 3, 4, 5], key=i)
#             if ss == 1:
#                 x = st.sidebar.selectbox('select you X value', df.columns,key=i)
#                 y = st.sidebar.selectbox('select you Y value', df.columns,key=i)
#                 colr = st.sidebar.selectbox('select you color value', df.columns,key=i)
#                 filter1 = st.sidebar.selectbox("select filter", df.columns,key=i)
#                 if st.sidebar.checkbox("show Bar Chart",key=i):
#                     fil = st.selectbox("select filter", df[filter1].unique(),key=i)
#                     fig = px.bar(df, x=x, y=y, color=colr,
#                                  barmode="group")
#                     # fig.update_layout(width=610, height=450)
#                     st.plotly_chart(fig)
#                     st.markdown("<hr/>", unsafe_allow_html=True)
# import streamlit as st
# from streamlit_plotly_events import plotly_events
# import plotly.express as px
# import pandas as pd
# import geopandas as gpd
# import numpy as np

# tngdf = gpd.read_file('perfecttamilnadu.geojson')
# # print(tngdf["district"].unique())
# limsdf = pd.read_csv('lims_gis.csv')
# # dd = limsdf.groupby(['District Name']).sum()
# df = limsdf[["District Name","Manual Test"]]
# # uni = df["District Name"].unique()
# # dd =  df.groupby(['District Name', "Manual Test"]).sum().reset_index()
# dd = df.groupby(['District Name'])['Manual Test'].sum().reset_index()
# # dd.set_index('District Name')
# # print(dd)
#
# dd.insert(loc=0, column='row_num', value=np.arange(len(dd)))

# dd['Sno'] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,
#              29,30,31,32,33,34,35,36,37]
#
# res = dd.query('Index == 2')
# print(res)

# fig = px.choropleth(dd, geojson=tngdf,
#                         featureidkey='properties.district',
#                         locations="District Name",
#                         hover_name="District Name",
#                         color="Manual Test"
#                         )
# fig.update_geos(fitbounds="locations", visible=False)


# fig.update_layout(width=1250, height=700)
# st.plotly_chart(fig)



#
# df = pd.read_csv("train.csv")
#
# a = "State"
# c = "City"
# dh = st.multiselect("Please",df["State"].unique())
# frame = df[df[a].isin(dh)]
# dh1 = st.multiselect("Please",frame["City"].unique())
# fg = frame[frame[c].isin(dh1)]
# col1,col2=st.columns(2)
# with col1:
#     figs = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
#     st.plotly_chart(figs)
#     na = "qwes"
#
# with col2:
#     figs = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
#     st.plotly_chart(figs)

    # if na == "qwe":
    #     with col1:
    #         figs = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
    #         st.plotly_chart(figs)
    #
    #     with col2:
    #         figs = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
    #         st.plotly_chart(figs)

# with co1:
#     figs = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
#     sels = plotly_events(fig, click_event=True, hover_event=False, select_event=True,key="fcd")

# Writes a component similar to st.write()
# fig = px.line(x=[1], y=[1])
# selected_points = plotly_events(fig)

# # Can write inside of things using with!
# with st.expander('Plot'):
#     fig = px.line(x=[1], y=[1])
#     selected_points = plotly_events(fig)

# Select other Plotly events by specifying kwargs

# df = px.data.gapminder().query("country=='Canada'")
# fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
# fig.show()
# # fig = px.line(x=[1, 5, 7, 8, 8], y=[1,5, 8,7, 4, 2])
# sel = plotly_events(fig, click_event=True, hover_event=False, select_event=True)
# a=sel[0]
# a = pd.DataFrame.from_dict(a,orient='index')
# print(a)
# #
# fg = sel[0]["pointNumber"]
# dg = dd[dd["row_num"]== fg]
# print(dg["District Name"])


# from time import sleep
# import streamlit as st
#
# widget = st.empty()
# widget.write("original text")
#
# sleep(2)
#
# widget.empty()
# st.write("cleared original text")

# sleep(2)
#
# st.text("end")
# #
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import time
# from streamlit_plotly_events import plotly_events
#
# df = pd.read_csv("train.csv")
# st.sidebar.write("Welcome .....")
# a = "State"
# c = "City"
# dh = st.multiselect("Please", df["State"].unique())
# frame = df[df[a].isin(dh)]
# dh1 = st.multiselect("Please", frame["City"].unique())
# fg = frame[frame[c].isin(dh1)]
#
# if len(fg) > 0:
#     with st.empty():
#         fig = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
#         sel = plotly_events(fig, click_event=True, select_event=True, key="cfcvg") # select_event=True,
#         if len(sel) > 0:
#             fgs = frame[frame[c] == sel[0]["x"]]
#             fig = px.bar(fgs, x="City", y="Sales", color="Segment", barmode="group")
#             sels = plotly_events(fig, click_event=True, select_event=True, key= "hbvcg")
            # print(len(sels))
            # if len(sels) > 0:
            #     with st.empty():
            #         fig = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
            #         sel = plotly_events(fig, click_event=True, select_event=True, key="cfcvgh")




   # dh = empty()





        # empty()
    # if len(dgg) >0:
    #     empty()

    # d = fina[0]["x"]
    # fgs = frame[frame[c]==fina[0]["x"]]
    # fig = px.bar(fgs, x="City", y="Sales", color="Segment", barmode="group")
    # sel = plotly_events(fig, click_event=True, select_event=True, key="fcds")
    # print(sel)

# if len(fg) > 0:
#     with st.empty():
#         fig = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
#         sel = plotly_events(fig, click_event=True, select_event=True, key="fcd")
#
#         if len(sel) > 0:
#             # st.write("Wait.....")
#             # time.sleep(1)
#             fgs = frame[frame[c] == sel[0]["x"]]
#             sels = plotly_events(fgs, click_event=True, select_event=True, key="fcdgt")
#             print(sels)




        # print(sel[0]["pointNumber"])
        # if sel[0]["pointNumber"] >= 0:
        #     time.sleep(1)
        #     st.write("Wait.....")


#
# fig = px.bar(fg, x="City", y="Sales",color="Segment", barmode="group")
# sel = plotly_events(fig, click_event=True, hover_event=False, select_event=True, key="fcd")
# fg = sel[0]["pointNumber"]
# with st.empty():
#     if fg:
#         st.write("bchbhfxbcbvjbxcjvbjxnjnn")

    # fig = px.bar(fg, x="City", y="Sales",color="Segment", barmode="group")
    # st.plotly_chart(fig)
    # time.sleep(1)
    # st.write("Wait.....")
    #
    # figs = px.bar(fg, x="City", y="Sales",color="Segment", barmode="group")
    # sel = plotly_events(fig, click_event=True, hover_event=False, select_event=True, key="fcd")


# cols = st.columns(3)
# if len(fg) > 0:
#     with cols[0]:
#         fig = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
#         # sel = plotly_events(fig, click_event=True, select_event=True, key="fcd")
#         gh = st.plotly_chart(fig)
#         if cols[2].button('Clear'):
#             gh.empty()


    # with cols[1]:
    #     field2 = st.code('name', language="markdown")
    # if cols[2].button('Clear'):
    #     field1.empty()
    #     field2.empty()

# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import time
# from streamlit_plotly_events import plotly_events
#
#
#
#
# df = pd.read_csv("train.csv")
# st.sidebar.write("Welcome .....")
# a = "State"
# c = "City"
# dh = st.multiselect("Please", df["State"].unique())
# frame = df[df[a].isin(dh)]
# dh1 = st.multiselect("Please", frame["City"].unique())
# fg = frame[frame[c].isin(dh1)]

# def sdf():
#     placeholder = st.empty()
#     with placeholder.container():
#         fig = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
#         dfm = plotly_events(fig, click_event=True, select_event=True, key="cfcvg")
#         if len(dfm) > 0:
#             placeholder.empty()
#             with placeholder.container():
#                 fgs = frame[frame[c] == dfm[0]["x"]]
#                 fig = px.bar(fgs, x="City", y="Sales", color="Segment", barmode="group")
#                 sels = plotly_events(fig, click_event=True, select_event=True, key="hbvcg")
#                 if len(sels) > 0:
#                     placeholder.empty()
                    # sdf()
# def sdf(d):
#     with st.empty():
#         print(d)
#         # fig = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
#         # dfm = plotly_events(fig, click_event=True, select_event=True, key= d)
#         # if len(dfm) > 0:
#         #     fgs = frame[frame[c] == dfm[0]["x"]]
#         #     fig = px.bar(fgs, x="City", y="Sales", color="Segment", barmode="group")
#         #     sels = plotly_events(fig, click_event=True, select_event=True, key= d)
#         #     if len(sels) > 0:
#         con = 2
#         sdf(con)
#         con += 1





            # st.plotly_chart(fig)

            # if len(sels) > 0:
            # st.button("hcxxc", on_click=sdf(),key="djfjdn")


                # sdf()

# if len(fg) > 0:
#     sdf()
# #

            # fgs = frame[frame[c] == dfm[0]["x"]]
            # fig = px.bar(fgs, x="City", y="Sales", color="Segment", barmode="group")
            # sels = plotly_events(fig, click_event=True, select_event=True, key= "hbvcg")





# # Clear all those elements:
#         placeholder.empty()


    # placeholder.line_chart({"data": [1, 5, 2, 6]})
    # fig = px.bar(fg, x="City", y="Sales", color="Segment", barmode="group")
    # sel = plotly_events(fig, click_event=True, select_event=True, key="cfcvg") # select_event=True,
    # # if len(sel) > 0:
    #         fgs = frame[frame[c] == sel[0]["x"]]
    #         fig = px.bar(fgs, x="City", y="Sales", color="Segment", barmode="group")
    #         sels = plotly_events(fig, click_event=True, select_event=True, key= "hbvcg")

# # #
# import random
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import time
# from streamlit_plotly_events import plotly_events
#
# df = pd.read_csv("train.csv")
#
# dd = st.sidebar.radio("filter",["No", "Yes"])
#
# if dd == "No":
#     a = st.sidebar.selectbox("X value", df.columns)
#     b = st.sidebar.selectbox("y value", df.columns)
#     c = st.sidebar.multiselect("Color value", df.columns)
#
#     if st.sidebar.checkbox("show bar"):
#         if c == []:
#             c = None
#             fig = px.bar(df, x=a, y=b, color=c, barmode="group")
#             # plotly_events(fig)
#             st.plotly_chart(fig)
#         else:
#             fig = px.bar(df, x=a, y=b, color=c[0], barmode="group")
#             # plotly_events(fig)
#             st.plotly_chart(fig)
#
#
# if dd == "Yes":
#     a = st.sidebar.selectbox("X value", df.columns)
#     b = st.sidebar.selectbox("y value", df.columns)
#     c = st.sidebar.multiselect("Color value", df.columns)
#     fil = st.sidebar.selectbox("Filter", df.columns)
#     fils = st.sidebar.selectbox("Filter 1", df.columns)
#
#     if st.sidebar.checkbox("show bar"):
#         # if c == []:
#         #     c = None
#         #     fig = px.bar(df, x=a, y=b, color=c, barmode="group")
#         #     st.plotly_chart(fig)
#         # else:
#         #     fig = px.bar(df, x=a, y=b, color=c[0], barmode="group")
#         #     st.plotly_chart(fig)
#
#         col, col2= st.columns(2)
#         with col:
#             fls = st.multiselect("you selected : {}".format(fil),  df[fil].unique())
#             frame = df[df[fil].isin(fls)]
#             # print(frame)
#
#         with col2:
#             flse = st.multiselect("you selected : {}".format(fils), frame[fils].unique())
#
#         if c == []:
#             c = None
#         else:
#             c = c[0]
#
#         # def new():
#         #     if 'count' not in st.session_state:
#         #         st.session_state['count'] = 0
#         #     with st.empty():
#         #         fig = px.bar(fg, x=a, y=b, color=c, barmode="group")
#         #         fig.update_layout({
#         #                         'plot_bgcolor': 'rgb(100,100,100)',
#         #                         # 'paper_bgcolor':'rgb(0,0,0)',
#         #                     })
#         #
#         #         dfm = plotly_events(fig, click_event=True, select_event=True,key=st.session_state.count)
#         #         if len(dfm) > 0:
#         #             st.session_state.count += 1
#         #             fgs = frame[frame[fils] == dfm[0]["x"]]
#         #             fig = px.bar(fgs, x=a, y=b, color=c,text=a ,barmode="group")
#         #             sels = plotly_events(fig, click_event=True, select_event=True, key=st.session_state.count + 1)
#         #             if len(sels) > 0:
#         #                 st.session_state.count += 1
#         #                 new()
#
#         fg = frame[frame[fils].isin(flse)]
#
#         if len(fg) > 0:
#                 new()


# import random
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import time
# from streamlit_plotly_events import plotly_events
#
# def new():
#     if 'count' not in st.session_state:
#         st.session_state['count'] = 0
#     with st.empty():
#         fig = px.bar(fg, x=c, y=d, color=None, barmode="group")
#         fig.update_layout({
#             'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#             'paper_bgcolor': 'rgba(0, 0, 0, 0)',
#         })
#         dfm = plotly_events(fig, click_event=True, select_event=True, key= st.session_state.count)
#         if len(dfm) > 0:
#             st.session_state.count += 1
#             fgs = frame[frame[c] == dfm[0]["x"]]
#             fig = px.bar(fgs, x=c, y=d, color=col, barmode="group")
#             sels = plotly_events(fig, click_event=True, select_event=True, key = st.session_state.count + 1)
#             if len(sels) > 0:
#                 st.session_state.count += 1
#                 new()
#
# df = pd.read_csv("train.csv")
# st.sidebar.write("Welcome .....")
# a = "State"
# c = "City"
# d = "Sales"
# col = "Segment"
# dh = st.multiselect("Please", df["State"].unique())
# frame = df[df[a].isin(dh)]
# dh1 = st.multiselect("Please", frame["City"].unique())
# fg = frame[frame[c].isin(dh1)]
# if len(fg) > 0:
#     new()


# # 1.notnull  2.fillna  3.dtype(cat) 4. space  5.select_dtypes(wights)
# import pandas as pd
# import datetime as dt
# import streamlit as st
#
#
# def _get_col_dtype(col):
#
#     if col.dtype == "object":
#         # try numeric
#         try:
#             col_new = pd.to_datetime(col.dropna().unique())
#             return col_new.dtype
#         except:
#             try:
#                 col_new = pd.to_numeric(col.dropna().unique())
#                 return col_new.dtype
#             except:
#                 try:
#                     col_new = pd.to_timedelta(col.dropna().unique())
#                     return col_new.dtype
#                 except:
#                     return "object"
#     else:
#         return col.dtype
#
# df = pd.read_csv("train.csv")
#
# for x in df.columns:
#     # print(x)
#     a = _get_col_dtype(df[x])
#     if a == "datetime64[ns]":
#         df[x]= pd.to_datetime(df[x])
#
# date_time_col = df.select_dtypes(include='datetime64').columns
# objects_col = df.select_dtypes(include='object').columns
# integer_col = df.select_dtypes(include='number').columns

# def trim_all_columns(df):
#     trim_strings = lambda x: x.strip() if isinstance(x, str) else x
#     return df.applymap(trim_strings)
#
# # simple example of trimming whitespace from data elements
# # dfs = pd.DataFrame([['  a nnn ', 10], ['  c  ', 5]])
# dfs = trim_all_columns(df)
# print(dfs.head().to_string())

# print(integer_col)
# print(type(df.columns))

# if fg.dtypes == "object":
#    print("yes")
# # print(df.columns[0])
# df_1 = df.iloc[1:]
# df_2=df_1.infer_objects()
# print(type(df_2.columns))
# dfs = df["Ship Date"]
# print(dfs.dtypes)
# if dfs.dtypes == "object":
#     print("yes")


    # col_new = pd.to_datetime(df.dropna().unique())
    # print(col_new.dtype)

#
# print(col_new)
# a = _get_col_dtype(df.columns)
# print(a)
# print(df.dtypes)
# df_1 = df.iloc[1:]
# print(df_1.dtypes)
# df_2=df_1.infer_objects()
# print(df_2.dtypes)

# print(df.info())
# df_new = df.infer_objects()
# print(df_new.info())
# print(df.describe())
# print(df.dtypes)
# print(df.info())

# dte = pd.to_datetime(df["Ship Date"], infer_datetime_format=True)
# print(dte)
# print(df.select_dtypes(include=['datetime64']))

import pandas as pd
import datetime as dt
import streamlit as st
import plotly.express as px
from datetime import *
import numpy as np

dfe = pd.read_csv("train.csv")  #  st Kentucky   ci Henderson
# print(df[["State","City"]].head(50).to_string())
# dh = ["Amarillo","Glendale" ]
# df = dfe[dfe["City"].isin(dh)]
# # print(df)
#
# df['year'] = pd.DatetimeIndex(df['Ship Date']).year
# df['Month'] = pd.DatetimeIndex(df['Ship Date']).month
# dff = df[df["year"] == 2017]
#
#
# dff['Month'] = dff.apply(
#     lambda row: '{:%b}'.format(datetime.strptime(str(row['Month']), '%m')),
#     axis=1
# )
#
# dg = dff.groupby(["Month"])['Sales'].sum().reset_index()
# # print(dg)
#
# mnth = {'Month':['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
#
# mnth_df = pd.DataFrame(mnth)
# jdf = pd.merge(mnth_df,dg, how='outer',on='Month').replace(np.nan, 0)
# # print(jdf)
# fig = px.line(jdf, x ="Month", y ="Sales", text="Month",markers=True)
# fig.add_bar(x="Month", y="Sales", name="Last year")
# fig.update_traces(textposition="bottom right")
# fig.show()
# fig = px.line(jdf, x ="Month", y ="Sales", )
# # fig.update_traces(textposition="bottom right")
# # fig.update_xaxes(categoryorder='array', categoryarray= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# fig.show()
# # st.plotly_chart(fig)



# dff = dff.set_index('Month').sort_index()

# dff['Month'].replace({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May',
#             6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'})
# # look_up = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May',
# #             '6': 'Jun', '7': 'Jul', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# #
# dg = dff.groupby(["Month"])['Sales'].sum().reset_index()

# dff['Month'] = pd.to_datetime(dff['Month'], format='%m').dt.month_name().str.slice(stop=3)
# dff['Month'] = dff['Month'].apply(lambda x: look_up[x])

# dff['Month'] = dff['Month'].apply(lambda x: calendar.month_abbr[x])
# dff['Month'] = pd.DatetimeIndex(pd.to_datetime(dff['Month'], format='%b')).month

# dff = dff.set_index('Month').sort_index()
# # print(dg.head(12))
# dff['Month'] = dff.apply(
#     lambda row: '{:%b}'.format(datetime.strptime(str(row['Month']), '%m')),
#     axis=1
# )
# print(dff)
# dg = dff.groupby(["Month"])['Sales'].sum()
# print(dff.to_string())
# Sort_Dataframeby_MonthandNumeric_cols(df = dff,  monthcolumn='Month',numericcolumn='Sales')

# dg = dff.groupby(["Month"])['Sales'].sum().reset_index()


# fig = px.line(dg, x ="Month", y ="Sales", text="Month",markers=True)
# fig.update_traces(textposition="bottom right")
# fig.show()
# st.plotly_chart(fig)








# dg = dff.groupby(['Product Name','Product ID']).sum()
# dg  = dff.groupby(['Product Name'])['Product ID'].agg('sum')
# dg = dff.groupby(['Product Name', 'Product ID'])['Sales'].sum()
# dg = df.groupby(['Product Name','Product ID'])['Sales'].sum()
# df2 = dff.groupby('Product Name').sum()
# df.groupby(["Rep"]).sum().sort_values("Units", ascending=False)

# dg = dff.groupby(['Product Name', "City"])['Sales'].sum().sort_values(ascending=False)
#
# dg = dff.groupby(['State', "City"])['Sales'].sum().sort_values(ascending=False)
# dg = dff.groupby(['State', "City"])['Sales'].sum().sort_values(ascending=False)
# dg = df[df["State"] == "California"]
# dgs = dg.groupby(['City'])['Sales'].sum().sort_values(ascending=False)
# table = pd.pivot_table(data=dff,index=['City', 'Sales'])
# st.write(table)

# print(table.head())

