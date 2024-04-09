#page info will come here
import streamlit as st

def helppage():
    #Create the title and intro
    st.title("Need assistance?")
    st.write("Welcome, Not sure what to do or where to be? We have the support you need.")
    
    with st.expander("Home"):
            
    
    #Create the info section for home page. 
        st.title("Home")
    
            
    
    #create the Step by step guide for the Home page.
        st.title("Steps")
        st.write("- Choose Between Content based or Collaborative based filtering.")
        
        st.info(
            """
        - Content based is where we see what a user may like based on keywords/movies.
        
        - Collaborative based filtering is where we see what a user may like based on other users likes.
        
        """
        )
        
        st.write(
            """
        - Select 1st, 2nd & 3rd favourite movie.
        - Press the Recommend button.
        - Enjoy the selection of recommended movie and their trailers.
        """
                )
    
    #create the About help section.
    with st.expander("About"):
        st.title("About")

    
    #create the Step by step guide for the About Page.
        st.title("Steps")
        st.write(
            """
        - Find out about the RecoExperTechnologies.
        
        """
        )
    
    #create help section for trailers page.    
    with st.expander("Movie Trailers"):
        st.title("Trailers")
        

    #create the Step by step guide for the Trailers Page.
        st.title("Steps")
        st.write(
            """ 
            -  Choose the radio button to select years.
            -  Choose which years drop down to select and click it.
            -  Play the vid.
            -  Feel free to read the comments or leave a comment.
            -  To leave comment type name in the name box.
            -  Leave your comment in comment section.
            -  Press the send button to comment.
            """
                )
        
    #create the About help section.
    with st.expander("Movie insights"):
        st.title("Movie insights")

    #create the Step by step guide for the About Page.
        st.title("Steps")
        st.write(
            """
            - Click the drop down.
            - Select your options.
            - After selecting your 2nd metric your chart or plot should pop up.
            - To select a different chart clear one of the other metrics.
            - Feel free to check out the valuable data insights we have for the movie industry.
            """
                )
        
    #create the Contact Us help section.
    with st.expander("Contact Us"):
        st.title("Contact Us")
    
    #create the Step by step guide for the Contact Us Page.
        st.title("Steps")
        st.write(
            """
            As you can see Contact Us is pretty simple, but should you require any assistance feel free to reach out.
            
            - Add your name.
            - Add your email.
            - Leave your message.
            - Press the send message button.
        
            """
                )
    
        
    
    
