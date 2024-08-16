import streamlit as st 
import time 

#st.title('ILINA 2024 Road Map')
#st.markdown("<h1 style='text-align: center; color: black;'>ILINA 2024 Road Map</h1>", unsafe_allow_html=True)
st.image("./img/ILINA.png")

with st.sidebar:
    st.success("Done!")

st.title("Goals")

st.subheader("Theoretical AI Alignment Understanding", divider="grey",)

st.success('''
This includes covering major research topics on Alignment, Building a mathematical context for understanding ML papers, and exploring philosophical questions that are related to Alignment. 

Simple Measurement after the study 
- Can you write up your thoughts on AI and the future in a nuanced, well-thought-out manner?

''', icon="🟢")

st.subheader("AI safety research engineering proficiency", divider="grey")


st.success('''
This includes increasing proficiency in my Python skills for ML development, having hands-on experience with ML libraries and frameworks, understanding technical papers, and replicating them.

Simple Measurement after the study 
- With a few weeks' work, could you - hypothetically! - write a new feature or fix a bug in a major ML library?

''', icon="🟢")

st.subheader("Fellowship & Seminar", divider="grey")

st.success('''
Acquire new ways of thinking and broaden perspective on topics that might have previously been neglected. Pursue readings outside of technical work from the seminar reading materials.

''', icon="🟢")




