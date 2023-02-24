import streamlit as st

st.write("""
# My first app
Hello *world!*
""")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)