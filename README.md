# Accident Severity Prediction Using Machine Learning

## Project Overview
This project predicts the severity of road accidents using machine learning techniques on the US Accidents dataset. The model is trained on historical accident data and deployed as a web application using Streamlit.

## Dataset
- Dataset: US_Accidents_March23.csv
- Source: Kaggle

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Machine Learning Models Used
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

## Best Model
Random Forest Classifier was selected as the best model based on accuracy.

## Features Used
- Start_Lat
- Start_Lng
- Distance(mi)
- Temperature(F)
- Humidity(%)
- Pressure(in)
- Visibility(mi)
- Wind_Speed(mph)
- Precipitation(in)
- End_Lat
- End_Lng
- Wind_Chill(F)

## Project Workflow
1. Loaded the US Accidents dataset.
2. Explored the dataset using `head()`, `shape`, and `columns`.
3. Checked for missing values using `isnull().sum()`.
4. Filled missing numerical values with the median.
5. Selected relevant numerical features.
6. Defined the target variable (`Severity`).
7. Split the dataset into training and testing sets.
8. Trained three machine learning models:
   - Logistic Regression
   - Decision Tree Classifier
   - Random Forest Classifier
9. Evaluated model performance using accuracy score.
10. Selected the best-performing model.
11. Saved the model using `pickle`.
12. Built a Streamlit web application for prediction.
13. Allowed users to enter feature values manually.
14. Predicted accident severity using the trained model.
15. Uploaded the complete project to GitHub.

## Files in the Project
- `sample.ipynb` – Jupyter Notebook containing all preprocessing, training, and evaluation code.
- `app.py` – Streamlit web application.
- `model.pkl` – Saved trained machine learning model.
- `requirements.txt` – Python dependencies.
- `README.md` – Project documentation.

## How to Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
