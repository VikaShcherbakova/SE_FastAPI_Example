import streamlit as st
from transformers import pipeline

st.title("Sentiment Analysis App")


@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")


def analyze_text(classifier, text: str):
    return classifier(text)


classifier = load_model()

text = st.text_area("Введите текст")

if st.button("Проверить"):
    if text:
        try:
            result = analyze_text(classifier, text)
            st.write(result)
        except Exception as e:
            st.error(f"Ошибка: {e}")
    else:
        st.warning("Введите текст")
