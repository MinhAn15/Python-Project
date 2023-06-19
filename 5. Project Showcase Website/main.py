import streamlit as st


st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=500)
    
with col2:
    st.title("Minh An Projects")
    content = """
    Greate to see you! My name is Andy and I am a data engineer, a trainer and a founder of Tech Coaching.
    Hope you could enjoy while reading this page.
    Cheer!
    """
    st.info(content)
    

