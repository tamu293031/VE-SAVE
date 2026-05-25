import streamlit as st

# Configuración de página
st.set_page_config(page_title="Smart Charge VE", page_icon="⚡")

# Estilos CSS para centrar todo y darle un aspecto limpio
st.markdown("""
    <style>
    .stApp { text-align: center; }
    .titulo-principal { font-size: 32px; font-weight: bold; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFAZ ---
st.markdown('<p class="titulo-principal">⚡ Smart Charge VE</p>', unsafe_allow_html=True)

st.write("---")

# Información optimizada
st.subheader("Horario óptimo hoy:")
st.info("### 02:00 - 06:00")

st.write("---")

st.subheader("Ahorro estimado:")
st.success("### 2.40€")

import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Smart Charge VE", page_icon="⚡")

# Estilos
st.markdown("<style>.stApp { text-align: center; }</style>", unsafe_allow_html=True)

# Lógica para obtener precios reales (Simulada por la estructura de la API)
def obtener_datos_luz():
    # En un entorno real, aquí iría la llamada a la API oficial
    # Por ahora, usamos esta estructura para que siempre funcione
    horario = "02:00 - 06:00"
    ahorro = "2.40€"
    return horario, ahorro

horario, ahorro = obtener_datos_luz()

# --- INTERFAZ ---
st.title("⚡ Smart Charge VE")
st.write("---")

st.subheader("Horario óptimo hoy:")
st.info(f"### {horario}")

st.subheader("Ahorro estimado:")
st.success(f"### {ahorro}")

st.write(f"Última actualización: {datetime.now().strftime('%H:%M')}")