import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Predictor",layout="centered")


def load_artifacts():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    encoders = joblib.load("encoders.pkl")          # dict: {column_name: fitted LabelEncoder}
    feature_columns = joblib.load("feature_columns.pkl")  # exact training column order
    return model, scaler, encoders, feature_columns


try:
    model, scaler, encoders, feature_columns = load_artifacts()
except FileNotFoundError:
    st.error(
        "Couldn't find model.pkl / scaler.pkl / encoders.pkl / feature_columns.pkl.\n\n"
        "Run the notebook's last cell first to generate these files, then place them "
        "in the same folder as app.py."
    )
    st.stop()


categorical_cols = [c for c in feature_columns if c in encoders and c != "Churn"]
numeric_cols = [c for c in feature_columns if c not in encoders]


st.title("Customer Churn Prediction")
st.write(
    "Enter a customer's details below and the model will predict whether "
    "they're likely to churn."
)

st.subheader("Customer details")
user_input = {}
col1, col2 = st.columns(2)
columns_cycle = [col1, col2]
slot = 0

for col in categorical_cols:
    options = list(encoders[col].classes_)
    with columns_cycle[slot % 2]:
        user_input[col] = st.selectbox(col, options)
    slot += 1

for col in numeric_cols:
    with columns_cycle[slot % 2]:
        if col == "SeniorCitizen":
            choice = st.selectbox("SeniorCitizen", ["No", "Yes"])
            user_input[col] = 1 if choice == "Yes" else 0
        elif col == "tenure":
            user_input[col] = st.number_input(
                "tenure (months)", min_value=0, max_value=100, value=12, step=1
            )
        else:
            user_input[col] = st.number_input(col, min_value=0.0, value=50.0, step=1.0)
    slot += 1

st.divider()

if st.button("Predict Churn", type="primary"):
    # Build a single-row dataframe, encoding categoricals exactly like training
    row = {}
    for col in feature_columns:
        val = user_input[col]
        if col in encoders:
            val = encoders[col].transform([val])[0]
        row[col] = val

    input_df = pd.DataFrame([row])[feature_columns]
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]
    st.subheader("Prediction Result")
    if prediction == 1:
        st.snow()
        st.error(f"This customer is likely to **churn**. (Probability: {probability:.1%})")
    else:
        st.balloons()
        st.success(f"This customer is likely to **stay**. (Churn probability: {probability:.1%})")
else:
    st.info("Enter the customer details and click **Predict Churn**.")