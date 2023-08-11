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