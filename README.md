# IntelliFeedback AI
### Student Feedback Analytics & Intelligence Platform

IntelliFeedback AI is a Python-based student feedback analysis project that uses Machine Learning to classify student feedback into Positive, Negative, and Neutral sentiments.

## Project Overview
The project helps analyze student feedback, understand sentiment distribution, and generate feedback reports through an interactive dashboard.

## Features
- Student feedback dataset analysis
- Text preprocessing
- AI-based sentiment classification
- Positive, Negative, and Neutral feedback prediction
- Interactive Streamlit dashboard
- Sentiment distribution charts
- Dataset upload (CSV)
- Downloadable feedback report

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Plotly
- NLTK

## Project Structure
```text
IntelliFeedback_AI/
│
├── data/
│   └── student_feedback.csv
│
├── src/
│   ├── preprocessing.py
│   ├── sentiment_analysis.py
│   ├── analytics.py
│   └── visualization.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/suvarna-dange/IntelliFeedback_AI.git
```

2. Open the project folder:
```bash
cd IntelliFeedback_AI
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## Machine Learning Model
The project uses:
- CountVectorizer for text feature extraction.
- Multinomial Naive Bayes for sentiment classification.

## Dataset
The project includes a sample dataset containing 50 student feedback records.

## Author
**Suvarna Dange**

GitHub: https://github.com/suvarna-dange