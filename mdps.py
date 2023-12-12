 
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))



# # sidebar for navigation
# with st.sidebar:
    
#     selected = option_menu('Multiple Disease Prediction System',
                          
#                           ['Diabetes Prediction',
#                            'Heart Disease Prediction'],
#                           icons=['activity','heart',],
#                           default_index=0)
    
    
# # Diabetes Prediction Page
# if (selected == 'Diabetes Prediction'):
    
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
    Age = st.text_input('Enter Age of the Person (Range: 0 - 100)')
    
    
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





        
    
    
