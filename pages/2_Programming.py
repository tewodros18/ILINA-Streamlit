import streamlit as st 


selected = st.selectbox("", ["See Fellow's Note for this section", "Sienka", "Tewodros"])

if(selected == "Tewodros"):
    with st.expander("📝Notes"):
        st.write('')

st.markdown("<h3 style='text-align: left; color: black;'>Checklist</h3>", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.write("")
with col2:
    st.checkbox("PyTorch")
    st.checkbox("Einops and Einsum")
    st.checkbox("Transformers Library")