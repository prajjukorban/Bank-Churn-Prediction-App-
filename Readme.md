
# 🔍 Bank Customer Churn Prediction App

This is a machine learning-powered web application built with **Streamlit** that predicts whether a bank customer will churn (i.e., leave the bank). It uses a **Random Forest Classifier** trained on real-world data and includes preprocessing steps like scaling and encoding.

---

## 📌 Features

- Upload customer data via CSV
- Automatically preprocesses (scaler + encoder)
- Predicts churn and shows churn probability
- Displays results in a table
- Download the final result as a CSV
- Keeps `CustomerId` in output for tracking

---

## 📁 Sample Input File Format (CSV)

The file should contain the following **column headers**:

| Column Name        | Type             | Example     |
|--------------------|------------------|-------------|
| CustomerId         | Integer          | 15634602    |
| CreditScore        | Integer          | 619         |
| Geography          | Categorical      | France      |
| Gender             | Categorical      | Female      |
| Age                | Integer          | 42          |
| Tenure             | Integer          | 2           |
| Balance            | Float            | 0.00        |
| NumOfProducts      | Integer          | 1           |
| HasCrCard          | 0 or 1           | 1           |
| IsActiveMember     | 0 or 1           | 1           |
| EstimatedSalary    | Float            | 101348.88   |

---

## 🚀 Getting Started

### 🔧 Step 1: Clone the Project

```bash
git clone https://github.com/YOUR-USERNAME/churn-prediction-app.git
cd churn-prediction-app


---

📦 Step 2: Install Dependencies

pip install -r requirements.txt

Or, manually:

pip install streamlit pandas numpy scikit-learn joblib


---

▶️ Step 3: Run the Streamlit App

streamlit run app.py


---

📂 Project Structure

churn-prediction-app/
├── app.py                  # Streamlit web app
├── churn_model.pkl         # Trained RandomForest model
├── scaler.pkl              # StandardScaler for numeric data
├── ohe.pkl                 # OneHotEncoder for categorical data
├── requirements.txt        # Python dependencies
└── README.md               # You're reading it :)


---

🧠 How It Works

Model: RandomForestClassifier trained on customer churn dataset.

Preprocessing:

StandardScaler for numerical features

OneHotEncoder for categorical features


Output Columns:

Churn_Prediction: 0 = Not Churn, 1 = Churn

Churn_Probability: Confidence score (0.0 to 1.0)




---

📥 Output Example

CustomerId	Churn_Prediction	Churn_Probability

15634602	1	0.83
15647311	0	0.32


You can download this final prediction table directly from the app UI.


---

📜 requirements.txt

streamlit
pandas
numpy
scikit-learn
joblib


---

🏦 Real-Life Usage

This tool helps banks:

Identify high-risk customers

Take preventive actions (calls, offers, support)

Improve retention and reduce revenue loss



---

✍️ Author

Prajwal K.
BTech CSE (Data Science) | MERN Stack Dev
📫 [your-email@example.com] • 🌐 [https://your-portfolio.com] • 💼 [https://linkedin.com/in/yourprofile]


---

📘 License

This project is licensed under the MIT License.

---

You're ready to go! Let me know if you want the `app.py` file or help deploying to Streamlit Cloud too.

