# # import streamlit as st
# # import streamlit_authenticator as stauth
# #
# # names = ['John Smith','Rebecca Briggs']
# # usernames = ['jsmith','rbriggs']
# # passwords = ['123','456']
# #
# # hashed_passwords = stauth.Hasher(passwords).generate()
# #
# # authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
# #     'some_cookie_name','some_signature_key',cookie_expiry_days=30)
# #
# #
# # name, authentication_status, username = authenticator.login('Login','main')
# #
# #
# # # if authentication_status:
# # #     st.write('Welcome *%s*' % (name))
# # #     st.title('Some content')
# # # elif authentication_status == False:
# # #     st.error('Username/password is incorrect')
# # # elif authentication_status == None:
# # #     st.warning('Please enter your username and password')
# #
# #
# # # if st.session_state['authentication_status']:
# # #     st.write('Welcome *%s*' % (st.session_state['name']))
# # #     st.title('Some content')
# # # elif st.session_state['authentication_status'] == False:
# # #     st.error('Username/password is incorrect')
# # # elif st.session_state['authentication_status'] == None:
# # #     st.warning('Please enter your username and password')
# #
# # if authentication_status:
# #     authenticator.logout('Logout', 'main')
# #     st.write('Welcome *%s*' % (name))
# #     st.title('Some content')
# # elif authentication_status == False:
# #     st.error('Username/password is incorrect')
# # elif authentication_status == None:
# #     st.warning('Please enter your username and password')
#
# # streamlit_app.py
# # import streamlit as st
# # import pandas as pd
# #
# # st.set_page_config(
# #     page_title = 'LIMS DASHBOARD',
# #     layout="wide",
# #     initial_sidebar_state = 'expanded'
# # )
# #
#
# # def check_password():
# #     """Returns `True` if the user had a correct password."""
# #
# #     def password_entered():
# #         """Checks whether a password entered by the user is correct."""
# #         if (
# #             st.session_state["username"] in st.secrets["passwords"]
# #             and st.session_state["password"]
# #             == st.secrets["passwords"][st.session_state["username"]]
# #         ):
# #             st.session_state["password_correct"] = True
# #             del st.session_state["password"]  # don't store username + password
# #             del st.session_state["username"]
# #         else:
# #             st.session_state["password_correct"] = False
# #
# #     if "password_correct" not in st.session_state:
# #         # First run, show inputs for username + password.
# #         st.text_input("Username", on_change=password_entered, key="username")
# #         st.text_input(
# #             "Password", type="password", on_change=password_entered, key="password"
# #         )
# #         return False
# #     elif not st.session_state["password_correct"]:
# #         # Password not correct, show input + error.
# #         st.text_input("Username", on_change=password_entered, key="username")
# #         st.text_input(
# #             "Password", type="password", on_change=password_entered, key="password"
# #         )
# #         st.error("😕 User not known or password incorrect")
# #         return False
# #     else:
# #         # Password correct.
# #         return True
# #
# # if check_password():
# #     place =st.empty()
# #     with place.container():
# #         aa = st.selectbox("Select any Weights", ["wig1", "wig2", "wig3"])
# #         if aa == "wig2":
# #             with place.container():
# #                 title = st.text_input('Movie title')
# #                 with place.container():
# #                     df = pd.read_csv("file.csv")
# #                     st.write(df)
# #                     st.selectbox("select your bar chart xaxis", df.columns)
# #                     st.selectbox("select your bar chart yaxis", df.columns)
# #
# #
# #
#
#
# # c1, c2, c3 = st.columns([1,6,2])
# #
# # with c1:
# #     st.write("snjsbdmnn")
# # with c2:
# #     st.write("snjsbdmnn")
# # with c3:
# #     st.write("snjsbdmnn")
#
# import streamlit as st
# import pandas as pd
#
#
# st.set_page_config(
#     page_title = 'LIMS DASHBOARD',
#     layout="wide",
#     initial_sidebar_state = 'expanded'
# )
#
#
# st.sidebar.header("MIS REPORTS")
#
#
#
# if st.sidebar.checkbox("Retail"):
#     if st.sidebar.checkbox("Week wise Sales Report"):
#         st.header("Week wise Sales Report")
#         c1, c2, c3, c4, c5, c6 = st.columns(6)
#         with c1:
#             st.selectbox("Year",[2019, 2020, 2021])
#         with c2:
#             st.selectbox("Month",[2019, 2020, 2021])
#         with c3:
#             st.selectbox("Weak",[2019, 2020, 2021])
#         with c4:
#             st.selectbox("Days",[2019, 2020, 2021])
#         with c5:
#             st.date_input('Start Date')
#         with c6:
#             st.date_input('End Date')
#         c11, c12, c13, c14, c15, c16 = st.columns(6)
#         with c11:
#             st.selectbox("License Type", [2019, 2020, 2021])
#         with c12:
#             st.selectbox("Brandwise", [2019, 2020, 2021])
#         with c13:
#             st.selectbox("Entity wise", [2019, 2020, 2021])
#         with c14:
#             st.selectbox("Liquor Typewise", [2019, 2020, 2021])
#         with c15:
#             st.selectbox("Package Size", [2019, 2020, 2021])
#         with c16:
#             st.selectbox("Package Type", [2019, 2020, 2021])
#         st.markdown("""
#         <html>
#         <body>
#            <br>
#         </body>
#         </html>
#         """, unsafe_allow_html=True)
#         cl1, cl2, cl3, cl4, cl5 = st.columns(5)
#         with cl1:
#             q = "Opening Stock - Cases"
#             w = 7000
#             st.markdown("""
#                     <html>
#                     <head>
#                     <style>
#                     .one{
#                             background: #4680ff;
#                             border-radius: 14px;
#                             padding: 25px 20px 65px 25px;
#                             width: 280px;
#                             height: 20px;
#                             font-size: 18px;
#                             color:white;
#                             line-height: 0.1;
#                             text-align: center;
#                             font-weight:bold;
#                         }
#                     .oneplus{
#                     fond-weight:bold;
#                     line-height: 2.3;
#                     margin-left:18px;
#                     font-size: 30px;
#                     }
#                     </style>
#                     </head>
#                         <body>
#                             <div class="one">%s
#                                <div class= "oneplus">%i
#                                </div>
#                             </div>
#                         </body>
#                     </html>
#                     """ % (q, w), unsafe_allow_html=True)
#         with cl2:
#             q = "Opening stock - Bottles"
#             w = 7000
#             st.markdown("""
#                     <html>
#                     <head>
#                     <style>
#                     .ones{
#                             background: #11c15b;
#                             border-radius: 14px;
#                             padding: 25px 20px 65px 25px;
#                             width: 280px;
#                             height: 20px;
#                             font-size: 18px;
#                             color:white;
#                             line-height: 0.1;
#                             text-align: center;
#                             font-weight:bold;
#                         }
#                     .oneplusy{
#                     fond-weight:bold;
#                     line-height: 2.3;
#                     margin-left:10px;
#                     font-size: 30px;
#                     }
#                     </style>
#                     </head>
#                         <body>
#                             <div class="ones">%s
#                                <div class= "oneplusy">%i
#                                </div>
#                             </div>
#                         </body>
#                     </html>
#                     """ % (q, w), unsafe_allow_html=True)
#         with cl3:
#             q = "Total Stock in - Cases"
#             w = 7000
#             st.markdown("""
#                     <html>
#                     <head>
#                     <style>
#                     .oneq{
#                             background: #ffa21d;
#                             border-radius: 14px;
#                             padding: 25px 20px 65px 25px;
#                             width: 280px;
#                             height: 20px;
#                             font-size: 18px;
#                             color:white;
#                             line-height: 0.1;
#                             text-align: center;
#                             font-weight:bold;
#                         }
#                     .oneplusq{
#                     fond-weight:bold;
#                     line-height: 2.3;
#                     margin-left:10px;
#                     font-size: 30px;
#                     }
#                     </style>
#                     </head>
#                         <body>
#                             <div class="oneq">%s
#                                <div class= "oneplusq">%i
#                                </div>
#                             </div>
#                         </body>
#                     </html>
#                     """ % (q, w), unsafe_allow_html=True)
#         with cl4:
#             q = "Total Stock in - Bottles"
#             w = 7000
#             st.markdown("""
#                     <html>
#                     <head>
#                     <style>
#                     .onew{
#                             background: #6644da;
#                             border-radius: 14px;
#                             padding: 25px 20px 65px 25px;
#                             width: 280px;
#                             height: 20px;
#                             font-size: 18px;
#                             color:white;
#                             line-height: 0.1;
#                             text-align: center;
#                             font-weight:bold;
#                         }
#                     .oneplusw{
#                     fond-weight:bold;
#                     line-height: 2.3;
#                     margin-left:10px;
#                     font-size: 30px;
#                     }
#                     </style>
#                     </head>
#                         <body>
#                             <div class="onew">%s
#                                <div class= "oneplusw">%i
#                                </div>
#                             </div>
#                         </body>
#                     </html>
#                     """ % (q, w), unsafe_allow_html=True)
#         with cl5:
#             q = "Total Damaged - Cases"
#             w = 7000
#             st.markdown("""
#                     <html>
#                     <head>
#                     <style>
#                     .oner{
#                             background: #ff5252;
#                             border-radius: 14px;
#                             padding: 25px 20px 65px 25px;
#                             width: 280px;
#                             height: 20px;
#                             font-size: 18px;
#                             color:white;
#                             line-height: 0.1;
#                             text-align: center;
#                             font-weight:bold;
#                         }
#                     .oneplusr{
#                     fond-weight:bold;
#                     line-height: 2.3;
#                     margin-left:10px;
#                     font-size: 30px;
#                     }
#                     </style>
#                     </head>
#                         <body>
#                             <div class="oner">%s
#                                <div class= "oneplusr">%i
#                                </div>
#                             </div>
#                         </body>
#                     </html>
#                     """ % (q, w), unsafe_allow_html=True)
#
#
#
#
#
#
#         # if st.sidebar.checkbox("Monthwise Sales Report"):
#         # if st.sidebar.checkbox("Brandwise Sales Report"):
#         # if st.sidebar.checkbox("Peak Season sales report"):
#         # if st.sidebar.checkbox("Dry day report"):
#         # if st.sidebar.checkbox("Last year sales report"):
#         # if st.sidebar.checkbox("Roll over stock report"):
#         # if st.sidebar.checkbox("Overall Report"):
#         #     if st.sidebar.checkbox("Advance Duty Register"):
#         #         if st.sidebar.checkbox("Non Movement Products"):
#         #         if st.sidebar.checkbox("Zero Stock View"):
#         #         if st.sidebar.checkbox("Expired Products"):
#         #         if st.sidebar.checkbox("Damaged Products"):
#         #         if st.sidebar.checkbox("Consignment Receipt"):
#         #         if st.sidebar.checkbox("Stockin Report"):
#         #         if st.sidebar.checkbox("Import Permit Report"):
#         #         if st.sidebar.checkbox("Import Permit Acceptance Report"):
#         #         if st.sidebar.checkbox("Indent Report"):
#         #         if st.sidebar.checkbox("Indent Acceptance report"):
#         #         if st.sidebar.checkbox("Challan Report"):
#         #         if st.sidebar.checkbox("Dispatch report"):
#         #         if st.sidebar.checkbox("License Report"):
#         #         if st.sidebar.checkbox("Brand And Label Report"):
#         #         if st.sidebar.checkbox("Wastage Report"):
#         #         if st.sidebar.checkbox("Lost and Missing"):
#         #         if st.sidebar.checkbox("Breakage Entry Report"):

