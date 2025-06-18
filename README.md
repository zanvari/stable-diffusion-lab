# 🧪 Stable Diffusion Lab

A hands-on, tutorial-driven project for experimenting with various Stable Diffusion pipelines using Hugging Face's `diffusers` library.

## 📚 Tutorials Included

| Notebook | Description |
|----------|-------------|
| [`01_txt2img_tutorial.ipynb`](./notebooks/txt2img_tutorial.ipynb) | Generate images from text prompts |
| [`02_inpainting_tutorial.ipynb`](./notebooks/inpainting_tutorial.ipynb) | Modify masked image areas using prompts |
| [`03_img2img_tutorial.ipynb`](./notebooks/img2img_tutorial.ipynb) | Transform images using guiding prompts |

---

## ✨ Prompt Ideas

### Text-to-Image Prompts
- `"A futuristic cityscape at sunset, highly detailed"`
- `"A magical forest with glowing plants and floating lanterns"`
- `"An astronaut playing guitar on the moon, digital art"`
- `"A cat wearing a spacesuit in a spaceship cockpit"`

### Inpainting Use Cases
- Remove objects from background and regenerate surroundings
- Replace sky with dramatic sunset
- Change outfits or accessories in portraits
- Fill missing or damaged parts of an image creatively

### Image-to-Image Prompts
- `"Turn this pencil sketch into a realistic portrait"`
- `"Make this daytime photo look like night with neon lights"`
- `"Convert this rough landscape into a digital oil painting"`

---

## 🖥️ App Interfaces

| App | File | Description |
|-----|------|-------------|
| Gradio | [`app/gradio_app.py`](./app/gradio_app.py) | Launches a Gradio web UI for text-to-image generation |
| Streamlit | [`app/streamlit_app.py`](./app/streamlit_app.py) | Launches a Streamlit app with prompt input and image output |

To run locally:
```bash
# Gradio
python app/gradio_app.py

# Streamlit
streamlit run app/streamlit_app.py
```

---

## 🧰 Requirements

```bash
pip install -r requirements.txt
```

---

## 🧠 Author

By **Zahra Anvari**

---

## 📜 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it with attribution.
