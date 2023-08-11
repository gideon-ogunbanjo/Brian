# importing libraries
import streamlit as st

# Class for BMI calculation
class Calculation:
    def BMICalculator(self, Height, Mass):
        # Calculate BMI using the formula: BMI = Mass / (Height * Height)
        BMI = Mass / (Height * Height)