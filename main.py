import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from io import StringIO

model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
ohe = joblib.load("ohe.pkl")

num_cols = ["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "EstimatedSalary"]
cat_cols = ["Geography", "Gender", "HasCrCard", "IsActiveMember"]

st.title("🔍 Bank Churn Prediction App")

st.warning(
    "⚠️ **The CSV file must contain a 'CustomerId' column** for identification, "
    "**and the following columns for features:** " + ", ".join(num_cols + cat_cols) + ". "
    "This is required **so the model can make predictions**. "
    "If you want to use your own data, please **clone the repository and run the model locally**, "
    "but make sure to **update the following variables in the `main.py` file** to match your data: "
    "**num_cols = [" + ", ".join(num_cols) + "]** and **cat_cols = [" + ", ".join(cat_cols) + "]**."
)

csv_url = "https://raw.githubusercontent.com/prajjukorban/Bank-Churn-Prediction-App-/main/Churn_Modelling.csv"
response = requests.get(csv_url)

if response.status_code == 200:
    df_sample = pd.read_csv(StringIO(response.text)).head(20)
    sample_csv = df_sample.to_csv(index=False)
    st.download_button(
        label="📥 Download Example CSV (20 Rows)",
        data=sample_csv,
        file_name="example_data.csv",
        mime="text/csv"
    )
else:
    st.error("Failed to fetch example CSV. Please check the file URL.")

uploaded_file = st.file_uploader("Upload customer CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if "CustomerId" not in df.columns:
        st.error("❌ 'CustomerId' column is required in the uploaded file.")
    else:
        try:
            df = df.dropna()
            X_num = scaler.transform(df[num_cols])
            X_cat = ohe.transform(df[cat_cols]).toarray()
            X = np.hstack([X_num, X_cat])

            df["Churn_Prediction"] = model.predict(X)
            df["Churn_Probability"] = model.predict_proba(X)[:, 1]

            output_df = df[["CustomerId", "Churn_Prediction", "Churn_Probability"] + num_cols + cat_cols]
            st.success("✅ Prediction Completed!")
            st.dataframe(output_df)

            csv = output_df.to_csv(index=False)
            st.download_button("📥 Download Predictions", data=csv, file_name="predictions_with_customerid.csv", mime='text/csv')

        except Exception as e:
            st.error(f"❌ Error during prediction: {e}")
