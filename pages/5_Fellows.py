import streamlit as st 
import time 
from streamlit_image_select import image_select

_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""
st.markdown("<h1 style='text-align: center; color: black;'>Ask previous fellows</h1>", unsafe_allow_html=True)

profiles = {"Sienka": ("Hi,", "Hi, I am Sienka, and I am passionate about STEM, with a recent interest in AI alignment."), "Tewodros":("Hi,","Hi, I am tewodros, software engineer upskilling to be an AI safety research engineer")}
Questions = ["What was your goal with the fellowship?", "Which part of upskilling did you focus on?"]


def answer_question():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)



col1, col2 = st.columns([1, 1])

with col1:
    img = image_select(
        label="Click a fellow to ask: ",
        images = ["./img/sienka.jpg", "./img/Tewodros.jpg"],
        captions = ["Sienka", "Tewodros"],
        use_container_width = False,        
    )
with col2:
    if img:
        if("sienka" in img):
            st.write(" ");st.write(" ")
            st.info("{}".format(profiles['Sienka'][1] ))
        else:
            st.write(" ");st.write(" ")
            st.info("{}".format(profiles['Tewodros'][1] ))
option = st.selectbox(
    label="Choose a question",
    placeholder="Placeholder",
    options= Questions,
)
    
if st.button("Ask"):
    st.write_stream(answer_question)
