# import streamlit as st
# import pandas as pd
# import numpy as np
#
# st.set_page_config(
#     page_title = 'Streamlit Sample Dashboard Template',
#     layout = 'wide'
# )
#
# st.markdown("## DASH BOARD")
#
# # kpi = st.beta_columns(1)
# #
# # with kpi:
# #     st.markdown("** FIRST PAGE**")
# #     number = 11
# #     st.markdown(f"<h1 style='text-align: center; color: red;'>{number}</h1>", unsafe_allow_html=True)
# #
# # st.markdown("<hr/>",unsafe_allow_html=True)
#
# col1=st.beta_columns(1)
# with col1:
#     st.markdown("** FIRST PAGE**")
#     number = 11
#     st.markdown(f"<h1 style='text-align: center; color: red;'>{number}</h1>", unsafe_allow_html=True)
#
#
#
# # kpi1, kpi2, kpi3 = st.beta_columns(3)
# #
# # with kpi1:
# #     st.markdown("**First KPI**")
# #     number1 = 111
# #     st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)
# #
# # with kpi2:
# #     st.markdown("**Second KPI**")
# #     number2 = 222
# #     st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)
# #
# # with kpi3:
# #     st.markdown("**Third KPI**")
# #     number3 = 333
# #     st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)
# #
# # st.markdown("<hr/>",unsafe_allow_html=True)
# #
# #
# # st.markdown("## KPI Second Row")
# #
# # # kpi 1
# #
# # kpi01, kpi02, kpi03, kpi04, kpi05 = st.beta_columns(5)
# #
# # with kpi01:
# #     st.markdown("**Another 1st KPI**")
# #     number1 = 111
# #     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)
# #
# # with kpi02:
# #     st.markdown("**Another 1st KPI**")
# #     number1 = 222
# #     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)
# #
# # with kpi03:
# #     st.markdown("**Another 1st KPI**")
# #     number1 = 555
# #     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)
# #
# # with kpi04:
# #     st.markdown("**Another 1st KPI**")
# #     number1 = 333
# #     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)
# #
# # with kpi05:
# #     st.markdown("**Another 1st KPI**")
# #     number1 = 444
# #     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)
# #
# # st.markdown("<hr/>",unsafe_allow_html=True)
# #
# # st.markdown("## Chart Layout")
# #
# # chart1, chart2 = st.beta_columns(2)
# #
# # with chart1:
# #     chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
# #     st.line_chart(chart_data)
# #
# # with chart2:
# #     chart_data = pd.DataFrame(np.random.randn(2000, 3),columns=['a', 'b', 'c'])
# #     st.line_chart(chart_data)

import streamlit as st
import pandas as pd
import numpy as np
from  PIL import Image
import plotly.express as px

st.set_page_config(
    page_title = 'Streamlit Sample Dashboard Template',
    layout = 'wide'
)
df = pd.read_csv("train.csv")

# fig = px.bar(df, x="Product", y=["Comfort", "Sound", "Calls"], barmode='group', height=400)


st.markdown("## DASH BOARD")

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("**Another 1st KPI**")
    number1 = 333
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with col2:
    st.markdown("**Another 1st KPI**")
    number1 = 444
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with col3:
    st.markdown("**Another 1st KPI**")
    number1 = 533
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)


dro1, dro2= st.columns(2)

with dro1:
    dfd = df["State"].unique()
    option = st.selectbox('How would you like to be contacted?', dfd, key="one")
    dfg = df[df["State"] == option]
    # print(dfg.head().to_string())
    fig = px.bar(dfg, x="City", y="Sales",color="Segment",
                 barmode="group")
    st.plotly_chart(fig)


with dro2:
    dfd = df["State"].unique()
    option = st.selectbox('How would you like to be contacted?', dfd, key="two")
    dfg = df[df["State"] == option]
    # print(dfg.head().to_string())
    fig = px.line(dfg, x="City", y="Sales", color="Segment")
    st.plotly_chart(fig)

# grp1, grp2= st.columns(2)
#
# with grp1:
#     st.markdown("**Another 1st KPI**")
#     st.plotly_chart(fig)
#
# with grp2:
#     st.markdown("**Another 1st KPI**")
#     st.plotly_chart(fig)




# colll1, colll2 = st.columns(2)
#
# with colll1:
#     st.markdown("**Another 1st KPI**")
#     st.plotly_chart(fig)
#
#     # number1 = 533
#     # st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)
#
# with colll2:
#     st.markdown("**Another 1st KPI**")
#     st.plotly_chart(fig)
#     # number1 = 533
#     # st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)
#
#
# co31, co32 = st.columns(2)
#
# with co31:
#     st.markdown("**Another 1st KPI**")
#     st.plotly_chart(fig)
#
# with co32:
#     st.markdown("**Another 1st KPI**")
#     st.plotly_chart(fig)

# original = Image.open("1771703.jpg")
# col1.header("Original")
# col1.image(original, use_column_width=True)
#
# grayscale = original.convert('LA')
# col2.header("Grayscale")
# col2.image(grayscale, use_column_width=True)


# import streamlit as st
# import time
#
# @st.cache
# def resource_consuming_func(a, b):
#     time.sleep(15)  # This makes the function take 15s to run
#     return a + b
#
# result = resource_consuming_func(a=5, b=10)
#
# st.write(f"Result: {result}")

#
# import streamlit as st
# import pandas as pd
# import plotly.express as px
#
# # continue loading the data with your excel file, I was a bit too lazy to build an Excel file :)
# # df = pd.DataFrame(
# #     [["Product A", 5.6, 7.8, 5], ["Product B", 5.8, 7.2, 4.9]],
# #     columns=["Product", "Comfort", "Sound", "Calls"]
# # )
# df = pd.read_csv("train.csv")
#
# # fig = px.bar(df, x="Product", y=["Comfort", "Sound", "Calls"], barmode='group', height=400)
# fig = px.bar(df, x="City", y= "Sales", color="State",
#                   barmode="group")
# # st.dataframe(df) # if need to display dataframe
# st.plotly_chart(fig)