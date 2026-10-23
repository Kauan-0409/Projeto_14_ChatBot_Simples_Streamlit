import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

if "historico" not in st.session_state:
    st.session_state.historico = []

with st.container(border=True):
    st.title("ChatBot")

    for mensagem in st.session_state.historico:
        with st.chat_message(mensagem["role"]):
            st.write(mensagem["content"])

pergunta = st.chat_input("digite sua mensagem...")

if pergunta:
    st.session_state.historico.append({
        "role": "user",
        "content": pergunta
    })

    resposta = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=st.session_state.historico
    )

    texto = resposta.choices[0].message.content

    st.session_state.historico.append({
        "role": "assistant",
        "content": texto
    })

    st.rerun()