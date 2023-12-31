# Working Code



import streamlit as st
import base64
import requests

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

# Streamlit app
st.title("Image Describer + Caption Generator for Instagram✨")

# Upload image through Streamlit
image = st.file_uploader("Choose an image", type=["jpg", "jpeg"])

if image:
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Encode the image
    base64_image = encode_image(image)

    # OpenAI API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What’s in this image? Can you please generate 10 Instagram captions with text and emoji for posting this image on Instagram?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Display OpenAI API response
    # st.subheader("OpenAI API Response:")
    # st.json(response.json())

    # Display content from the response
    st.subheader("Here's the Description + Instagram Captions for the Image you Provided:")
    for choice in response.json()['choices']:
        content = choice['message']['content']
        st.write(content)



