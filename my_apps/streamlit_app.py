# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import time
from st_pages import Page, Section, show_pages, add_page_title

print('home page -------------------')
add_page_title()

show_pages(
    [
        Page("streamlit_app.py", "Validation", "🏠"),
        Section('Setting namelists', icon=":pig:"),
        Page("pages/geo_namelist.py", "Create geo validation namelist", "📝"),
        Page("pages/page_2.py", "Page 3", "☔"),
        Section('Section b', icon=":horse:"),
        Page("pages/page_3.py", "Page 3", "☔"),
        Page("pages/page_b.py", "Page bbbbb", "☔"),
        Page("pages/page_test.py", "Page test", ":pig:", in_section=False),
    ]
)

with st.sidebar:
    st.write("This code will be printed to the sidebar.")
    with st.spinner("Loading..."):
        time.sleep(5)
    st.sidebar.success("Done!")

st.write('Introduction For this app')

with st.expander("Show documentation"):
    from st_pages import add_indentation

    st.help(show_pages)

    st.help(Page)

    st.help(add_page_title)

    st.help(Section)

    st.help(add_indentation)
