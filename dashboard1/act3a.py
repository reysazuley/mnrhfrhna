import streamlit as st  # Importing Streamlit to build a simple web app
import pandas as pd  # Importing pandas to handle data manipulation

# Set the title of the dashboard
st.title("Fetch and Display Data from Local Storange")

# Fetch data from a local file
file_path = './restaurant.csv'  # Replace this with the path to your local CSV file
local_data = pd.read_csv(file_path)  # Read the CSV file into a DataFrame

# Display the fetched data using Streamlit's dataframe component
st.subheader("Display Data from Local CSV File")  # Add a subheader
st.dataframe(local_data, use_container_width=True)   # Display the data interactively
st.caption("Displaying data using as.dataframe")   # Add a brief caption
