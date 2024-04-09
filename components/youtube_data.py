import urllib.request
import requests
import unicodedata
import re
from streamlit_player import st_player
import streamlit as st


def youtubeScrapper(top_10):
    search_string = unicodedata.normalize('NFKD', top_10).encode('ascii', 'ignore').decode()
    youtube_str = re.sub("[ ]", "+", search_string)
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + youtube_str + '+trailer')
    vid_id = re.findall(r'watch\?v=(\S{11})', html.read().decode())
    if len(vid_id) == 0:
        st.write("No video found")
    
    trailer_res = 'https://www.youtube.com/watch?v=' + vid_id[0]
    st_player(trailer_res)