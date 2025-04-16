# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 01:42:42 2025

@author: zam
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load (open('C:/Users\zam/Desktop/diabetes-prediction-app/trained_model.sav', 'rb'))

# creating a function for prediction

def diabetes_prediction(input_data):
    


    #changing to data to numpy array

    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the input data
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)



    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)
    if (prediction[0]==0):
      return "The person is non diabetic"
    else:
      return "The person is diabetic"
  
    


def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web app')
    
    #getting the input data from the user
   
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('BloodPressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin value')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age of a person')
    
    
    
    #code for prediction
    diagnosis = ''
    
    
    # CREAting a button for prediction    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    
    
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    