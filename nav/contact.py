# streamlit dependencies
import streamlit as st
# data dependencies
import pandas as pd
import numpy as np
import base64
from PIL import Image

def data_professionals():
    st.info("""
		
		Our team consists of 6 talented data scientists, DevOps Engineers and Software developers based in South Africa. We are passionate about data science and machine learning and we are always looking for new opportunities to learn and grow.
        You can reach out using the contacts provided bellow: """)


        # create divs to display team members in two rows
    col1, col2, col3 = st.columns(3)
    with col1:
            st.image("resources/imgs/makhambi.png", width=100)
            st.write("Makhambi Maliviwe- Data Scientist")
            st.write('Email : makhambi80@gmail.com')
            st.write('Github: https://github.com/Makhambi')   
    with col2: 
            st.image("resources/imgs/tami.png", width=100)
            st.write("Tamika Govington - Data Analyst")
            st.write('Email: tamika1786@gmail.com' )
            st.write('Github: https://github.com/TamikaGovington')
    with col3:
            st.image("resources/imgs/phemba.png", width=100) 
            st.write("Phemba Mabatha - DevOps Engineer")
            st.write('Email : phemabam@gmail.com')
            st.write('Github: https://github.com/phemabam')
    col4, col5, col6 = st.columns(3)
    with col4:
            st.image("resources/imgs/nolwa.png", width=100)
            st.write("Nolwazi - Data Analyst")
            st.write('Email: nolwazi@gmail.com' )
            st.write('Github: https://github.comNolwazi')
    with col5:
            st.image("resources/imgs/hlaka.png", width=100)
            st.write("Hlakamiphile Zwane - Data Scientist") 
            st.write('Email: hlakaniphile171123@gmail.com' )
            st.write('Github: https://github.com/Hlakaniphile171123')
    with col6:
            st.image("resources/imgs/londy.png", width=100)
            st.write("Londeka - Software Developer")
            st.write('Email: lolomagyt@gmail.com' )
            st.write('Github: https://github.com/Londeka')
            
    
    contact_form = """
    <form action="https://formsubmit.co/makhambi80@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send mail</button>
    </form>
    """
    
    
    
    team, members, contact, = st.columns([2, 1.5, 1.5])

    with contact:
        st.header("Contact us")
        st.markdown(contact_form, unsafe_allow_html=True)
        local_css("./utils/style.css")
    with team:
        st.write("")
    
    with members:
        st.markdown(f'',unsafe_allow_html=True)
        
    st.write("")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style >{f.read()}</style>", unsafe_allow_html=True)