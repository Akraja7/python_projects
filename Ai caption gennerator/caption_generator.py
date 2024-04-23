import requests
import streamlit as st
API_URL_SEMANTICS = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"

API_URL_CAPTION = "https://api-inference.huggingface.co/models/google/gemma-7b"

headers = {"Authorization": f"Bearer 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"}



def generate_semantics(file):
    response = requests.post(API_URL_SEMANTICS, headers=headers, data=file)
    return response.json()[0]["generated_text"]

def generate_caption(payload):
	response = requests.post(API_URL_CAPTION, headers=headers, json=payload)
	return response.json()[0]["generated_text"]

st.title("AI CAPTION GENERATOR")


file = st.file_uploader("Upload an Image", type=['jpg', 'png', 'jpeg'])

if file:

    col1 , col2 = st.columns(2)
    with col1:
         st.image(file,use_column_width=True)
    with col2:
        with st.spinner("Generating Semantics..."):
            senmantics = generate_semantics(file)
            st.subheader("Semantics")
            st.write(senmantics)

        with st.spinner("Generating Caption..."):
            prompt_dict = {"inputs": f"Question : Convert the following image semantics {senmantics} to an instagram caption for my post .Make sure to add hash tags and emojis. : Answer:"}
            caption_raw = generate_caption(prompt_dict)
            st.subheader("Caption")
            caption = caption_raw.split("Answer:")[1]
            st.write(caption)
        
            
