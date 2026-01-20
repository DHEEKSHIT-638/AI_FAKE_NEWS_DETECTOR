import streamlit as st
import google.generativeai as genai
from PIL import Image

# CONFIGURATION

GOOGLE_API_KEY = "YOUR_API_KEY_HERE"  # insert your own API key from https://aistudio.google.com/apikey. Refer to Readme file for instructions.

genai.configure(api_key=GOOGLE_API_KEY)

# PAGE SETUP

st.set_page_config(
    page_title="AI Fake News Detector for Students",
    layout="wide"
)

st.title("📰 AI Fake News Detector for Students")
st.write(
    "This tool helps students analyze news articles or news images, assess credibility, "
    "and generate neutral summaries to reduce the spread of misinformation."
)

# SIDEBAR

with st.sidebar:
    st.subheader("Context")

    subject_domain = st.selectbox(
        "Subject Domain",
        ["General", "Politics", "Science", "Health", "Technology"]
    )

    st.info(
        "This information is used only to slightly tailor the explanation. "
        "It does not affect the credibility score logic."
    )

# FUNCTIONS

def get_gemini_response(prompt, image_data=None):
    model = genai.GenerativeModel("gemini-2.5-flash")
    content = [prompt]

    if image_data:
        content.extend(image_data)

    try:
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    return None

# MAIN INPUT

st.subheader("Provide News Content")

article_text = st.text_area(
    "Option 1: Paste the full news article or content here",
    height=220,
    placeholder="Paste news content copied from websites, blogs, or social media..."
)

uploaded_image = st.file_uploader(
    "Option 2: Upload an image of the news (screenshot / poster / headline)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded News Image", width="content")

# ANALYZE BUTTON

if st.button("Analyze Credibility"):
    if not article_text.strip() and uploaded_image is None:
        st.warning("Please provide either news text or a news image.")
    elif article_text.strip() and uploaded_image is not None:
        st.warning("Please provide either news text or a news image, not both.")
    else:
        with st.spinner("Analyzing credibility..."):

            image_data = input_image_setup(uploaded_image)

            prompt = f"""
You are an expert fact-checker and media literacy educator.

Analyze the following news content to help students assess its credibility.

If the input is an image, first extract and understand the visible text before analysis.

Content:
{article_text if article_text.strip() else "News provided as an image."}

Context:
- Target audience: University students (UG & PG)
- Subject domain: {subject_domain}

Your task:
1. Evaluate the credibility of the news
2. Identify possible signs of misinformation
3. Avoid making absolute claims
4. Clearly state uncertainty where applicable

Provide the output in the following format:

Credibility Score:
(Give a score between 0–100%)

Risk Level:
(Choose one: Likely Reliable / Needs Verification / Likely Fake / Not a News Article)
If the content does not resemble a news article (such as personal messages, questions, or random text), classify the risk level as "Not a News Article" and clearly explain why.

Explanation:
- Bullet-point explanation in simple student-friendly language
- Mention emotional language, bias, lack of sources, or logical gaps if present

Neutral Summary:
- Rewrite the content in a factual, unbiased, concise manner
- Remove sensational or misleading tone

Source Awareness Hint:
- Mention authoritative organizations or official bodies students should consult
- Do NOT include website URLs

Student Advice:
- 1–2 lines on how students should treat this information
"""

            response = get_gemini_response(prompt, image_data)

        # OUTPUT SECTION

        st.subheader("Analysis Result")
        st.markdown(response)

        # DOWNLOAD OPTION

        st.download_button(
            label="Download Analysis",
            data=response,
            file_name="fake_news_analysis.txt",
            mime="text/plain"
        )

# FOOTER

st.markdown("---")
st.caption(
    "⚠️ Disclaimer: This tool provides an AI-assisted credibility assessment. "
    "Students should always verify information using official and authoritative sources."
)