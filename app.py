import streamlit as st
import requests
import json
from places import get_companies_in_tech_park
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('Google_Maps_API_KEY')

# Set the title and a brief description for your app
st.title("Company Finder")
st.write("Enter the name of a tech park to find companies listed there.")

# Create a text input for the user
tech_park_name = st.text_input("Enter Tech Park Name:", "Manyata Tech Park, Bengaluru")

# Create a button to trigger the search
if st.button("Find Companies"):
    if not API_KEY or API_KEY == "YOUR_Google Maps_API_KEY":
        st.error("Please provide a valid Google Maps API Key in the script.")
    elif tech_park_name:
        # Show a loading spinner while the search is in progress
        with st.spinner(f"Searching for companies in {tech_park_name}..."):
            company_list = get_companies_in_tech_park(API_KEY, tech_park_name)
        
        if company_list:
            st.success(f"Found the following companies in {tech_park_name}:")
            for company in company_list:
                st.write(f"- {company}")
        else:
            st.warning("No companies found or an error occurred. Please try a different name.")
    else:
        st.warning("Please enter a tech park name.")