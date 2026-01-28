import streamlit as st

st.title("Week 8 - DAY 1: HeadStart with StreamLit")
st.write("Testing version of first Streamlit code")

name = st.text_input("Enter your name: ")
if name: 
    st.success(f"Hello, {name}!")