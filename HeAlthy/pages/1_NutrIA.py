import streamlit as st
from dotenv import load_dotenv

load_dotenv(dotenv_path='../')

st.title("NutrIA")
st.subheader("Seu nutricionista amigável. 🥗")

with st.sidebar:
    st.markdown("Aqui é necessário a priori definir algumas informações que serão necessárias para eu conseguir te ajudar!")
    Idade = st.select_slider(
        "Selecione o intervalo de idade",
        options=["10-20", "20-30", "30-40", "40-50", "50+"]
    )
    ativFisica = st.radio(
        "Qual é o seu grau de Atividade Física?",
        ["Não faço atividade física", "Pouca atividade física",
        "Faço atividade física constante"],
        captions = ["Nem tenta?", "Duas vezes por semana.", "Três vezes por semana para cima."]
    )




