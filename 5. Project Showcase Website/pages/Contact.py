import streamlit as st

st.header("Contact us")

with st.form(key="form_1"):
    user_email = st.text_input("Your email address: ")
    message = st.text_area("Your message")
    button = st.form_submit_button()
    if button:
        message = message + user_email
        