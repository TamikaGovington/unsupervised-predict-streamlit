"""
    Streamlit webserver-based Recommender Engine.
    Author: Explore Data Science Academy.
    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.
    NB: !! Do not remove/modify the code delimited by dashes !!
    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------
    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.
	For further help with the Streamlit framework, see:
	https://docs.streamlit.io/en/latest/
"""
# Streamlit dependencies
import streamlit as st
import hydralit_components as hc

# Data handling dependencies
import pandas as pd
import numpy as np


# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
import components.youtube_data as top_trailers
import nav.trailers as t
# import menu.data_professionals as dreamers
import nav.contact as contact
import nav.statistics as stat
import nav.helper as h
import nav.About as a
import time

# Data Loading
title_list = load_movie_titles('https://raw.githubusercontent.com/Makhambi/movies-data/main/movies.csv')

#Logo
st.set_page_config(page_icon='resources/imgs/RecoXperTechnologies_Logo.png', page_title= 'RecoXperTechnologies', layout='wide', initial_sidebar_state='auto')

over_theme = {'txc_inactive': '#FFFFFF'}

# specify the primary menu definition
menu_data = [
    
    {'id':'Trailers','icon':'fas fa-film','label':'Movie Trailers'},
    {'icon': 'fas fa-chart-pie', 'label':'Movie insights'},
    {'icon': "far fa-copy", 'label':'About'},
    {'icon': 'far fa-chart-bar', 'label':'EDA'},
    {'id':'Contact Us', 'icon': 'fas fa-users', 'label':'Contact Us'},
    {'id':'Info', 'icon': 'fas fa-info-circle', 'label':'Info'}
   
]

# App declaration

def main():
    # Nav bar
    menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    
    home_name='Home',
    hide_streamlit_markers=False, 
    sticky_mode='pinned', 
)
    page_selection = f'{menu_id}'
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    

    if page_selection == 'Home':

        st.image('resources/imgs/logo.jpg',width=100)
        # Header contents
        st.write('# Movie Match')

        st.image('resources/imgs/Untitled.png',use_column_width=True)

        st.write('Choose Between Content based or Collaborative based filtering...')
        st.write(
            """
        - Select 1st, 2nd & 3rd favourite movie.
        - Press the Recommend button.
        - Enjoy the selection of recommended movies and their trailers.
        """
                )
        # Recommender System algorithm selection
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: right;} </style>', unsafe_allow_html=True)
        st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-right:2px;}</style>', unsafe_allow_html=True)
        sys = st.radio("", ('Content Based Filtering', 'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Select Your Three Favorite Movies')
        movie_1 = st.selectbox('1ˢᵗ Movie',title_list[14930:15200])
        movie_2 = st.selectbox('2ⁿᵈ Movie',title_list[25055:25255])
        movie_3 = st.selectbox('3ʳᵈ Movie',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
   
        st.write('### Recommendations')
        if sys == 'Content Based Filtering':
            if st.button('Recommend'):
                try:
                    # intialize hydralit loaders
                    with hc.HyLoader('Hold on tight... your movies are coming up...\n',hc.Loaders.standard_loaders,index=[5,0,3]):
                        # get top 10 recommended movies using the content_model algorithm
                        top_recommendations = content_model(movie_list=fav_movies, top_n=10)
                        time.sleep(5)
                    st.title('Here\'s a list of movies you might like...')
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                        # get trailer from youtube
                        top_trailers.youtubeScrapper(top_recommendations[i])
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

        if sys == 'Collaborative Based Filtering':
            if st.button('Recommend'):
                try:
                    # intialize hydralit loaders
                    with hc.HyLoader('Hold on tight... your movies are coming up...\n',hc.Loaders.standard_loaders,index=[5,0,3]):
                        # get top 10 recommended movies using the collab_model algorithm
                        top_recommendations = collab_model(movie_list=fav_movies, top_n=10)
                        time.sleep(5)
                    st.title('Here\'s a list of movies you might like...')
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                        # get trailer from youtube
                        top_trailers.youtubeScrapper(top_recommendations[i])
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------------
    elif page_selection == 'About':
        # navigate to the About page
        a.about()
    elif page_selection == 'Trailers':
        # navigate to the Trailers page
        t.vids()
    elif page_selection == 'Contact Us':
        # navigate to the Contact Us page
        contact.data_professionals()
    elif page_selection == 'Movie insights':
        # navigate to the Statistics page
        stat.visuals()
    elif page_selection == 'Info':
        # navigate to the Help page
        h.helppage()
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    if page_selection == "EDA":
        st.title("EDA")
        st.write("Exploratory Data Analysis")
        st.info("This will be an exploration and explanation of the dataset used and insights derived respectively")
        st.subheader(' Density plot and the Average rating of users')
        st.image('resources/imgs/output.png',use_column_width=True)
        st.markdown('The density plots explain the general trend of the users. Two features that were observed displayed that most users(80%) give an average rating of 3.5 for a movie that the user has watched.')
        
        st.subheader(' Correlation between average rating and the number of the times have the user has watch a movie')
        st.image('resources/imgs/output.png',use_column_width=True)
        st.markdown('The relationship between average rating and number of movies is observed from above linear dependent. When the user has watched more movies tend give a higher rating.')
        
        st.subheader(' A box plot showing average number of movies watch per member')
        st.image('resources/imgs/output3.png',use_column_width=True)
        st.markdown(" The above plots shows that mosts users have watched less than 500 movies and most users gave average rating of 3.5 for all the movies they have watched. ")
        
        st.subheader(' The number of movies for each ratings')
        st.image('resources/imgs/output4.png',use_column_width=True)
        st.markdown("From the countplot movies in the dataset where rated 3.0 or above where most were rated given the rating of 4.0. Most of the movies in the data were very good considering the amount of movies that were rated 4.0 or above. With further scrutiny of the data, the observations acquired from the above chart will be explained in the next incoming sections. ")
        
        st.subheader(' The top 10 best rated movies')
        st.image('resources/imgs/output6.png',use_column_width=True)
        st.markdown('The best rated movies have generally an average rating of 5.0 with the best movie as *Exorcist* and above whereas the worst rated movies generally have lower rating of 2.5 and below with the worst movie being Singin in the rain. ')
        
        st.subheader(' Top Genres')
        st.image('resources/imgs/output7.png',use_column_width=True)
        st.markdown('Drama and Comedy are the most popular genres, followed by Thriller and Romance. We noted that movies could have multiple genres.')

if __name__ == '__main__':
    main()
