# Contents of ~/my_app/pages/page_test.py
import streamlit as st
from st_pages import add_page_title, hide_pages

print('test -------------------')

add_page_title()


title = st.text_input('Your data path is: ', '/home/')
st.write('The current path is', title)

options2 = st.multiselect(
    "What are your favorite colors",
    ['Green', 'Yellow', 'Red', 'Blue'],
    default=['Yellow', 'Red'],
    placeholder="Select contact method...",
)
st.write('You selected:', options2)
print(options2)
