import numpy as np 
import pandas as pd 
import streamlit as st




#Streamlit UI
st.title(" Music Recommendation System")
name = st.text_input("Enter a name")

if st.button("Recommend Songs"):
    if name:
        songs = get_recommendations(name)
        st.subheader(f"Recommended Songs for {name}")

        for song in songs:
            st.write(f"{song}")

    else:
        st.warning("Please enter a name")

if st.checkbox("Show average Ratings"):
    ratings = get_average_ratings()
    st.bar_chart(ratings)