import pandas as pd
import streamlit as st
from time import gmtime, strftime
import pytz
from datetime import date, datetime
import  plotly.express as px

st.set_page_config(
    page_title = 'LIMS DASHBOARD',
    layout="wide",
)
@st.cache(allow_output_mutation=True)
def big_data():
    df = pd.read_csv("wids.csv")
    return df
df = big_data()
IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)
times = datetime_ist.strftime('%d:%m:%Y: %H:%M:%S')
col21, col22 = st.columns([9,3])
with col21:
    st.markdown('<h1 style="font-family:Verdana;text-align:top;color:#4e518b; font-size: 50px;">UP Excise Sales Report </h1>',
                unsafe_allow_html=True)
    st.caption('Dashboard displays the Overall sales report ')
with col22:
    st.markdown(f'<p style="text-align:right;color:#4e518b;font-size:18px">Date & Time</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:right;color:#4e518b;font-size:18px">{times}</p>', unsafe_allow_html=True)

df['Date'] =  pd.to_datetime(df['Date']).dt.date

df = df.sort_values(by='Date')
col1, col2 = st.columns(2)

with col1:
    fr = st.selectbox("From Date", df["Date"].unique())
with col2:
    en = st.selectbox("End Date", df["Date"].unique())

sf = df.loc[(df["Date"] >= fr ) & (df["Date"] <= en )]

