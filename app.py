
import streamlit as st

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")
st.write("Ask me questions about Artificial Intelligence and Machine Learning.")

questions = {
    "what is ai": "Artificial Intelligence (AI) is the ability of machines to perform tasks that normally require human intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI where computers learn patterns from data and make predictions or decisions.",
    "what is deep learning": "Deep Learning is a part of Machine Learning that uses neural networks with multiple layers to learn from large amounts of data.",
    "what is neural network": "A neural network is a computing model inspired by the human brain. It consists of connected nodes called neurons.",
    "what is nlp": "Natural Language Processing (NLP) is a field of AI that helps computers understand and process human language.",
    "what is computer vision": "Computer Vision is an AI field that enables computers to understand images and videos."
}

user_question = st.text_input("💬 Enter your question:")

if user_question:
    question = user_question.lower().strip()

    if question in questions:
        st.success(questions[question])
    else:
        st.info("Sorry, I don't have