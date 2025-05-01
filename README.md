# Mental-health-app
AI-powered Mental Health Assessment App using Streamlit. Built as part of BrainAI Internship Assignment.# Mental Health Assessment App

## Project Overview
This is an AI-powered mental health assessment application built using Streamlit. The app allows users to fill out mental health questionnaires such as PHQ-9 and GAD-7 to assess their mental well-being. Based on the user's responses, it provides a prediction and personalized mental health recommendations.

### Technologies Used
- Streamlit (for building the web app)
- Python (for backend development)
- Scikit-learn (for ML model)
- Pandas, NumPy (for data handling)

---

## Setup Instructions

### Prerequisites
Before running the app, make sure you have the following installed:
- Python 3.x
- pip (for installing Python packages)

### Steps to Run the App:- https://github.com/Sakshi983-cmd/Mental-health-app.git
    cd Mental-health-app
    
 Install the required dependencies- pip install -r requirements.txt
    ```
Run the app using Streamlit:-streamlit run app.py
    

## API Documentation

### Endpoints

1. **POST /submit-answers**
   - **Description**: Submits the user's answers to the mental health questionnaire.
   - **Method**: POST
   - **Payload**:
     ```json
     {
       "phq_9_score": 9,
       "gad_7_score": 7
     }
     ```
   - **Response**:
     ```json
     {
       "prediction": "Mild depression",
       "recommendations": "Try relaxation and self-care techniques."
     }
     ```

---

## Environment Variables


```env
MODEL_PATH=app.py


## 🚀 Live Demo APP-https://mental-health-app-6bubvcw2yuqzgbjkumhald.streamlit.app/

Click here to try the app 👉 [Mental Health App Live](https://mental-health-app-6bubvcw2yuqzgbjkumhald.streamlit.app/)
