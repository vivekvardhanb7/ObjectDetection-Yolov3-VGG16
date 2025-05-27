import streamlit as st
import os
from PIL import Image
from detection import Detector
import uuid
import shutil

# Set page config
st.set_page_config(
    page_title="🔍 YOLOv3 Object Detection",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better visuals
st.markdown("""
    <style>
    .reportview-container {
        background: #f9f9f9;
    }
    .sidebar .sidebar-content {
        background: #f0f2f6;
    }
    .css-1d391kg, .css-1v3fvcr {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stButton > button {
        border-radius: 12px;
        background-color: #4CAF50;
        color: white;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# UI Header
st.title("🔍 YOLOv3 Object Detection App")
st.markdown("Welcome to the intelligent object detection tool powered by **YOLOv3** 🧠. Just upload an image, click detect, and see the magic happen! ✨")

# Upload image
uploaded_file = st.file_uploader("📤 Upload an image (jpg/jpeg/png)", type=["jpg", "jpeg", "png"])

# Image preview and detection
if uploaded_file is not None:
    # Save uploaded image temporarily
    temp_dir = "temp_images"
    os.makedirs(temp_dir, exist_ok=True)
    unique_filename = f"{uuid.uuid4()}.jpg"
    file_path = os.path.join(temp_dir, unique_filename)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.markdown("✅ **Image successfully uploaded!** Preview below 👇")
    st.image(file_path, caption="📸 Uploaded Image", use_container_width=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        detect_button = st.button("🚀 Detect Objects")
    with col2:
        clear_button = st.button("🧹 Clear Image")

    # Object Detection
    if detect_button:
        with st.spinner("🔍 Detecting objects... Please wait..."):
            detector = Detector()
            detector.do_detect(file_path)

        st.success("🎯 Detection completed!")

        # Reload updated image with boxes
        detected_image = Image.open(file_path)
        st.image(detected_image, caption="📍 Detected Image", use_container_width=True)

    # Clear temp files
    if clear_button:
        shutil.rmtree(temp_dir)
        st.experimental_rerun()
else:
    st.info("📎 Please upload an image to begin.")
