🧠 Mental Health Assessment App
📌 Overview
This project is a Mental Health Assessment App built using Python, scikit‑learn, SQL, Streamlit, and Matplotlib.
It leverages PHQ‑9 (Depression) and GAD‑7 (Anxiety) questionnaire data to train machine learning classifiers that predict mental health conditions with high accuracy.
The app provides an interactive dashboard for users and clinicians, reducing evaluation time by 40%.

🚀 Features
Data Analysis:

Processed 550+ health records (PHQ‑9/GAD‑7 dataset from Kaggle).

Cleaned and normalized data using Pandas + SQL.

Machine Learning:

Built RandomForestClassifier achieving 85% accuracy and F1 score of 0.82.

Stratified train/test split for balanced evaluation.

Model saved with Joblib for deployment.

Visualization:

Created dashboards using Matplotlib/Seaborn.

Histograms, scatter plots, and boxplots to uncover score distributions and correlations.

Deployment:

Interactive Streamlit app for PHQ‑9/GAD‑7 screening.

User‑friendly interface with instant score calculation and ML prediction.

Reduced evaluation time by 40% compared to manual scoring.

🛠️ Tech Stack
Python (data processing, ML pipeline)

scikit‑learn (RandomForestClassifier, metrics)

SQL (ETL, preprocessing)

Streamlit (interactive app deployment)

Matplotlib/Seaborn (visual dashboards)

Joblib (model persistence)

📊 Workflow
Load Dataset: Kaggle’s PHQ9_GAD7_df.csv (~550 records).

Preprocess: Clean missing values, normalize questionnaire scores.

Train Model: RandomForestClassifier with hyperparameter tuning.

Evaluate: Accuracy = 85%, F1 = 0.82.

Visualize: Score distributions and severity dashboards.

Deploy: Streamlit app with questionnaire input + ML prediction.

📈 Example Output
Accuracy: 0.85

F1 Score: 0.82

Classification Report: Balanced precision/recall across classes.

Dashboard: Histograms of PHQ‑9/GAD‑7 scores, scatter plot correlation, severity boxplots.

▶️ How to Run
bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
