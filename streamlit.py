import streamlit as st
from transformers import pipeline

st.title("Sentiment Analysis App")


@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")


classifier = load_model()

text = st.text_area("Введите текст")

if st.button("Проверить"):
    if text:
        result = classifier(text)
        st.write(result)
    else:
        st.warning("Введите текст")
