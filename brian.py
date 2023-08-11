# importing libraries
import streamlit as st

# Class for BMI calculation
class Calculation:
    def BMICalculator(self, Height, Mass):
        # Calculate BMI using the formula: BMI = Mass / (Height * Height)
        BMI = Mass / (Height * Height)
        
        # Defines BMI categories and corresponding descriptions
        for t1, t2 in [
            (16, "Severely underweight"),
            (18.5, "Underweight"),
            (25, "Normal"),
            (30, "Overweight"),
            (35, "Moderately obese"),
            (float("inf"), "Severely obese"),
        ]:
            if BMI <= t1:
                # Displays the calculated BMI and the corresponding category
                st.write("Your BMI is", BMI, " The individual is:", t2)
                break
            
# Set title for the Streamlit app
st.title("Briann - Body Mass Index Analyzer and Interpreter ")
st.write("Brian is an app that calculates individuals Body Mass Index using Height and Weight.")
st.header("Enter your parameters below: ")

# Input fields for height and weight
Height = st.number_input("Enter Height (m)", step=0.01)
Mass = st.number_input("Enter Weight (kg)", step=0.01)

# Instance of the Calculation class
obj = Calculation()

# Button to calculate BMI
if st.button("Calculate BMI"):
    # Call the BMICalculator method and display the results
    obj.BMICalculator(Height, Mass)