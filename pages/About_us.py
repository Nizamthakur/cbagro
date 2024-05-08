import streamlit as st
import base64

st.set_page_config(layout="wide")

st.header("About Us")

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

col1, col2 = st.columns(2)

with col1:
    st.title("Canada Bangla Agro")
    content = """ 
    We’re Canada Bangla Agro, an Agricultural Consulting Firm with a proven track record of supporting businesses in a
     variety of industries through results-driven consulting. We’ll give your company the attention it deserves, offering personalized solutions and guidance to help you meet and surpass your goals."""
    st.info(content)
    if st.button("View Products"):
        st.page_link('pages/Products.py')

with col2:
    try:
        # Display the logo as a favicon
        st.markdown(
            f'<link rel="shortcut icon" href="data:image/png;base64,{favicon_base64}" type="image/x-icon">',
            unsafe_allow_html=True
        )
        # Display the resized logo
        st.image("images/farm.png")
    except FileNotFoundError:
        st.error("Image file not found. Please check the file path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown("<h2 style='text-align: center; color: gray; font-weight: bold;'>Mission & Vision</h2>", unsafe_allow_html=True)
col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

# Define content for the Mission and Vision cards with background color
mission_content = """
<div style='background-color: #f2ebe7; padding: 10px; border-radius: 5px;'>
Canada Bangla Agro is committed to providing exceptional consulting services to businesses in the agricultural sector. Our mission is to help our clients achieve sustainable growth and success through innovative strategies and personalized solutions.
</div>
"""

vision_content = """
<div style='background-color:#f2ebe7; padding: 10px; border-radius: 5px;'>
Our vision is to become a leading consulting firm in the agricultural industry, recognized for our expertise, integrity, and dedication to client success. We strive to empower businesses to thrive in a rapidly evolving agricultural landscape.
</div>
"""

# Display Mission card
with col3:
    st.subheader("Mission")
    st.markdown(mission_content, unsafe_allow_html=True)

# Display Vision card
with col4:
    st.subheader("Vision")
    st.markdown(vision_content, unsafe_allow_html=True)

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
