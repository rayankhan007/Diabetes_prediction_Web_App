# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

loaded_model = pickle.load (open('C:/Users\zam/Desktop/Deploying ML mode/trained_model.sav', 'rb'))



input_data = (8,176,90,34,300,33.7,0.467,58)

#changing to data to numpy array

input_data_as_numpy_array = np.asarray(input_data)

#reshape the input data
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)



prediction = loaded_model.predict(input_data_reshaped)

print(prediction)
if (prediction[0]==0):
  print("The person is non diabetic")
else:
  print("The person is diabetic")