# # container wide Screen
# # width: 1313px;
# # height: 100px;
#
# # container Normal Screen
# #width: 974px;
# #height: 100px;



import streamlit as st
import streamlit.components.v1 as components
from string import Template


st.set_page_config(
    page_title = 'Oasys_viz',
    layout="wide"
)
st.sidebar.subheader("Oasys")


col1,col2,col3, col4 = st.columns(4)

with col1:
    components.html("""
                    <html>
                    <head>
                       <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css">
                    <style>
                    .four{
                    background: linear-gradient(45deg,#4099ff,#73b4ff);
                    border-radius: 13px;
                    padding: 20px;
                    width: 180px;
                    height: 80px;
                    color: #fff;
                    font-size: 25px;
                    line-height: 0.5;
                    }
                    </style>
                    </head>
                    <body>
                    <div class="four">Hello
                       <div>
                       <i class="bi bi-skype" style="font-size: 2.0rem; color: black; line-height:3.5; margin-left:150px"></i>
                       </div
                    </div>
                    </body>
                    </html>""")
with col2:
    components.html("""
                <html>
                <head>
                   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css">
                <style>
                .four{
                background: linear-gradient(45deg,#2ed8b6,#59e0c5);
                border-radius: 13px;
                padding: 20px;
                width: 180px;
                height: 80px;
                color: #fff;
                font-size: 25px;
                line-height: 0.5;
                }
                </style>
                </head>
                <body>
                <div class="four">Hello
                   <div>
                   <i class="bi bi-spotify" style="font-size: 2.0rem; color: black; line-height:3.5; margin-left:150px"></i>
                   </div
                </div>
                </body>
                </html>""")
with col3:
    components.html("""
            <html>
            <head>
               <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css">
            <style>
            .four{
            background: linear-gradient(45deg,#FFB64D,#ffcb80);
            border-radius: 13px;
            padding: 20px;
            width: 180px;
            height: 80px;
            color: #fff;
            font-size: 25px;
            line-height: 0.5;
            }
            </style>
            </head>
            <body>
            <div class="four">Hello
               <div>
               <i class="bi-youtube" style="font-size: 2.0rem; color: black; line-height:3.5; margin-left:150px"></i>
               </div
            </div>
            </body>
            </html>""")
with col4:
    my = 8
    html = f"{my}"
    components.html("""
        <html>
        <head>
           <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css">
        <style>
        .four{
            border-radius: 13px;
            background: linear-gradient(45deg,#FF5370,#ff869a);
            padding: 20px;
            width: 180px;
            height: 80px;
            color: #fff;
            font-size: 25px;
            line-height: 0.5;
        }
        </style>
        </head>
        <body>
        <div class="four">

        </div>
        </body>
        </html>""")
    #.format(my_value= "hari")
# s = Template(sd).safe_substitute(code="We Says Thanks!")
# print(s)
 # <img src = "venv/assets/img/checklist.png" width = "32" height = "32" ></img>
#
# import streamlit as st
# import streamlit.components.v1 as components
#
# # >>> import plotly.express as px
# # >>> fig = px.box(range(10))

# <figure><embed type="image/svg+xml" img src="venv/assets/img/bootstrap.png" width = "230" height = "60" /></figure>
            # <img src = "venv/assets/img/checklist.png" width = "32" height = "32" ></img>
# # >>> fig.write_html('test.html')
#
# st.header("test html import")
#
# HtmlFile = open("test.html", 'r', encoding='utf-8')
# source_code = HtmlFile.read()
# print(source_code)
# components.html(source_code)