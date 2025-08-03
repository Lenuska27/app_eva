
import streamlit as st
import pandas as pd
import random

@st.cache_data
def load_data():
    return pd.read_excel("eva.xlsx")

df = load_data()

st.set_page_config(page_title="Рандомайзер от Евы 💫", page_icon="💫", layout="centered")

st.title("✨ Рандомайзер от Евы ✨")
st.markdown("Выбери, что хочешь получить 👇")

st.markdown("""
    <style>
        .stButton>button {
            font-size: 18px;
            height: 3em;
            width: 100%;
            border-radius: 10px;
            margin-bottom: 10px;
            background-color: #fbeaff;
            color: black;
            border: 2px solid #caa4f7;
        }
        .stButton>button:hover {
            background-color: #e3c6ff;
            color: black;
        }
        .result-box {
            padding: 20px;
            border-radius: 15px;
            background-color: #fff0fb;
            text-align: center;
            font-size: 20px;
            margin-top: 20px;
            border: 1px solid #f3d2f7;
        }
    </style>
""", unsafe_allow_html=True)

def get_random_value(column):
    if column not in df.columns:
        return "⚠️ Нет такого столбца"
    values = df[column].dropna().tolist()
    if not values:
        return "⚠️ Пустой столбец"
    return random.choice(values)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💖 Комплимент"):
        result = get_random_value("Комплименты")
        st.markdown(f"<div class='result-box'>💖 {result}</div>", unsafe_allow_html=True)

with col2:
    if st.button("🕺 Действие"):
        result = get_random_value("Действия")
        st.markdown(f"<div class='result-box'>🕺 {result}</div>", unsafe_allow_html=True)

with col3:
    if st.button("❓ Вопрос"):
        result = get_random_value("Вопросы")
        st.markdown(f"<div class='result-box'>❓ {result}</div>", unsafe_allow_html=True)
