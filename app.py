import venv
import os
from transformers import pipeline

import streamlit as st
from transformers import pipeline
from utils import clasificar_intencion, generar_respuesta  # Funciones personalizadas

# Configuración de la página
st.set_page_config(page_title="Asistente SISTECRÉDITO", layout="centered")
st.title("🤖 Asistente Virtual de Negociación")

# Entrada del usuario
user_input = st.text_input("Describe tu situación financiera:", placeholder="Ej: No puedo pagar esta cuota...")

if user_input:
    # 1. Clasificar la intención
    intencion = clasificar_intencion(user_input)  # Usando BERT/DistilBERT
    
    # 2. Generar respuesta basada en la intención
    respuesta = generar_respuesta(user_input, intencion)
    
    # Mostrar resultado
    st.markdown(f"**Propuesta de acuerdo:**\n\n{respuesta}")