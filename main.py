import streamlit as st

# ----------------------------
# Page & CSS Configuration
# ----------------------------
st.set_page_config(
    page_title="Awesome Unit Converter",
    page_icon="🔄",
    layout="wide"
)

st.markdown("""
    <style>
        /* Set the dark theme background for the page */
        body {
            background: #121212;
            color: #E0E0E0;
            margin: 0;
            padding: 0;
        }
        /* Ensure the main Streamlit app container is dark */
        .stApp {
            background-color: #121212;
        }
        /* Header styling */
        .box{
            display:none;
            }
            .element-container{
            margin-top:20px;
            }
        .header {
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
            font-size: 3rem;
            margin-top: 20px;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        }
        .subheader {
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
            font-size: 1.5rem;
            margin-bottom: 20px;
            color: #b3b3b3;
        }
        /* Box container styling with dark background */
        .box {
            background-color: #1e1e1e;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.6);
            margin: auto;
            max-width: 600px;
            border: none;
        }
        /* Style selectbox and number input (if needed) */
        .stSelectbox, .stNumberInput {
            background-color: #1e1e1e;
            color: #E0E0E0;
        }
        /* Remove any extra white borders or spacing */
        .css-18e3th9 {
            border: none;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>Awesome Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Convert Length, Weight, and Temperature with style!</p>", unsafe_allow_html=True)

# ----------------------------
# Main Container for Converter
# ----------------------------
with st.container():
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    
    # Conversion category selection
    category = st.selectbox("Select conversion category", ("Length", "Weight", "Temperature"))
    
    # Value input
    value = st.number_input("Enter value", value=0.0, format="%.4f")
    
    # ----------------------------
    # Define allowed units and default values per category
    # ----------------------------
    if category == "Length":
        units = {"Meters": 1.0, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084}
        allowed_units = list(units.keys())
        default_from = "Meters"
        default_to = "Kilometers"
    elif category == "Weight":
        units = {"Grams": 1.0, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274}
        allowed_units = list(units.keys())
        default_from = "Grams"
        default_to = "Kilograms"
    elif category == "Temperature":
        allowed_units = ["Celsius", "Fahrenheit", "Kelvin"]
        default_from = "Celsius"
        default_to = "Fahrenheit"
    
    # ----------------------------
    # Dropdowns for selecting "From" and "To" units
    # ----------------------------
    from_unit = st.selectbox("From", allowed_units, index=allowed_units.index(default_from))
    to_unit = st.selectbox("To", allowed_units, index=allowed_units.index(default_to))
    
    # ----------------------------
    # Conversion Logic
    # ----------------------------
    if category in ["Length", "Weight"]:
        # Convert via base unit
        base_value = value / units[from_unit]
        result = base_value * units[to_unit]
    elif category == "Temperature":
        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
    
    # ----------------------------
    # Display the conversion result
    # ----------------------------
    st.markdown(f"<h2 style='text-align: center; color: #ffffff;'>Result: {result:.4f}</h2>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
