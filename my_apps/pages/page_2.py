# Contents of ~/my_app/pages/page_2.py
import streamlit as st
from st_pages import add_page_title, hide_pages
import time
import subprocess

print('2 -------------------')

add_page_title()

title = st.text_input('Your data path is: ', '/home/')
st.write('The current path is', title)

col1, col2, col3 = st.columns(3)
with col1:
    st.write('A testing')
    options = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        index=None,
        placeholder="Select contact method..."
    )
    st.write('You selected:', options)

    agree = st.checkbox('I agree')
    a_values = 'False'
    if agree:
        a_values = 'True'
        st.write('Great!')

    on = st.toggle('Activate feature')
    if on:
        st.write('Feature activated!')

print(a_values)


with col2:
    st.write("B testing")
    lat = st.number_input("Latitude", min_value=-90, max_value=90, value=None, placeholder="Latitude...")
    # st.write('Latitude is ', number)
    lon = st.number_input("Logitude", min_value=-180, max_value=180, value=None, placeholder="Logitude...")

with col3:
    st.write("C testing")

    genre = st.radio(
        "What's your favorite movie genre",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        captions=["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

    if genre == ':rainbow[Comedy]':
        st.write('You selected comedy.')
    else:
        st.write("You didn\'t select comedy.")


if st.button('Run', type="primary"):
    with st.spinner("Now ploting..."):
        subprocess.run('echo "success"', shell=True)
        time.sleep(3)
    st.success("Done!")
