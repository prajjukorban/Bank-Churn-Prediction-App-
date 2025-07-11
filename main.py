import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and transformers
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
ohe = joblib.load("ohe.pkl")

# Define columns
num_cols = ["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "EstimatedSalary"]
cat_cols = ["Geography", "Gender", "HasCrCard", "IsActiveMember"]

st.title("🔍 Churn Prediction App (with Customer ID)")

uploaded_file = st.file_uploader("Upload customer CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if "CustomerId" not in df.columns:
        st.error("❌ 'CustomerId' column is required in the uploaded file.")
    else:
        try:
            # Preprocess features only
            df = df.dropna()
            X_num = scaler.transform(df[num_cols])
            X_cat = ohe.transform(df[cat_cols]).toarray()
            X = np.hstack([X_num, X_cat])

            # Predict churn
            df["Churn_Prediction"] = model.predict(X)
            df["Churn_Probability"] = model.predict_proba(X)[:, 1]

            # Show table
            output_df = df[["CustomerId", "Churn_Prediction", "Churn_Probability"] + num_cols + cat_cols]
            st.success("✅ Prediction Completed!")
            st.dataframe(output_df)

            # Download CSV
            csv = output_df.to_csv(index=False)
            st.download_button("📥 Download Predictions", data=csv, file_name="predictions_with_customerid.csv", mime='text/csv')

        except Exception as e:
            st.error(f"❌ Error during prediction: {e}")
