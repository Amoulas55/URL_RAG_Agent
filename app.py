import streamlit as st
from rag_pipeline import answer_question_from_url

st.set_page_config(page_title="URL RAG Assistant", layout="wide")

st.title("🔎 URL RAG Assistant")
st.markdown("This assistant reads a URL and answers your question using a local model.")

# Input fields
url_input = st.text_input(
    "Enter a webpage URL:",
    placeholder="https://example.com/article"
)

question_input = st.text_area(
    "Ask your question about the content:",
    placeholder="e.g., What are the key takeaways?"
)

# Action
if st.button("Get Answer"):
    if not url_input or not question_input:
        st.warning("Please provide both a URL and a question.")
    else:
        with st.spinner("⏳ Processing..."):
            try:
                answer = answer_question_from_url(url_input, question_input)
                st.success("✅ Answer generated!")
                st.markdown(f"**Answer:**\n\n{answer}")  # ✅ This line shows the answer
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
