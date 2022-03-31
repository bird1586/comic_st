import streamlit as st
import webbrowser



a = st.button('google')
if a:
    webbrowser.open(r'http://www.google.com')
