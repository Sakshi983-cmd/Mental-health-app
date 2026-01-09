import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.title("🧠 Mental Health Assessment App")

# Load trained model
model = joblib.load("mental_health_model.pkl")

# PHQ-9 Questions
phq9_questions = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself - or that you are a failure",
    "Trouble concentrating on things",
    "Moving or speaking slowly or being fidgety",
    "Thoughts that you would be better off dead"
]

options = {"Not at all":0, "Several days":1, "More than half the days":2, "Nearly every day":3}

scores = []
for q in phq9_questions:
    answer = st.selectbox(q, list(options.keys()))
    scores.append(options[answer])

if st.button("Submit"):
    total_score = sum(scores)
    st.success(f"Your total PHQ-9 score is: {total_score}")

    # Severity interpretation
    if total_score <= 4:
        st.info("Minimal depression. Keep maintaining good habits!")
    elif total_score <= 9:
        st.warning("Mild depression. Try relaxation and self-care techniques.")
    elif total_score <= 14:
        st.warning("Moderate depression. Consider talking to a professional.")
    else:
        st.error("Severe depression. It's recommended to seek professional help.")

    # Model prediction
    input_df = pd.DataFrame([scores], columns=[f"PHQ{i}" for i in range(1,10)])
    prediction = model.predict(input_df)[0]
    st.write(f"ML Model Prediction: {prediction}")

    # Dashboard visualization
    fig, ax = plt.subplots()
    ax.bar(range(1,10), scores, color="skyblue")
    ax.set_title("PHQ-9 Response Distribution")
    ax.set_xlabel("Question")
    ax.set_ylabel("Score")
    st.pyplot(fig)

