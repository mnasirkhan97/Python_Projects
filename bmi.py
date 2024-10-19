import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def convert_height(height, unit):
    if unit == "Centimeters":
        return height / 100
    elif unit == "Feet":
        return height * 0.3048
    return height  # Already in meters

def convert_weight(weight, unit):
    if unit == "Pounds":
        return weight * 0.453592
    return weight  # Already in kilograms

# Streamlit layout
st.set_page_config(page_title="BMI Calculator", page_icon="🏋️‍♂️")
st.title("🏋️‍♂️ BMI Calculator")

st.markdown("""
<style>
    .title {
        text-align: center;
        color: #4CAF50;
    }
    .header {
        text-align: left;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# Input section with styling
st.header("Enter Your Details")
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight:", min_value=0.0, step=0.1, format="%.1f")
    weight_unit = st.selectbox("Select weight unit:", ["Kilograms", "Pounds"])

with col2:
    height = st.number_input("Height:", min_value=0.0, step=0.1, format="%.1f")
    height_unit = st.selectbox("Select height unit:", ["Meters", "Centimeters", "Feet"])

# Calculate BMI button with a custom style
if st.button("Calculate BMI", key="calculate"):
    if height > 0:  # Prevent division by zero
        weight_kg = convert_weight(weight, weight_unit)
        height_m = convert_height(height, height_unit)
        
        bmi = calculate_bmi(weight_kg, height_m)
        st.success(f"Your BMI is: **{bmi:.2f}**")

        # BMI categories with improved visuals
        if bmi < 18.5:
            st.warning("Category: **Underweight**")
            st.markdown("👉 It's important to maintain a healthy weight. Consult a healthcare provider.")
        elif 18.5 <= bmi < 24.9:
            st.success("Category: **Normal weight**")
            st.markdown("✅ Keep up the good work!")
        elif 25 <= bmi < 29.9:
            st.warning("Category: **Overweight**")
            st.markdown("⚠️ Consider a balanced diet and regular exercise.")
        else:
            st.error("Category: **Obesity**")
            st.markdown("🚨 Please consult a healthcare provider for guidance.")
        
        # Ideal BMI range
        st.markdown("---")
        st.info("**Ideal BMI Range:**")
        st.write("The World Health Organization (WHO) defines a normal BMI range as **18.5 to 24.9**.")
    else:
        st.warning("Height must be greater than zero.")

# Additional information section
st.markdown("---")
st.header("What is BMI?")
st.write("BMI (Body Mass Index) is a measure of body fat based on height and weight.")
st.write("It helps categorize individuals into different weight categories.")

st.markdown("---")
st.write("Developed By Nasir")