st.markdown("""
        <html>
        <body>
           <br>
        </body>
        </html>
        """, unsafe_allow_html=True)

cl1, cl2, cl3, cl4, cl5 = st.columns(5)
with cl1:
    q = "Total Cases Sold"
    w = sf["Total Cases Sold (Nos) "].sum()
    st.markdown("""
            <html>
            <head>
            <style>
            .one{
                    background: #4680ff;
                    border-radius: 14px;
                    padding: 25px 20px 65px 25px;
                    width: 250px;
                    height: 20px;
                    font-size: 18px;
                    color:white;
                    line-height: 0.1;
                    text-align: center;
                    font-weight:bold;
                }
            .oneplus{
            fond-weight:bold;
            line-height: 2.3;
            margin-left:18px;
            font-size: 30px;
            }
            </style>
            </head>
                <body>
                    <div class="one">%s
                       <div class= "oneplus">%i
                       </div>
                    </div>
                </body>
            </html>
            """ % (q, w), unsafe_allow_html=True)
with cl2:
    q = "Total Bottles Sold"
    w = sf["Total Bottles Sold (Nos) "].sum()
    st.markdown("""
            <html>
            <head>
            <style>
            .ones{
                    background: #11c15b;
                    border-radius: 14px;
                    padding: 25px 20px 65px 25px;
                    width: 250px;
                    height: 20px;
                    font-size: 18px;
                    color:white;
                    line-height: 0.1;
                    text-align: center;
                    font-weight:bold;
                }
            .oneplusy{
            fond-weight:bold;
            line-height: 2.3;
            margin-left:10px;
            font-size: 30px;
            }
            </style>
            </head>
                <body>
                    <div class="ones">%s
                       <div class= "oneplusy">%i
                       </div>
                    </div>
                </body>
            </html>
            """ % (q, w), unsafe_allow_html=True)
