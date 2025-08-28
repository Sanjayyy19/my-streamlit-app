import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("loan_model.pkl")

st.set_page_config(page_title="Loan Approval App", page_icon="💰", layout="centered")
st.title("🏦 Loan Approval Prediction App")
st.write("Fill in the applicant details below:")

# Input fields with labels
no_of_dependents = st.number_input("👨‍👩‍👧 Number of Dependents", min_value=0, max_value=10, step=1, value=0)
education = st.selectbox("🎓 Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("💼 Self Employed", ["Yes", "No"])
income_annum = st.number_input("💵 Annual Income", min_value=0, value=500000)
loan_amount = st.number_input("🏠 Loan Amount", min_value=0, value=100000)
loan_term = st.number_input("📅 Loan Term (years)", min_value=1, value=10)
cibil_score = st.number_input("📊 CIBIL Score", min_value=300, max_value=900, value=750)
residential_assets_value = st.number_input("🏡 Residential Assets Value", min_value=0, value=100000)
commercial_assets_value = st.number_input("🏢 Commercial Assets Value", min_value=0, value=50000)
luxury_assets_value = st.number_input("🚗 Luxury Assets Value", min_value=0, value=20000)
bank_asset_value = st.number_input("🏦 Bank Asset Value", min_value=0, value=30000)

# Encode categorical fields
education_val = 1 if education == "Graduate" else 0
self_employed_val = 1 if self_employed == "Yes" else 0

# Prediction button
if st.button("🔍 Predict Loan Approval"):
    input_data = pd.DataFrame([[no_of_dependents, education_val, self_employed_val,
                                income_annum, loan_amount, loan_term, cibil_score,
                                residential_assets_value, commercial_assets_value,
                                luxury_assets_value, bank_asset_value]],
                              columns=["no_of_dependents","education","self_employed",
                                       "income_annum","loan_amount","loan_term","cibil_score",
                                       "residential_assets_value","commercial_assets_value",
                                       "luxury_assets_value","bank_asset_value"])

    prediction = model.predict(input_data)[0]

    if prediction == 1:   # if 1 means approved
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Rejected.")
