import streamlit as st
import pandas as pd

st.header("Basic Statistical Relation")



import random
from streamlit_d3_demo import d3_line
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("sc_data")
x_q = df['Unit quantity']
y_w = df["Weight"]
# def generate_random_data(x_r, y_r):
#     return list(zip(range(x_r), [random.randint(0, y_r) for _ in range(x_r)]))

plot = plotly.tools.make_subplots(rows=1, cols=3)
plot.add_trace(go.Scatter(x = x_q,y = y_w, name = "quantity - weight"), row = 1, col = 1)
df2 = df.groupby('Product ID')['Unit quantity'].sum()
df2 = pd.DataFrame(df2).reset_index()
x2 = df2["Product ID"]
y2 = df2["Unit quantity"]

plot.add_trace(go.Scatter(x = x2, y = y2, name = 'ID - quantity'), row = 1, col = 2)


df3 = df.groupby('Product ID')['Ship ahead day count'].sum()
df3 = pd.DataFrame(df3).reset_index()
x3 = df3["Product ID"]
y3 = df3["Ship ahead day count"]
plot.add_trace(go.Scatter(x = x3, y = y3, name = "ID - Ship count"), row = 1, col = 3)


layout = go.Layout(
    autosize=False,
    width=1000,
    height=1000,
    margin=go.layout.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad = 4
    )
)


st.plotly_chart(plot, use_container_width=True, layout = layout)

# plot1 = px.scatter(data_frame = df
#            ,x = 'Unit quantity'
#            ,y = 'Weight'
#            ,color_discrete_sequence = ['red']
#            )
# st.plotly_chart(plot1, use_container_width=True)

# st.caption('Distribution of the product unit quantity and weight')
# df2 = df.groupby('Product ID')['Unit quantity'].sum()
# df2 = pd.DataFrame(df2).reset_index()
# plot2 = px.bar(df2, 'Product ID' ,'Unit quantity')
# st.plotly_chart(plot2, use_container_width=True)
