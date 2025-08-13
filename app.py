import streamlit as st
import joblib
import numpy as np

# Load your trained model
model_diabetes = joblib.load("diabetes.joblib")  # replace with your filename

# Title
st.title("Diabetes Prediction App")

# User input fields
preg = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glu = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
dias = st.number_input("Diastolic Blood Pressure", min_value=0, max_value=150, value=70)
tri = st.number_input("Triceps Skinfold Thickness", min_value=0, max_value=100, value=20)
ins = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
ped = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=0, max_value=120, value=30)

# Prediction button
if st.button("Predict"):
    # Prepare data
    data = np.array([[preg, glu, dias, tri, ins, bmi, ped, age]])
    predicted_value = model_diabetes.predict(data)

    # Show result
    if predicted_value[0] == 1:
        st.error("The model predicts: **Diabetic**")
    else:
        st.success("The model predicts: **Not Diabetic**")
