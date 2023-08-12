# importing libraries
import streamlit as st

# Welcome Page and Page Configuration
st.set_page_config(
    page_title="Brian",
    initial_sidebar_state="expanded",
    layout="centered"
)

# Class for BMI calculation
class Calculation:
    def BMICalculator(self, Height, Mass):
        if Height <= 0:
            st.warning("Height must be greater than zero.")
            return
        
        # Calculate BMI using the formula: BMI = Mass / (Height * Height)
        BMI = Mass / (Height * Height)
        
        # Defines BMI categories and corresponding descriptions
        bmi_categories = [
            (16, "Extremely underweight", "You are at a significantly low weight. Consider consulting a healthcare professional."),
            (18.5, "Underweight", "Your weight is below the healthy range. Focus on a balanced diet and exercise."),
            (25, "Normal Weight", "Congratulations! Your weight falls within the healthy range."),
            (30, "Overweight", "Your weight is above the healthy range. Consider adopting healthier habits."),
            (35, "Moderately obese", "Your weight is in the obese range. It's important to prioritize your health."),
            (float("inf"), "Extremely obese", "Your weight is at a level of extreme obesity. Seek guidance from a healthcare provider.")
        ]
        
        for t1, t2, t3 in bmi_categories:
            if BMI <= t1:
                # Displays the calculated BMI, the corresponding category, and an informative description
                st.write("Your BMI is", BMI, "Status:", t2)
                st.write(t3)
                break

# Set title for the Streamlit app
st.title("Brian - Body Mass Index Analyzer and Interpreter ")
st.write("Brian is an app that calculates individuals Body Mass Index using Height and Weight.")
st.header("Enter your parameters below: ")

# Input fields for height and weight
Height = st.number_input("Enter Height (m)", step=0.01)
Mass = st.number_input("Enter Weight (kg)", step=0.01)

# Instance of the Calculation class
obj = Calculation()

# Button to calculate BMI
if st.button("Calculate BMI"):
    # Check if both fields are entered before calculating BMI
    if Height is None or Mass is None or Height == "" or Mass == "":
        st.warning("Please enter both height and weight before calculating BMI.")
    else:
        # Call the BMICalculator method and display the results
        obj.BMICalculator(Height, Mass)

# Information about Brian and ModelX
st.write("Brian is the sub-version of ModelX. A standard runway supermodel prediction model that uses BMI and other physical attributes to calculate individuals compatibility with runway modeling.")
modelX = 'Test [ModelX](https://modelx.streamlit.app/)'
st.markdown(modelX, unsafe_allow_html=True)

link = 'Created by [Gideon Ogunbanjo](https://gideonogunbanjo.netlify.app)'
st.markdown(link, unsafe_allow_html=True)
