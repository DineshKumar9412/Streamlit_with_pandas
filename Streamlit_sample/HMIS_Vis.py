import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_plotly_events import plotly_events
sumry = pd.read_csv("DMS.csv")
col, col2 = st.columns([15, 1])
with col:
    fls = st.selectbox("Please select the Directorate", sumry["Directorate Name"].unique(), key='4')

def new():
    if 'count' not in st.session_state:
        st.session_state['count'] = 0
    placeholders = st.empty()
    with placeholders.container():
        sd = st.radio("", ['None', 'Ascending', 'Descending'], key=st.session_state.count + 2)
        st.write(
            '<style>div.row-widget.stRadio > div{flex-direction:row;border-radius: 15px 15px; height: 10px; width: 200000px;}</style>',
            unsafe_allow_html=True)

    with st.empty():
        fig = px.bar(ddd, x="x_axis", y="y_axis", color="Directorate Name", barmode="relative", text_auto=True,
                     color_discrete_sequence=px.colors.cyclical.Twilight,
                     title="<b>{} Metric status</b> <br>".format(fls.partition(' ')[0]))
        fig.update_layout({
            'plot_bgcolor': 'rgb(229,236,246)',
            'paper_bgcolor': 'rgb(255,255,255)',
            'title_font_size': 20,
            'title_x': 0.07,
            'height': 650,
        })
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        if sd == "None":
           dfms = plotly_events(fig, click_event=True, select_event=True, override_height=650, key= st.session_state.count + 3)

        elif sd == "Ascending":
            fig.update_layout(barmode='relative', xaxis={'categoryorder': 'total ascending'})
            dfms = plotly_events(fig, click_event=True, select_event=True, override_height=650,
                                 key=st.session_state.count + 2)
        else:
            fig.update_layout(barmode='relative', xaxis={'categoryorder': 'total descending'})
            dfms = plotly_events(fig, click_event=True, select_event=True, override_height=650,
                                 key=st.session_state.count + 2)
        if len(dfms) > 0:
            placeholders.empty()
            st.session_state.count += 1
            dgh = pd.read_csv("DMS1.csv")
            dgb = dgh[dgh["Directorate Name"] == fls]
            # print(dfms[0]['x'])
            hh = dgb[dgb["Metric"] == dfms[0]['x']]
            print(hh)
            # fig = px.bar(hh, x="Facility Name", y="Percentage", color="", barmode="relative", text_auto=True,
            #              color_discrete_sequence=px.colors.cyclical.Twilight,
            #              title="<b>{} Metric status</b> <br>".format(fls.partition(' ')[0]))
            #
            # # fig = px.bar(hh, x="Facility Name", y="Percentage")
            # fig.update_layout({
            #     'plot_bgcolor': 'rgb(229,236,246)',
            #     'paper_bgcolor': 'rgb(255,255,255)',
            #     'title_font_size': 20,
            #     'title_x': 0.07,
            #     'height': 650,
            # })
            # fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
            # dfms = plotly_events(fig, click_event=True, select_event=True, override_height=650, key=st.session_state.count + 4)
            # if len(dfms) > 0:
            #     st.session_state.count =+ 1
            #     new()

ddd = sumry[sumry["Directorate Name"] == fls]
if len(ddd) > 0:
    new()


