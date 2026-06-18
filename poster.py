import streamlit as st
from PIL import Image
import os
o=os
# Set up page layout to be wide (dashboard style)
st.set_page_config(page_title="Poster Feedback AI (Local)", layout="wide")

st.title("🎨 Poster Feedback AI")
st.caption("Upload your design to get instant local feedback based on image layout and dimensions.")

st.markdown("---")

# Layout: Two columns
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.subheader("📁 Upload Poster")
    uploaded_file = st.file_uploader(
        "Drag and drop your poster here",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Your Design", use_container_width=True)

with col2:
    st.subheader("📊 Mock AI Feedback & Suggestions")

    if uploaded_file:
        with st.spinner("Analyzing layout and aspect ratios..."):
            # Extract basic image properties to simulate dynamic analysis
            width, height = image.size
            aspect_ratio = width / height
            file_size_kb = len(uploaded_file.getvalue()) / 1024

            # Formulate dynamic pseudo-scores based on file data
            hierarchy_score = 8 if aspect_ratio < 0.8 else 7
            composition_score = 9 if file_size_kb > 200 else 6

            # Render the feedback structure locally
            st.markdown(f"""
            ### 1. 📊 VISUAL HIERARCHY (Score: {hierarchy_score}/10)
            * **Observation:** The image uses a {'vertical/portrait' if aspect_ratio < 1 else 'horizontal/landscape'} layout. The human eye naturally scans this format from top-to-bottom, left-to-right.
            * **Suggestion:** Ensure your main headline is placed in the top third of the frame to capture attention immediately.

            ### 2. 🅰️ TYPOGRAPHY (Score: 7/10)
            * **Observation:** Text elements detected within standard boundaries. Contrast levels look sufficient for general readability.
            * **Suggestion:** Limit your design to a maximum of 2 font families (one for headings, one for body text) to keep it clean.

            ### 3. 🎨 COLOR PALETTE (Score: 8/10)
            * **Observation:** The image data indicates a balanced distribution of color values across the canvas area.
            * **Suggestion:** Try using the 60-30-10 rule: 60% dominant background color, 30% secondary structure color, and 10% sharp accent color for call-to-actions.

            ### 4. 📐 COMPOSITION & LAYOUT (Score: {composition_score}/10)
            * **Observation:** Current resolution is {width}x{height} pixels. {'The image has good density for high-quality printing.' if composition_score > 7 else 'The resolution is low; text elements might pixelate.'}
            * **Suggestion:** Always leave at least a 5% margin around the edge of the poster so text doesn't look like it's falling off the canvas.
            """)
    else:
        st.info("Upload a poster image on the left to generate local metrics and suggestions.")