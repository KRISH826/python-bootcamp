import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name = st.text_input("Enter your name")
description = st.text_area("Enter a description")
age = st.slider("Select your age", 0, 100, 25)
gender_options = ["Male", "Female", "Other"]
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
button = st.button("Submit")

if name:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old.")


uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)




