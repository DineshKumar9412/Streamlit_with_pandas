# # # Display Map in geopanda
# # import pandas as pd
# # import plotly.express as px
# # import geopandas as gpd
# #
#
# #
# #
# # px.set_mapbox_access_token("Your mapbox API Token")
# # fig = px.scatter_mapbox(data, lat="latitude", lon="longitude",color="room_type", size="price",
# #                   color_continuous_scale=px.colors.cyclical.IceFire, size_max=20,zoom=12)
# # fig.show()
#
#
#
# # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')
#
# # df.info()
#
# # fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
# #                         center=dict(lat=0, lon=180), zoom=0,
# #                         mapbox_style="stamen-terrain")
# # fig.show()
#
#
#
# # #
# # tngdf = gpd.read_file('tamilnadu.geojson')
# # # tngdf.plot(figsize=(50, 10))
# # limsdf = pd.read_csv('lims_gis.csv')
# # newdf = limsdf.groupby(['gid', 'District Name']).sum().reset_index()
# #
# # fig = px.choropleth(newdf, geojson=tngdf, locations="gid", hover_name="District Name")
# #
# # fig.update_geos(fitbounds="locations", visible=False, showsubunits=True, subunitcolor="Red")
# # # fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0},
# # # #                   coloraxis_colorbar={'title':'Intefaced Percentage'})
# # # fig.update_layout(height=700, margin={"r": 0, "t": 0, "l": 0, "b": 0})
# # #
# # # # fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
# # #
# # # fig.show()
# #
# #
# #
# import pandas as pd
# import plotly.express as px
# import geopandas as gpd
#
# dfs = pd.read_csv("tets.csv")
# # print(df)
#
# df = dfs[["gid", "District Name", "Interface SAA"]]
#
# mapes = gpd.read_file('new_tamilnadu.geojson')
#
# print(mapes["district"])
# # fig = px.choropleth(df, locations="gid",color="Interface SAA",hover_name="District Name",geojson=mapes)
# # fig.show()
#
# # fig = px.density_mapbox(df, lat='lat', lon='log', z='sales', radius=10,
# #                         center=dict(lat=0, lon=180), zoom=0,
# #                         mapbox_style="stamen-terrain")
# # fig.show()
#
# # print(df.head().to_string())
# # print(geojson["features"][0]["properties"])
# # fig = px.choropleth(df, geojson=geojson, color="Bergeron",
# #                     locations="district", featureidkey="properties.district",
# #                     projection="mercator"
# #                    )
# # fig.update_geos(fitbounds="locations", visible=False)
# # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# # fig.show()









# import json
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import geopandas as gpd
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
#
# dfd = pd.read_csv("sts.csv")
# df = dfd[["state","den"]]
#
# # mapes = gpd.read_file('states_india.geojson')
# counties = json.load('states_india.geojson')
# print(counties)
#

# print(df.head().to_string())

# fig = px.choropleth(
#     df,
#     geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
#     featureidkey='properties.ST_NM',
#     locations='state',
#     color='den',
#     color_continuous_scale='Reds'
# )
#
# fig.update_geos(fitbounds="locations", visible=False)
# fig.show()
# print("ehdgh")
# fig = px.choropleth(
#     df,
#     geojson=mapes,
#     featureidkey='st_nm',
#     locations='state',
#     color='den',
#     color_continuous_scale='Reds'
# )
#
# fig.update_geos(fitbounds="locations", visible=False)
# fig.show()

# df["id"] = df["State or union territory"].apply(lambda x: state_id_map[x])
# tngdf = gpd.read_file('tamilnadu.geojson')
# dff =

# state_id_map = {}
# for feature in india_states["features"]:
#     feature["id"] = feature["properties"]["state_code"]
#     state_id_map[feature["properties"]["st_nm"]] = feature["id"]


# import json
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import geopandas as gpd
#
# # mapes = gpd.read_file('india.geojson', 'r')
#
# india_states = json.load(open("india.geojson", "r"))

# print(mapes)






# #  1 BOTH CSV AND GEOJSON FILE https://
import json
import pandas as pd
import streamlit as st
import plotly.express as px
import geopandas as gpd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='active cases',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)
fig.show()


# 2 CVS IN LOCAL AND GEOJSON ON ONLINE
# import json
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import geopandas as gpd
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# df = pd.read_csv("my.csv")
#
# fig = px.choropleth(
#     df,
#     geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
#     featureidkey='properties.ST_NM',
#     locations='state',
#     color='active cases',
#     color_continuous_scale='Reds'
# )
#
# fig.update_geos(fitbounds="locations", visible=False)
# fig.show()

# 3
# import json
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import geopandas as gpd
