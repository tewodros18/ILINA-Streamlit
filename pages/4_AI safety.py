import streamlit as st 


col1, col2 = st.columns([1,1])

with col1:
    st.write("Interpretability")

with col2:
    st.checkbox("Mechanistic Interpretability")
    st.checkbox("Developmental Interpretability")
    st.checkbox("Sparse Auto-Encoders")
    st.checkbox("Evaluations and Red Teaming")
    st.checkbox("Hands-on Technical AI Safety")
