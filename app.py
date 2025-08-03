import streamlit as st
import pandas as pd
import random

# Загружаем Excel-файл
@st.cache_data
def load_data():
    return pd.read_excel("eva.xlsx")

df = load_data()

# Настройки страницы
st.set_page_config(page_title="Рандомайзер от Вани 💫", page_icon="💫", layout="centered")

# Заголовок
st.title("✨ Рандомайзер от Вани ✨")
st.markdown("Выбери, что хочешь получить 👇")

# Стили
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

# Функция для случайного выбора
def get_random_text(column):
    if column in df.columns:
        values = df[column].dropna().tolist()
        if values:
            return random.choice(values)
        else:
            return "⚠️ В этом разделе пока нет данных."
    else:
        return "⚠️ Столбец не найден в таблице."

# Кнопки
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💖 Комплимент"):
        text = get_random_text("Комплимент")
        st.markdown(f"<div class='result-box'>💖 {text}</div>", unsafe_allow_html=True)

with col2:
    if st.button("🕺 Действие"):
        text = get_random_text("Действие")
        st.markdown(f"<div class='result-box'>🕺 {text}</div>", unsafe_allow_html=True)

with col3:
    if st.button("❓ Вопрос"):
        text = get_random_text("Вопрос")
        st.markdown(f"<div class='result-box'>❓ {text}</div>", unsafe_allow_html=True)

