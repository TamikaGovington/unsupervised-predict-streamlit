import streamlit as st
from streamlit_player import st_player
import streamlit as st
import components.reviews as coms


def vids():
            st.write('Selct a year to display movies trailers from...')
            year = st.radio('Select release Year', [2018, 2019, 2020, 2021, 2022], index=0, format_func=lambda x: str(x), key=None)
        
        
            
    # display video
            if year == 2022:
                with st.expander('Top 10 Best Movies 2022'):
                    st_player('https://youtu.be/JAxj25X2EFA')
                    st.write('**Which movies did you like?**')
                    coms.commenter('Top 10 Best Movies 2022')
            if year >= 2021:
                with st.expander('Top 10 Best Movies 2021'):
                    # 2021
                    st.write('**Which movies did you like?**')
                    st_player('https://youtu.be/-KBBnTWp8h8')
                    coms.commenter('Top 10 Best Movies 2021')
            if year >= 2020:
                with st.expander('Top 10 Best Movies 2020'):
                    # 2020
                    st_player('https://youtu.be/WfI0nXedFzQ')
                    coms.commenter('Top 10 Best Movies 2020')
            if year >= 2019:
                with st.expander('Top 10 Best Movies 2019'):
                    # 2019
                    st_player('https://youtu.be/48NL3N6KMFo?t=9')
                    coms.commenter('Top 10 Best Movies 2019')
            if year >= 2018:
                with st.expander('Top 10 Best Movies 2018'):
                    # 2017
                    st_player('https://youtu.be/FkUtWUy77fQ?t=9')
                    coms.commenter('Top 10 Best Movies 2018')
