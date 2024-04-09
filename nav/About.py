import streamlit as st

def about():
    #about page title
    st.title("RecoXpertechnologies")

    about_RecoX, movieMatch_logo, = st.columns([2, 3])
    
    with about_RecoX:

        st.write("As RecoXpert we specialise in predictive analytics with a focus on recommender systems."+ 
            "We believe in the power of data-driven decision-making to transform businesses and enhance user experiences."+
            "With cutting-edge technology and a team of dedicated experts,"+
            "we enable our clients to fully utilise the power of their data to enhance operations, stimulate growth,"+
            "and provide customers with tailored advice")
    
    st.markdown("")
    with movieMatch_logo:
        st.image('resources/imgs/RecoXperTechnologies_Logo.png', caption="© RecoXperTechnologies. PTY. Ltd.")