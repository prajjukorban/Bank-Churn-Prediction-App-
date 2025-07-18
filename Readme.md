# 🔍 Bank Customer Churn Prediction App

A machine learning web application that predicts whether a bank customer is likely to churn (i.e., leave the bank) based on their personal and account-related data. Built with **Streamlit** and powered by a **Random Forest Classifier** trained on real-world churn data.
### Deployed on Render: <a href="https://bank-churn-prediction-app.onrender.com/">Click Here</a>

---

## 📌 Features

- ✅ Upload a CSV file with customer data
- 🔄 Automatically preprocesses the data (scaling & encoding)
- 🔍 Predicts customer churn (`Yes` or `No`)
- 📊 Shows churn probability
- 💾 Allows downloading of predictions with `CustomerId`

---

## 📁 Sample Input Format (CSV)

Ensure your file has these columns:

| Column Name        | Type      | Example         |
|--------------------|-----------|-----------------|
| CustomerId         | Integer   | 15634602        |
| CreditScore        | Integer   | 619             |
| Geography          | Categorical | France        |
| Gender             | Categorical | Female        |
| Age                | Integer   | 42              |
| Tenure             | Integer   | 2               |
| Balance            | Float     | 0.00            |
| NumOfProducts      | Integer   | 1               |
| HasCrCard          | Integer (0 or 1) | 1        |
| IsActiveMember     | Integer (0 or 1) | 1        |
| EstimatedSalary    | Float     | 101348.88       |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/churn-prediction-app.git
cd churn-prediction-app
