import streamlit as st
import pandas as pd
import joblib
# from sklearn.preprocessing import StandardScaler

# -----------------------------
# Load trained model & scaler
# -----------------------------
# Make sure you trained & saved them before
# pickle.dump(model, open("car_model.pkl", "wb"))
# pickle.dump(scaler, open("scaler.pkl", "wb"))

model = joblib.load(open("cardekhopkl.pkl", "rb"))
# scaler = pickle.load(open(r"C:\Users\sheeshragar\Desktop\machinelearing\standscaler.pkl", "rb"))

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🚗 Car Price Prediction App")

st.write("Enter car details to predict its **selling price**.")

# Inputs
year = st.number_input("Year of Purchase", 1990, 2025, 2015)
present_price = st.number_input("Present Price (in lakhs)", 0.0, 50.0, 5.0, step=0.1)
kms_driven = st.number_input("Kms Driven", 0, 500000, 20000)
owner = st.selectbox("Owner (Number of Previous Owners)", [0, 1, 2, 3])

# Label encoded categories
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# -----------------------------
# Apply Label Encoding Mapping
# -----------------------------
fuel_map = {"Petrol": 2, "Diesel": 1, "CNG": 2}
seller_map = {"Dealer": 0, "Individual": 1}
transmission_map = {"Manual": 1, "Automatic": 0}

data = {
    'Year': year,
    'Present_Price': present_price,
    'Kms_Driven': kms_driven,

    'Fuel_Type': fuel_map[fuel_type],
    'Seller_Type': seller_map[seller_type],
    'Transmission': transmission_map[transmission],
    'Owner': owner,
}
# ['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type',
    #    'Transmission', 'Owner']
df = pd.DataFrame([data])

# Scale numeric features
# scaler.fit(df)
# scaled_features = scaler.transform(df)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict Price"):
    prediction = model.predict(df)[0]
    st.success(f"💰 Estimated Selling Price: {prediction:.2f} lakhs")
