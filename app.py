import streamlit as st

st.title("🧠 Mental Health Assessment App")

st.header("PHQ-9: Depression Screening")
questions = [
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

options = ["Not at all (0)", "Several days (1)", "More than half the days (2)", "Nearly every day (3)"]

total_score = 0
for q in questions:
    answer = st.selectbox(q, options)
    score = int(answer[-2])  # last number is the score
    total_score += score

if st.button("Submit"):
    st.success(f"Your total PHQ-9 score is: {total_score}")
    
    if total_score <= 4:
        st.info("Minimal depression. Keep maintaining good habits!")
    elif total_score <= 9:
        st.warning("Mild depression. Try relaxation and self-care techniques.")
    elif total_score <= 14:
        st.warning("Moderate depression. Consider talking to a professional.")
    else:
        st.error("Severe depression. It's recommended to seek professional help.")
