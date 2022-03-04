# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:25:29 2022

@author: bird1586
"""

from requests_html import HTMLSession
import re
import streamlit as st

@st.cache
def get_chapters(comic):
    r = session.get(rf'https://www.omyschool.com/article_list/{comics[comic]}/{comic}/')
    chapters = r.html.find('div.chapter a')
    chapters = chapters[:-24]
    chapters = {re.findall('\d+', c.attrs['href'])[-1]:c.attrs['href'] for c in chapters}
    return chapters

@st.cache
def get_pages(chapter):
    r = session.get(r'https://www.omyschool.com' + chapters[chapter])
    links = r.html.find("amp-img[width='580']")
    links = [i.attrs['src'] for i in links]
    return links
    

st.set_page_config(layout="wide") 
    
session = HTMLSession()
comics= {'海賊王':1, '一拳超人':51, '王者天下':104, '新網球王子':32, '名偵探柯南':47}
comic = st.selectbox('請選擇漫畫', comics)
chapters = get_chapters(comic)

chapter  = st.selectbox('請選擇章節', chapters)

if chapter:
    links = get_pages(chapter)
    for link in links:
        st.image(link if link.startswith('http') else r'https://' + link.lstrip('/'))

        
col1, col2 = st.columns(2)
with col1:
    if st.button('上一章'):
        pass
with col2:
    if st.button('下一章'):
        pass
        
       
st.markdown('''
                <style>
                div[data-testid="stToolbar"] {visibility: hidden;}
                </style>
                ''', unsafe_allow_html=True)        
