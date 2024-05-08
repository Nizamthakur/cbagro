import streamlit as st
import base64
import  pandas as pd
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

col1, col2 = st.columns(2)

with col1:
    try:
        # Display the logo as a favicon
        st.markdown(
            f'<link rel="shortcut icon" href="data:image/png;base64,{favicon_base64}" type="image/x-icon">',
            unsafe_allow_html=True
        )
        # Display the resized logo
        st.image("images/logo.png")
    except FileNotFoundError:
        st.error("Image file not found. Please check the file path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

with col2:
    st.title("Canada Bangla Agro")
    content = """ 
We are Canada Bangla Agro, an Agricultural Consulting Firm with a well-established history of assisting businesses across diverse industries with effective consulting services. Our commitment is to provide your company with tailored solutions and expert guidance to not only meet but exceed your objectives.

At Canada Bangla Agro, our founding mission is singular: to emerge as the foremost innovative and successful consulting agency in the agricultural sector. We view each client with a unique perspective, crafting individualized strategies to drive success."""
    st.info(content)

# # Define image paths for the first section
# image_folder = "images"
# image_names = ["1.jpeg", "2.jpg"]
# image_paths = [os.path.join(image_folder, name) for name in image_names]
#
# # Display placeholder for the slider
# slider_placeholder = st.empty()
#
# # Function to update the slider with sliding effect
# def update_slider(image_path):
#     slider_placeholder.image(image_path, use_column_width=True)
#
# # Loop to display images with sliding effect for the first section
# idx = 0
# while True:
#     update_slider(image_paths[idx % len(image_paths)])
#     time.sleep(3)  # Pause for 3 seconds before showing the next image
#     idx += 1
# Read the data from the CSV file
# Display the "Our Products" title
st.markdown("<h2 style='text-align: center; color:gray; font-weight: bold;'>Our Products</h2>", unsafe_allow_html=True)
col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv("data.csv", sep=",")






# Display products in two columns
with col3:
    for index, row in df[:3].iterrows():

        # st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.markdown(f"<h3 style='color:green; padding-left: 100px;'>{row['title']}</h3>", unsafe_allow_html=True)

with col4:
    for index, row in df[3:].iterrows():

        # st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.markdown(f"<h3 style='color:green; padding-left: 100px;'>{row['title']}</h3>", unsafe_allow_html=True)


#services section

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


st.markdown("""
    <div style='text-align: center; padding: 5px;'>
        <h2 style='border: 2px solid gray; display: inline-block; padding: 5px;'>Our Services</h2>
    </div>
""", unsafe_allow_html=True)

# Display the services section

for service in services_info:
    col5, col6 = st.columns([1, 3])
    with col5:
        # Check if the image file exists
        image_path = os.path.join(image_folder, service["image_name"])
        if os.path.exists(image_path):
            st.image(image_path, width=100)
        else:
            st.error(f"Image file not found: {service['image_name']}. Please check the file path.")
    with col6:
        st.subheader(service["title"])
        st.write(service["description"])




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