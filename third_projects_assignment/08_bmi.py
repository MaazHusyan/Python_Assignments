import streamlit as st

st.title("BMI (Body Mass Index) Calculator")

height = st.slider("Enter your Height (in cm): ", 100, 180, 140)
weight = st.slider("Enter your Weight (in kg): ", 35, 150, 55)

bmi = weight / ((height / 100) ** 2)

st.markdown(f"### Your BMI is: {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("- Over-weight: over 25 ")
st.write("- Normal-weight: between 18.5 and 24.9 ")
st.write("- Under-weight: less than 18.4 ")