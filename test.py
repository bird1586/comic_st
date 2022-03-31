from bokeh.models.widgets import Div
import streamlit as st

if st.button('Go to Streamlit'):
    js = "window.open('https://www.streamlit.io/')"  # New tab or window
    js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
