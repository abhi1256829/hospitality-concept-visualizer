import streamlit as st

from gemini_service import generate_text
from image_service import generate_image
from utils import validate_prompt

st.set_page_config(page_title="Hospitality Concept Visualizer", layout="wide")

st.title("Hospitality Concept Visualizer")
prompt = st.text_input(
    "Enter a hospitality prompt",
    placeholder="Luxury beach resort with sunset view",
)

if st.button("Generate"):
    is_valid, error_message = validate_prompt(prompt)

    if not is_valid:
        st.error(error_message)
    else:
        with st.spinner("Generating concept..."):
            try:
                text_result = generate_text(prompt)
                image_result = generate_image(prompt)

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Generated Text")
                    st.write(text_result)

                with col2:
                    st.subheader("Generated Image")
                    st.image(image_result, caption=prompt, use_container_width=True)

            except Exception as exc:
                st.error(str(exc))
