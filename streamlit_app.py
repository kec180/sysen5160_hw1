import streamlit as st
import pandas as pd

st.title("Keshan Chen's HW1")
st.subheader('This is the first homework of SYSEN5160, trying to learn how to create streamlit related file')
st.subheader('D3 random dot plot')

import random
from streamlit_d3_demo import d3_line

def generate_random_data(x_r, y_r):
    return list(zip(range(x_r), [random.randint(0, y_r) for _ in range(x_r)]))

d3_line(generate_random_data(20, 500), circle_radius=15, circle_color="#6495ed")