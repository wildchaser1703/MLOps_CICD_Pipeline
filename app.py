import streamlit as st

# streamlit ui
st.title("Calculator")
st.write("Enter a number to calculate its square, cube, and fifth power")

# get user input
n = st.number_input("Enter a number", value = 1, step = 1)

# calculate the results
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

# Display the results
st.write(f"Square :  {square}")
st.write(f"Cube :  {cube}")
st.write(f"Fifth Power :  {fifth_power}")