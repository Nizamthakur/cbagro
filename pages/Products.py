import streamlit as st
import base64
import pandas as pd
from send_email import send_email  # Assuming you have a custom module for sending emails

st.set_page_config(layout="wide")

st.header("Products")

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




col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv("data.csv", sep=",")

# Display products in two columns
with col1:
    for index, row in df[:3].iterrows():
        st.image("images/" + row["image"], width=400)
        st.markdown(f"<h3 style='color:green; padding-left: 100px;'>{row['title']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-weight:bold; font-size:20px;'>Description</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-weight:san;'>{row['description']}</p>", unsafe_allow_html=True)

with col2:
    for index, row in df[3:].iterrows():
        st.image("images/" + row["image"], width=400)
        st.markdown(f"<h3 style='color:green; padding-left: 100px;'>{row['title']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-weight:bold; font-size:20px;'>Description</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-weight:san;'>{row['description']}</p>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color:black; font-weight: bold; margin-top: 60px;'>Get In Touch</h2>", unsafe_allow_html=True)



with st.form(key ="user_email"):
    user_email = st.text_input("Your Email Address")
    raw_massage = st.text_area("Your massage Here")
    subject = f"New email from {user_email}"
    message = f"""\
            Subject: {subject}\n
            From: {user_email}\n
            {raw_massage}
            """
    button = st.form_submit_button("submit")
    print(button)
    if button:
        send_email(message)
        st.info("your email was sent sucesfully ")


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