with cl3:
    q = "Total Stock in Cases"
    w = sf["Total Stock In - Cases "].sum()
    st.markdown("""
            <html>
            <head>
            <style>
            .oneq{
                    background: #ffa21d;
                    border-radius: 14px;
                    padding: 25px 20px 65px 25px;
                    width: 250px;
                    height: 20px;
                    font-size: 18px;
                    color:white;
                    line-height: 0.1;
                    text-align: center;
                    font-weight:bold;
                }
            .oneplusq{
            fond-weight:bold;
            line-height: 2.3;
            margin-left:10px;
            font-size: 30px;
            }
            </style>
            </head>
                <body>
                    <div class="oneq">%s
                       <div class= "oneplusq">%i
                       </div>
                    </div>
                </body>
            </html>
            """ % (q, w), unsafe_allow_html=True)
with cl4:
    q = "Total Stock in bottles"
    w = sf["Total Stock In - Bottles "].sum()
    st.markdown("""
            <html>
            <head>
            <style>
            .onew{
                    background: #6644da;
                    border-radius: 14px;
                    padding: 25px 20px 65px 25px;
                    width: 250px;
                    height: 20px;
                    font-size: 18px;
                    color:white;
                    line-height: 0.1;
                    text-align: center;
                    font-weight:bold;
                }
            .oneplusw{
            fond-weight:bold;
            line-height: 2.3;
            margin-left:10px;
            font-size: 30px;
            }
            </style>
            </head>
                <body>
                    <div class="onew">%s
                       <div class= "oneplusw">%i
                       </div>
                    </div>
                </body>
            </html>
            """ % (q, w), unsafe_allow_html=True)
