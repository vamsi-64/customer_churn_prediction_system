--> CUSTOMER_CHURN_PREDICTION_SYSTEM <--


A Machine Learning-based Customer Churn Prediction System that predicts whether a customer is likely to leave a telecom service using classification algorithms and provides real-time predictions through a Streamlit web application.

The project uses multiple classification algorithms, compares their performance, selects the best-performing model, and deploys it through a user-friendly Streamlit web application for real-time predictions.

---

--> Features

- Predict customer churn in real time
- User-friendly Streamlit interface
- Data preprocessing and feature engineering
- Label Encoding for categorical variables
- Feature Scaling using StandardScaler
- Comparison of multiple Machine Learning algorithms
- Model performance evaluation
- Probability-based churn prediction
- Saved trained model for deployment

--> Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn
- VS code

---

📂 Project Structure

```
Customer_Churn_Prediction_System/
│
├── churn_prediction_fixed.ipynb    # Model training notebook
├── app.py                          # Streamlit application
├── model.pkl                       # Trained ML model
├── scaler.pkl                      # StandardScaler
├── encoders.pkl                    # Label Encoders
├── feature_columns.pkl             # Feature order
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## 📊 Machine Learning Algorithms

The following algorithms were implemented and compared:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest

The best-performing model was selected based on evaluation metrics such as accuracy.

---

--> Project Workflow

```
Dataset
    ↓
Data Preprocessing
    ↓
Handling Missing Values
    ↓
Label Encoding
    ↓
Feature Scaling
    ↓
Train-Test Split
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Best Model Selection
    ↓
Save Model
    ↓
Streamlit Web Application
    ↓
Customer Churn Prediction
```

---

--> Model Evaluation

Models were evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

The highest accuracy model was saved and used for deployment.

---

## 💻 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/customer_churn_prediction_system.git

cd customer_churn_prediction_system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

After running the command, the application will open in your browser.

---

## 📱 Application Screens

The Streamlit application allows users to:

- Enter customer details
- Predict customer churn
- Display prediction probability
- Show whether the customer is likely to Stay or Churn

---

## 📊 Dataset

The project uses a Telecom Customer Churn dataset containing customer demographic information, account details, subscribed services, billing information, and churn status.

Typical features include:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Online Security
- Tech Support
- Contract
- Payment Method
- Monthly Charges
- Total Charges
- Churn

---

## 🎯 Objectives

- Predict customer churn using Machine Learning.
- Compare multiple classification algorithms.
- Improve prediction accuracy through preprocessing.
- Deploy the trained model using Streamlit.
- Assist telecom companies in customer retention strategies.

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data Preprocessing
- Feature Engineering
- Machine Learning Classification
- Model Evaluation
- Model Deployment
- Streamlit Application Development
- Python Programming
- Git & GitHub

---

## Future Enhancements

- Add more advanced ML algorithms
- Hyperparameter tuning
- Explainable AI (SHAP/LIME)
- Cloud deployment
- Database integration
- User authentication
- Dashboard analytics

---

## 👨‍💻 Author

**Vamsi Krishna Reddy**

Computer Science Engineering (Cyber Security)

Machine Learning Intern

---

## 📄 License

This project is developed for educational and internship purposes.
