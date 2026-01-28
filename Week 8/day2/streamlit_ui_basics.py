import streamlit as st

st.set_page_config(page_title="Week 8 - DAY 2",page_icon="🧠", layout="centered")

st.title("🧠 Streamlit Deep Learning")
st.write("Today we learn layouts, inputs and outputs step by step")

# section 1 on different text outputs
st.header("Section 1: Basic Text Output")
st.write("This is a normal text on the page")
st.success("This is a success message")
st.warning("This is a warning message")
st.error("This is an error message")

# section 2 on user inputs through text and slider
st.header("Section 2: User inputs")

name = st.text_input("Enter your name")
age = st.slider("Select your age", min_value=10, max_value=60, value=22)

st.write(f"Your name is: {name}")
st.write(f"Your age is: {age}")

# section 3 on buttons
st.header("Section 3: Buttons")

if st.button("Say Hello"):
    st.success(f"Hello {name}! You clicked the button ✅")
else:
    st.write("Click the button to see a message.")

# section 4 on layouts
st.header("Section 4: Sidebar + Columns")

st.sidebar.title("Controls")
confidence_threshold = st.sidebar.slider("Confidence threshold", 0.0, 1.0, 0.5)

col1, col2 = st.columns(2)

with col1:
    st.info("Left column")
    st.write("We can put text, charts, images here.")

with col2:
    st.info("Right column")
    st.write(f"Threshold set to: {confidence_threshold}")


# section 5 on images
from PIL import Image

st.header("Section 5: Upload an Image")

uploaded_file = st.file_uploader("Upload an image (jpg/png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.success("Image uploaded successfully ✅")
else:
    st.write("Please upload an image to continue.")


# section 6 on fake prediction output
import random

st.header("Section 6: Prediction Output (Demo)")

cifar10_classes = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

if uploaded_file is not None:
    if st.button("Predict (Demo)"):
        predicted_class = random.choice(cifar10_classes)
        confidence = round(random.uniform(0.50, 0.99), 2)

        st.subheader("Prediction Result")
        st.write(f"**Predicted Class:** {predicted_class}")
        st.write(f"**Confidence:** {confidence}")

        # simple confidence check
        if confidence >= confidence_threshold:
            st.success("Confidence is above threshold ✅")
        else:
            st.warning("Confidence is below threshold ⚠️")
