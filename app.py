import streamlit as st
import cv2
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow import keras
import os


def img_pred(img, weights_file):

    model = load_model(weights_file)

    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img = cv2.resize(opencvImage, (244, 244))
    img = img.reshape(1, 244, 244, 3)
    p = model.predict(img)
    p = np.argmax(p, axis=1)[0]

    return p


st.title("Scanostic")
st.header("Upload your MRI Scan image: ")


uploaded_img = st.file_uploader("Upload your image here...")

if uploaded_img is not None:
    img = Image.open(uploaded_img)
    st.image(img, caption="Uploaded scan image", use_column_width=True)

    st.write("Diagnosing...")

    st.write("")
    label = img_pred(img, 'mri_classifier_model.h5')
    if label == 0:
        st.write('\tTumor Detected- Consult a doctor immediately')
    else:
        st.write('\tNo tumor detected- You are healthy!')
