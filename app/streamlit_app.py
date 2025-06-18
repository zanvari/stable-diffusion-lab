import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

st.title("🧠 Stable Diffusion - Text to Image")
st.write("Generate images using Hugging Face Diffusers and Stable Diffusion.")

model_id = "runwayml/stable-diffusion-v1-5"
@st.cache_resource
def load_pipeline():
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    return pipe.to("cuda" if torch.cuda.is_available() else "cpu")

pipe = load_pipeline()

prompt = st.text_area("Enter your prompt", "A fantasy landscape with castles and waterfalls")

if st.button("Generate"):
    with st.spinner("Generating image..."):
        image = pipe(prompt).images[0]
        st.image(image, caption="Generated Image", use_column_width=True)
