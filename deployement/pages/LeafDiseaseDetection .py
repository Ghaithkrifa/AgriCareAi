import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
from groq import Groq

client = Groq(
    api_key="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"
)

def process_diseases(diseases):
    unique_elements = sorted(set(diseases))
    diseases_str = ", ".join(unique_elements)
    user_input = f"How can {diseases_str}  leaf diseases be treated?"
    return user_input


# Function to detect diseases in an image
def detect_image(image):
    detected_classes = []
    img_array = np.array(image)

    model = YOLO("/home/krifa/Bureau/implementation/best (3) (1).pt")
    results = model(img_array)

    for result in results:
        img_with_boxes = result.plot()
        for box in result.boxes:
            class_id = int(box.cls)
            class_name = model.names[class_id]
            detected_classes.append(class_name)

    return img_with_boxes, list(dict.fromkeys(detected_classes))

def get_chat_completion(prompt):
    
    chat_completion = client.chat.completions.create(
    messages=[{ "role": "user", "content": prompt, } ],
    model="llama3-8b-8192",)
    response=chat_completion.choices[0].message.content
    return response

st.title("Disease Detection and Solution Finder")

uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg","webp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    detected_image, diseases = detect_image(image)
    detected_pil_image = Image.fromarray(detected_image)
    st.image(detected_pil_image, caption='Detected Image', width=500)
    user_input = process_diseases(diseases)

    if st.button("Get Solution"):
        if user_input:
            st.write(user_input)
            with st.spinner("Generating response..."):
                response = get_chat_completion(user_input)
            st.write(response)  # Change st.write_stream to st.write
        else:
            st.write("No diseases detected to generate a solution.")
