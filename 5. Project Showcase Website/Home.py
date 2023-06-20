import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=540)
    
with col2:
    st.title("Minh An Projects")
    content = """
    Greate to see you! My name is Andy and I am a data engineer, a trainer and a founder of Tech Coaching.
    Hope you could enjoy while reading this page.
    Cheer!
    """
    st.info(content)

    content_subtitle = """
                    Below you can find all apps I have built in Python. Feel free to share and contact me!
    """
    st.write(content_subtitle)


col3, empty_col, col4 = st.columns([1.7, 0.3, 1.7])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
    
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

