# import pandas as pd
# import streamlit as st
# from st_aggrid import AgGrid
# from st_aggrid.grid_options_builder import GridOptionsBuilder
# from st_aggrid.shared import GridUpdateMode
# import plotly.express as px
#
#
# st.set_page_config(page_title="Netflix Shows", layout="wide")
# st.title("Netlix shows analysis")
#
# shows = pd.read_csv("netflix_titles.csv")
#
# gb = GridOptionsBuilder.from_dataframe(shows)
# gb.configure_pagination()
# gb.configure_selection(selection_mode="multiple", use_checkbox=True)
#
# gridOptions = gb.build()
# data = AgGrid(shows,
#               gridOptions=gridOptions,
#               enable_enterprise_modules=True,
#               allow_unsafe_jscode=True,
#               update_mode=GridUpdateMode.SELECTION_CHANGED)
#
# selected_rows = data["selected_rows"]
# selected_rows = pd.DataFrame(selected_rows)
#
#
# print(selected_rows)
#
# # if len(selected_rows) != 0:
# #     fig = px.bar(selected_rows, "rating", color="type")
# #     st.plotly_chart(fig)

import streamlit as st

st.markdown(
"""
<link rel="stylesheet" href="https://mleibman.github.io/SlickGrid/slick.grid.css" type="text/css"/>
<link rel="stylesheet" href="https://mleibman.github.io/SlickGrid/css/smoothness/jquery-ui-1.8.16.custom.css" type="text/css"/>
<link rel="stylesheet" href="https://mleibman.github.io/SlickGrid/examples/examples.css" type="text/css"/>
<table width="100%">
  <tr>
    <td valign="top" width="60%">
      <div id="myGrid" style="width:1000px;height:700px;"></div>
    </td>
    <td valign="top">
      <h2>Demonstrates:</h2>
      <ul>
        <li>basic grid with minimal configuration</li>
      </ul>
        <h2>View Source:</h2>
        <ul>
            <li><A href="https://github.com/mleibman/SlickGrid/blob/gh-pages/examples/example1-simple.html" target="_sourcewindow"> View the source for this example on Github</a></li>
        </ul>
    </td>
  </tr>
</table>
<script src="https://mleibman.github.io/SlickGrid/lib/jquery-1.7.min.js"></script>
<script src="https://mleibman.github.io/SlickGrid/lib/jquery.event.drag-2.2.js"></script>
<script src="https://mleibman.github.io/SlickGrid/slick.core.js"></script>
<script src="https://mleibman.github.io/SlickGrid/slick.grid.js"></script>
<script>
  var grid;
  var columns = [
    {id: "title", name: "Title", field: "title"},
    {id: "duration", name: "Duration", field: "duration"},
    {id: "%", name: "% Complete", field: "percentComplete"},
    {id: "start", name: "Start", field: "start"},
    {id: "finish", name: "Finish", field: "finish"},
    {id: "effort-driven", name: "Effort Driven", field: "effortDriven"}
  ];
  var options = {
    enableCellNavigation: true,
    enableColumnReorder: false
  };
  $(function () {
    var data = [];
    for (var i = 0; i < 500; i++) {
      data[i] = {
        title: "Task " + i,
        duration: "5 days",
        percentComplete: Math.round(Math.random() * 100),
        start: "01/01/2009",
        finish: "01/05/2009",
        effortDriven: (i % 5 == 0)
      };
    }
    grid = new Slick.Grid("#myGrid", data, columns, options);
  })
</script>
""", unsafe_allow_html=True)
