# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:25:29 2022

@author: bird1586
"""

from requests_html import HTMLSession
import re
import streamlit as st

session = HTMLSession()

comics= {'海賊王':1, '一拳超人':51, '王者天下':104, '新網球王子':32, '名偵探柯南':47}
comic = st.selectbox('請選擇漫畫', comics)
r = session.get(rf'https://www.omyschool.com/article_list/{comics[comic]}/{comic}/')
chapters = r.html.find('div.chapter a')
chapters = chapters[:-24]
chapters = {re.findall('\d+', c.attrs['href'])[-1]:c.attrs['href'] for c in chapters}

option  = st.selectbox('請選擇章節', chapters)

if option:
    r = session.get(r'https://www.omyschool.com' + chapters[option])
    links = r.html.find("amp-img[width='580']")
    links = [i.attrs['src'] for i in links]
    
    for link in links:
        st.image(link)
        
st.markdown('''
                <style>
                div[data-testid="stToolbar"] {visibility: hidden;}
                </style>
                ''', unsafe_allow_html=True)        
