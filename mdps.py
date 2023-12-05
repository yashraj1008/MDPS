# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:46:46 2023

@author: Aditya
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart',],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies (Range: 1-10)')
        
    with col2:
        Glucose = st.text_input('Glucose Level (Ramge: 80 - 200)')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value(Range: 0 -122 )')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value (Range:0 - 60 )')
    
    with col2:
        Insulin = st.text_input('Insulin Level (Range: 0 - 1000)')
    
    with col3:
        BMI = st.text_input('BMI value (Range: 0 - 70)')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value(Range: 0 - 2 )')
    
    with col2:
        Age = st.text_input('Age of the Person (Range: 0 - 100 )')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age (Range:0-100 )')
        
    with col2:
        sex = st.text_input('Sex (Range:M->0 , F->1)')
        
    with col3:
        cp = st.text_input('Chest Pain types(Range: 1 - 3 )')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (Range: 100 - 200 )')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl (Range: 50  - 200)')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results(R:0-1 )')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina (Range:0-1 )')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise(Range:0-3.0 )')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (Range:0-2 )')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy(Range: 0-1)')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    
