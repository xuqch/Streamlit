# Contents of ~/my_app/pages/page_3.py
import streamlit as st
from st_pages import add_page_title, hide_pages

print('3 -------------------')
add_page_title()

title = st.text_input('Your data path is: ', '/home/')
st.write('The current path is', title)

number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write('The current number is ', number)
print(number)

# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False,
#     text_input = st.text_input(
#         "Enter some text 👇",
#     )
#
# if text_input:
#     st.write("You input path is:  ", text_input)
