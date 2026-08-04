import numpy as np 
import pandas as pd 
import streamlit as st




#Streamlit UI

st.set_page_config(
    page_title="Music Recommendation System",
    page_icon="🎵",
    layout="centered"
)

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

/* Title */
h1{
    color:white;
    animation: fadeIn 1s ease-in-out;
}

/* Subtitle */
.stCaption{
    color:#EAEAEA;
}

/* Glass Effect Containers */
[data-testid="stVerticalBlockBorderWrapper"]{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius:18px;
    border:1px solid rgba(255,255,255,0.15);
}

/* Buttons */
.stButton>button{
    background:#1DB954;
    color:white;
    border:none;
    border-radius:12px;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    background:#1ed760;
    transform:scale(1.05);
}

/* Recommendation Cards */
.song-card{
    background:#1E1E1E;
    padding:15px;
    border-radius:15px;
    margin-bottom:15px;
    animation:fadeIn 0.6s;
    transition:0.3s;
}

.song-card:hover{
    transform:translateY(-4px);
    box-shadow:0 8px 20px rgba(0,0,0,.4);
}

/* Fade Animation */
@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(15px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center'>🎵 Music Recommendation System</h1>
<p style='text-align:center;
font-size:18px;
color:#EAEAEA'>
Discover songs you'll love based on users with similar tastes.
</p>
""", unsafe_allow_html=True)

st.divider()

with st.container(border=True):

    st.subheader("Get Recommendation")

    col1,col2 = st.columns([4,1])

    with col1:
        name = st.text_input("Enter a name",label_visibility="collapsed")

    with col2:
        recommend = st.button("Recommend Song(s)", use_container_width=True)

if recommend:
    if name:
        with st.spinner("Getting you a song..."):
            songs = get_recommendations(name)

        st.success(f"Found {len(songs)} recommendation(s) for {name}")

        st.subheader(f"Recommended Songs for {name}")

        for i,song in enumerate(songs,start=1):
            with st.container(border=True):

                col1,col2 = st.columns([1,4])

                with col1:
                    st.image("https://img.icons8.com/fluency/96/music.png",width=70)

                with col2:
                    st.markdown(f"""
                        <div class="song-card">
                            <h4>🎵 {song}</h4>
                            <p style="color:#B3B3B3;">Recommended Song #{i}</p>
                        </div>
                        """, unsafe_allow_html=True)

    else:
        st.warning("Please enter a name")


#Ratings chart
def get_average_ratings():

    df = pd.read_csv("user_song_ratings.csv")

    ratings = df.drop(columns=["User"])

    # Treat 0 as "not rated"
    ratings = ratings.replace(0, pd.NA)

    average_ratings = ratings.mean().sort_values(ascending=False)

    return average_ratings

st.divider()
with st.expander("Average Song Ratings"):
    ratings = get_average_ratings()
    st.bar_chart(ratings)  

