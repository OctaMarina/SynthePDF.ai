import fitz
import streamlit as st
import getpass
import os
from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import re

# Get the api key
load_dotenv()

google_api_key = os.environ.get("GOOGLE_API_KEY")

if not google_api_key:
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")


# Create the LLM
model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# Initialize the promt template
from langchain.prompts import PromptTemplate

summary_template = PromptTemplate(
    input_variables=["document_text"],
    template="""
You are a professional document summarizer.

Your task is to analyze the following block of text extracted from a PDF document. First, briefly infer what kind of document this is (e.g., legal contract, academic paper, invoice, manual, report, etc.). Then generate a clear and concise summary in bullet points.

Instructions:
- Start by stating what type of document it appears to be, in one short sentence.
- Then summarize the key points in bullet format (max 150 words total).
- Focus on the most relevant facts or ideas.
- Avoid copying entire sentences from the original.
- Use neutral, objective language.

Text to analyze:
{document_text}

Output:
"""
)

qa_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an intelligent assistant. You are given a block of text extracted from a PDF document.
Use only the information provided in the context below to answer the user's question as clearly and accurately as possible.

If the answer is not explicitly mentioned in the context, respond with "The answer is not available in the document."

Context:
{context}

Question:
{question}

Answer:
"""
)


# Initialize the promt chain
chain = summary_template | model

# Initialize the questions chain
qa_chain = qa_prompt | model

import streamlit as st
import fitz

# Page design
st.set_page_config(page_title="SynthePDF.ai", page_icon="📄", layout="centered")

# 🌟 Title
st.title("📄 SynthePDF.ai")

st.markdown(
    """
    *Turn long PDFs into clear, AI-powered summaries in seconds.*

    Upload any PDF, and let our AI extract the key ideas for you.  
    **No signup. No fluff. Just clarity.**
    """
)

st.divider()


uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])


if uploaded_file:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    st.success("✅ PDF uploaded successfully!")
    st.subheader("🔍 Raw Text Preview (First 100 characters):")
    st.code(text[:100], language="text")

    if st.button("🧠 Summarize PDF"):
        with st.spinner("Generating summary..."):
            try:
                summary = chain.invoke({"document_text": text})
                st.subheader("📝 Summary")
                summary_text = summary.content

                summary_text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", summary_text)

                summary_text = summary_text.replace("*", "•").replace("-", "•")

                st.markdown(f"""
                    <div style="background-color:#f9f9f9; padding: 15px; border-radius: 10px; border: 1px solid #ddd; color: #111; font-size: 15px; line-height: 1.6;">
                    {summary_text.replace("•", "<br>•")}
                    </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error during summarization: {e}")

    st.divider()
    st.subheader("❓ Ask a question about this PDF")

    user_question = st.text_input("Type your question here")
    ask_button = st.button("💬 Ask")

    if ask_button and user_question.strip():
        with st.spinner("Thinking..."):
            try:
                answer = qa_chain.invoke({
                    "context": text,
                    "question": user_question
                })
                st.markdown(f"**💬 Answer:** {answer.content}")
            except Exception as e:
                st.error(f"❌ Error answering question: {e}")
else:
    st.info("⬆️ Please upload a PDF file to begin.")