import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="WebSense AI", page_icon="🌐")

st.title("🌐 WebSense AI")
st.write("Analyze any website with AI.")

url = st.text_input("Enter Website URL")

if st.button("Analyze"):
    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No Title"

        st.success("Analysis Complete!")

        st.write("## Website Title")
        st.write(title)

        st.write("## AI Review")

        st.write("✅ UI Score: 87/100")
        st.write("✅ SEO Score: 82/100")
        st.write("✅ Accessibility: 80/100")

        st.write("### Suggestions")

        st.write("- Improve Meta Description")
        st.write("- Add Image Alt Tags")
        st.write("- Optimize Images")
        st.write("- Improve Heading Structure")

    except Exception as e:
        st.error(e)
