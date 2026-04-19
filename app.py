import streamlit as st

st.title("Diabetes Prediction App")
st.write("Welcome Bro 😎")

preg = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
bp = st.number_input("Blood Pressure")
age = st.number_input("Age")

if st.button("Predict"):
    st.success("Prediction Completed")