with cl5:
    q = "Total Sale amount"
    w = sf["Total Sale Amount (Rs)"].sum()
    st.markdown("""
            <html>
            <head>
            <style>
            .oner{
                    background: #ff5252;
                    border-radius: 14px;
                    padding: 25px 20px 65px 25px;
                    width: 250px;
                    height: 20px;
                    font-size: 18px;
                    color:white;
                    line-height: 0.1;
                    text-align: center;
                    font-weight:bold;
                }
            .oneplusr{
            fond-weight:bold;
            line-height: 2.3;
            margin-left:10px;
            font-size: 30px;
            }
            </style>
            </head>
                <body>
                    <div class="oner">%s
                       <div class= "oneplusr">%i
                       </div>
                    </div>
                </body>
            </html>
            """ % (q, w), unsafe_allow_html=True)

st.markdown("""
        <html>
        <body>
           <br>
        </body>
        </html>
        """, unsafe_allow_html=True)

st.header("CHART VIEW")

coa1, coa2, coa3, cla4, cla5 = st.columns(5)
with coa1:
    sd, new = df["Brand Name"].unique(), ["Select All"]
    new.extend(sd)
    f = st.multiselect("Brand Name:", new)
    if f == "Select All":
        selected_option_2 = df["Brand Name"].unique()
        r1 = df[df["Brand Name"].isin(selected_option_2)]
    else:
        r1 = df[df["Brand Name"].isin(f)]
with coa2:
    sd1, new1 = df["Liquor type"].unique(), ["Select All"]
    new1.extend(sd1)
    f1 = st.multiselect("Liquor type", new1)
    if f1 == "Select All":
        selected_option = r1["Liquor type"].unique()
        r2 = r1[r1["Liquor type"].isin(selected_option)]
    else:
        r2 = r1[r1["Liquor type"].isin(f1)]
    # r2 = r1[r1["Liquor type"] == f1]
with coa3:
    sd2, new2 = df["Liquor sub type"].unique(), ["Select All"]
    new2.extend(sd2)
    f2 = st.multiselect("Liquor sub type", new2)
    if f2 == "Select All":
        selected_option3 = r2["Liquor sub type"].unique()
        r3 = r2[r2["Liquor sub type"].isin(selected_option3)]
    else:
        r3 = r2[r2["Liquor sub type"].isin(f2)]
with cla4:
    sd3, new3 = df["Packaging size"].unique(), ["Select All"]
    new3.extend(sd3)
    f3 = st.multiselect("Packaging size", new3)
    if f3 == "Select All":
        selc = r3["Packaging size"].unique()
        r4 = r3[r3["Packaging size"].isin(selc)]
    else:
        r4 = r3[r3["Packaging size"].isin(f3)]
with cla5:
    sd4, new4 = df["Packaging type"].unique(), ["Select All"]
    new4.extend(sd4)
    f4 = st.multiselect("Packaging type", new4)
    if f4 == "Select All":
        selc3 = r4["Packaging type"].unique()
        r5 = r4[r4["Packaging type"].isin(selc3)]
    else:
        r5 = r4[r4["Packaging type"].isin(f4)]

if len(r5)> 0:
    # dfs = df.drop(["Date", "Price(Rs)","Brand Name", "Liquor type", "Liquor sub type","Packaging size","Packaging type" ], axis=1)
    with st.container():
        gh = pd.read_csv("fi.csv")
        ghs = gh.drop(["Date","Brand Name","price"], axis=1)
        dfmm = st.selectbox("CHART BY", ghs.columns)
        fig = px.bar(gh, x="Date", y=dfmm, color="Date")
#
# # print(r5.to_datetime(df['Date']).dt.date)
# # with st.container():
# #     dfmm = st.selectbox("CHART BY", dfs.columns)
# # fig = px.bar(r5, x="Date", y=dfmm, color="Date", color_discrete_sequence=px.colors.cyclical.Twilight)
# # # # fig.show()
        fig.update_layout({
                            'plot_bgcolor': 'rgb(229,236,246)',
                            'paper_bgcolor': 'rgb(255,255,255)',
                            'height': 650,
                            'title_font_color': "black",
                            'title_font_size': 20,
                        })
        st.plotly_chart(fig, use_container_width=True)

        csv = r5.to_csv().encode('utf-8')

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv',
        )

