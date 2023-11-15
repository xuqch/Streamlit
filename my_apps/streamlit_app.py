# Contents of ~/my_app/streamlit_app.py
# from geo_classification import initial_setting
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
        time.sleep(1)
    st.sidebar.success("Done!")

st.header('Introduction For this app')

st.write('Introduction for connect host')
code = """
In loaclhost
$ ssh-keygen -t rsa
$ ssh-copy-id -i ~/.ssh/id_rsa.pub username@172.16.102.36
$ cd ~/.ssh
$ touch config

Place the following text in the config file:
"
Host land
    Hostname 172.16.102.36
    User xuqch3
    IdentityFile C:/Users/Administrator/.ssh/id_rsa
    ForwardX11 yes
Host tms01
    Hostname 192.168.6.101
    User xuqch3
    IdentityFile ~/.ssh/id_rsa
    ForwardX11 yes
    ProxyJump land
"
If you are using the macos system, 
Replace "C:/Users/Administrator/.ssh/id_Rsa" with "~/.ssh/id_Rsa"
"""
with st.expander("Show method"):
    st.code(code, language='shell')

st.write('Introduction For this app')

with st.expander("Show documentation"):
    from st_pages import add_indentation

    st.help(show_pages)

    st.help(Page)

    st.help(add_page_title)

    st.help(Section)

    st.help(add_indentation)
