import gradio as gr
from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate(prompt):
    image = pipe(prompt).images[0]
    return image

gr.Interface(
    fn=generate,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="image",
    title="Stable Diffusion Text-to-Image",
    description="Generate an image using Stable Diffusion and Hugging Face's diffusers."
).launch()
