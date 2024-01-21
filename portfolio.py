import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = "My Webpage", page_icon="🏗", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None  
    return r.json()


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ycXDlOyJWi.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Kerwin! :wave:")
    st.title("A Structural Engineer From Singapore")
    st.write("""I am passionionate about finding ways to use software to automate and be more efficient in AEC.""")
    st.write("[Learn More >](https://www.linkedin.com/in/kerwint/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Hi, I'm Kerwin. I have been studying and working in the built environment sector for the past 5 years, building experiences in technical designs of underground structures and building infrastructure, as well as automating structural analysis and Building Information Modelling Systems through plugin development for multiple software, aiding in the effort for the industry to adopt industry 4.0.

            I am a self-motivated and purpose driven person. I enjoy facing and overcoming challenges to develop myself in both technical and non-technical skills such as interpersonal communication. It is an exciting time for the world right now, with digitalization and innovation disrupting industries such as the built environment sector. Many changes have been going on since the pandemic but there have also been tons of opportunities for growth. 

            Upskilling myself with digital and tech skills such as software programming in various languages and techniques, I am looking for new opportunities in the area of software development, specifically in the built environment sector. 

            I'd like to eventually be involved in the technological side of things and be a part of digitalization as the construction industry continues to push for Industry 4.0."""
        )
    with right_column:
        st.write("##")
        st.write("##")
        st_lottie(lottie_coding, height = 400, key="coding")