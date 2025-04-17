# Diabetes Prediction Web App

A machine learning-based web application to predict diabetes risk using patient health metrics, built with Streamlit.


## Features

- Predicts diabetes risk based on 8 health parameters
- Simple and intuitive user interface
- Fast prediction using a pre-trained SVM model
- Local deployment capability

## Tech Stack

- **Python** (Primary language)
- **Scikit-learn** (Machine learning)
- **Streamlit** (Web interface)
- **NumPy** (Data processing)
- **Pickle** (Model serialization)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/diabetes-prediction-app.git
   cd diabetes-prediction-app


## Install dependencies:
   pip install -r requirements.txt


## Download the pre-trained model:

  -Place trained_model.sav in the project root directory

## Usage
-Run the Streamlit app:

## bash
-streamlit run app.py
-Open your browser to http://localhost:8501

## Enter patient health parameters:

Number of Pregnancies

Glucose Level

Blood Pressure

Skin Thickness

Insulin Level

BMI

Diabetes Pedigree Function

Age

Click "Diabetes Test Result" to get prediction

## File Structure

diabetes-prediction-app/

**Streamlit web application**  
-app.py

**Model training script**    
-model_training.py

**Pre-trained SVM model**    
-trained_model.sav

**Python dependencies**      
-requirements.txt 

**This file**                
-README.md          


## Model Details
Algorithm: Support Vector Machine (SVM)

Input Features: 8 health parameters

Output: Binary prediction (Diabetic/Non-Diabetic)

Accuracy: 77% 

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## 📜 License  
This project is licensed under the [MIT License](LICENSE).

Acknowledgments
Dataset: Pima Indians Diabetes Database



