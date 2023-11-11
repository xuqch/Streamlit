# Contents of ~/my_app/pages/page_test.py
import streamlit as st
from st_pages import add_page_title, hide_pages
import numpy as np
import pandas as pd
import time

print('b -------------------')

add_page_title()

title = st.text_input('Your data path is: ', '/home/')
st.write('The current path is', title)

data = np.random.randn(100, 1)
tab1, tab2, tab3, tab4 = st.tabs(["📈 Chart", "🗃 Data", "📝 Scatter", "📗 data"])

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["x", "y", "c"])
tab3.subheader("A Scatter with the data")
tab3.scatter_chart(chart_data,
                   x='x',
                   y='y',
                   size='c', )

tab4.subheader("A tab with the data")
tab4.write(chart_data)
