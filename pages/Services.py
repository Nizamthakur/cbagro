import streamlit as st
import base64
import pandas as pd
from send_email import send_email
import os

st.set_page_config(layout="wide")

# Upload your logo file
logo_path = "images/logo.png"

# Check if the file exists
try:
    with open(logo_path, "rb") as f:
        favicon_bytes = f.read()
        favicon_base64 = base64.b64encode(favicon_bytes).decode()
except FileNotFoundError:
    st.error("Image file not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Display the favicon directly in the HTML header
st.markdown(
    f'<link rel="shortcut icon" href="data:image/png;base64,{favicon_base64}" type="image/x-icon">',
    unsafe_allow_html=True
)

st.markdown("<h1 style='margin-bottom: 60px; text-align: center;'>Our Services</h1>", unsafe_allow_html=True)

# services section

image_folder = "images"
services_info = [
    {
        "title": "Fish Feed",
        "description": "According to The State of World Fisheries and Aquaculture 2020 report by the Food and Agriculture Organization, Bangladesh ranks 3rd globally for fish extraction from open water bodies and 5th in aquaculture production."
                       " Moreover, Bangladesh ranks 4th globally and 3rd in Asia for tilapia fish production.",
        "image_name": "fish.jpg"
    },
    {
        "title": "Chicken Feed",
        "description": "The total market for commercial poultry feed (excluding home mixing) in Bangladesh is currently estimated at 3.05 MN MT, composed of 1.83 MN MT by the broiler sector and 1.23 MN MT by the layer sector. The farms produce 570 million tonnes of meat and 7.34 billion eggs annually."
                       " Poultry feed is primarily made from imported soybean and soy meals.",
        "image_name": "chicken.png"
    },
    {
        "title": "Cattle Feed",
        "description": "Bangladesh’s livestock and aquaculture production play an important role in maintaining the population’s livelihoods. Livestock is one of the fastest growing industries in Bangladesh,"
                       " contributing about 2 (1.90) percent to the country’s GDP and more than 16 (16.52) percent to the agriculture sector in FY 2021-22.",
        "image_name": "cattle.png"
    }
]

for service in services_info:
    col2, col3 = st.columns([1, 3])
    with col2:
        # Check if the image file exists
        image_path = os.path.join(image_folder, service["image_name"])
        if os.path.exists(image_path):
            st.image(image_path, width=100)
        else:
            st.error(f"Image file not found: {service['image_name']}. Please check the file path.")
    with col3:
        st.subheader(service["title"])
        st.write(service["description"])

if st.button("Talk To Us ", key="talk_to_us_button"):
    
    st.page_link("pages/Contact_Us.py")

button_style = """
    <style>
        .stButton>button {
            font-size: 16px;
            font-weight: bold;
            background-color: #3498db;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
        }
    </style>
"""
st.write(button_style, unsafe_allow_html=True)

# footer


footer_html = """
    <div style="background-color: #3498db; padding: 20px; text-align: center; margin-top: 60px;">
        <div>
            <p style="margin-bottom: 5px; color: white;">Canada Bangla Agro</p>
            <p style="margin-bottom: 5px; color: white;">123 Main Street, City, Province, Postal Code</p>
            <p style="margin-bottom: 5px; color: white;">Phone: (123) 456-7890 | Email: info@canadabanglaagro.com</p>
        </div>
        <hr style="margin-top: 20px; margin-bottom: 20px;">
        <div>
            <p style="margin-bottom: 5px; color: white;">© 2024 Canada Bangla Agro. All rights reserved.</p>
            <p style="margin-bottom: 5px; color: white;">Designed by Cb-agro</p>
        </div>
    </div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
