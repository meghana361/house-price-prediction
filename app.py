import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("modelreg.pkl", "rb"))

# Streamlit UI
st.title("🏡 House Price Prediction App")
st.write("Enter details to predict the house price.")

# Sidebar for inputs
st.sidebar.header("Enter House Features")

# User Inputs
sqft = st.sidebar.number_input("Square Feet", min_value=500, max_value=5000, value=1500)
bedrooms = st.sidebar.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.sidebar.number_input("Bathrooms", min_value=1, max_value=5, value=2)
location = st.sidebar.selectbox("Location", ["New York", "Los Angeles", "San Francisco"])
floors = st.sidebar.number_input("Number of Floors", min_value=1, max_value=3, value=1)
year_built = st.sidebar.number_input("Year Built", min_value=1900, max_value=2023, value=2000)
garage = st.sidebar.number_input("Garage Size (cars)", min_value=0, max_value=5, value=1)
crime_rate = st.sidebar.slider("Crime Rate (0 to 1)", min_value=0.0, max_value=1.0, value=0.1)

# Convert categorical location to numerical
location_mapping = {"New York": 0, "Los Angeles": 1, "San Francisco": 2}
location_num = location_mapping[location]

# Convert inputs into an array with all 8 features
input_features = np.array([[sqft, bedrooms, bathrooms, location_num, floors, year_built, garage, crime_rate]])

# Predict price when the button is clicked
if st.sidebar.button("Predict Price"):
    prediction = model.predict(input_features)  # Ensure model accepts raw input
    st.subheader(f"🏠 Estimated House Price: **${prediction[0]:,.2f}**")

